#!/usr/bin/env python3
"""Rebuild chart-reading.html from vedic-chart-analysis.md, into the page's
existing design system.  The <head>/CSS block is preserved verbatim."""
import html
import re

SRC = '/home/user/Analyse-/vedic-chart-analysis.md'
DST = '/home/user/Analyse-/chart-reading.html'
OLD = open(DST, encoding='utf-8').read()
HEAD = OLD.split('</style>')[0] + '</style>\n'

MAST = '''
<div class="wrap">
  <header class="masthead">
    <div class="eyebrow">Parashari reading · shodashavarga · shadbala · ashtakavarga · jaimini · transits</div>
    <h1>The difficulty and the fortune are the same object</h1>
    <p class="standfirst">A Kanya lagna with seven of nine grahas packed into two adjacent houses — the 8th and the 9th — which are in mutual exchange, which contain every raja yoga the chart possesses, and which measure among the weakest ground it owns.</p>

    <dl class="facts">
      <div class="fact"><dt>Lagna</dt><dd>27°37′ Kanya</dd></div>
      <div class="fact"><dt>Chandra</dt><dd>Krittika 2 · exalted</dd></div>
      <div class="fact"><dt>Mahadasha</dt><dd>Rahu → 2040</dd></div>
      <div class="fact"><dt>Antardasha</dt><dd>Guru → Jan 2028</dd></div>
      <div class="fact"><dt>Derived birth</dt><dd>15 Apr 2002, Mon</dd></div>
      <div class="fact"><dt>Audit</dt><dd>53 / 53 checks pass</dd></div>
    </dl>
  </header>
</div>
'''

FOOT = '''
    <p class="pull">The difficulty and the fortune<br>are the same object.</p>

    <footer>
      Prepared from supplied D1, D9, D10, D11, D8, D27, D30, upagraha, Vimshottari, Shadbala, Bhava Bala, Ashtakavarga, Reduced Ashtakavarga, Shodhya Pinda and transit data. All divisional charts, dasha boundaries and strength tables were independently recomputed from Swiss Ephemeris and verified. Forty-four scripts accompany this reading; <code>verify_audit.py</code> re-derives and asserts all 53 headline figures. Twenty-eight divisional schemes are computed and the sixteen Shodashavarga charts are printed in full. An earlier claim of node errors in D8 and D30 is retracted in §51; two unreconcilable columns are identified there and excluded. An interpretation within the framework of Jyotisha, presented on its own terms.
    </footer>
  </section>
</div>
'''


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    # Italics first, so that **bold containing *italic* inside** still closes.
    t = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    return t


def cell_class(raw):
    """Short, numeric or symbol-heavy cells get the tabular class."""
    s = re.sub(r'[*_`]', '', raw).strip()
    if not s or s == '—':
        return ' class="n"'
    if len(s) <= 22 and not re.search(r'[a-z]{4,}\s+[a-z]{4,}\s+[a-z]{4,}', s):
        return ' class="n"'
    return ''


def render_table(rows):
    out = ['<div class="scroll">', '<table>']
    head = rows[0]
    out.append('<thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head)
               + '</tr></thead>')
    out.append('<tbody>')
    for r in rows[1:]:
        tds = []
        for i, c in enumerate(r):
            cls = '' if i == 0 and cell_class(c) == '' else cell_class(c)
            if i == 0:
                cls = '' if len(re.sub(r'[*_`]', '', c)) > 22 else cls
            tds.append(f'<td{cls}>{inline(c)}</td>')
        out.append('<tr>' + ''.join(tds) + '</tr>')
    out += ['</tbody>', '</table>', '</div>']
    return '\n'.join(out)


def split_row(line):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [c.strip() for c in line.split('|')]


lines = open(SRC, encoding='utf-8').read().split('\n')
body, i = [], 0
section_open = False
n_sec = 0
buf = []


def flush():
    global buf
    if buf:
        txt = ' '.join(x.strip() for x in buf).strip()
        if txt:
            body.append(f'<p>{inline(txt)}</p>')
        buf = []


while i < len(lines):
    ln = lines[i]

    # skip the document title and the standfirst block before section 1
    if ln.startswith('# '):
        i += 1
        while i < len(lines) and not lines[i].startswith('## '):
            i += 1
        continue

    if ln.startswith('## '):
        flush()
        if section_open:
            body.append('  </section>\n</div>\n')
        n_sec += 1
        m = re.match(r'## (\d+)\.\s*(.*)', ln)
        num, title = (m.group(1), m.group(2)) if m else ('', ln[3:])
        body.append('<div class="wrap">\n  <section>')
        body.append(f'    <h2><span class="num">{int(num):02d}</span> '
                    f'{inline(title)}</h2>')
        section_open = True
        i += 1
        continue

    if ln.startswith('##### '):
        flush(); body.append(f'<h4>{inline(ln[6:])}</h4>'); i += 1; continue
    if ln.startswith('#### '):
        flush(); body.append(f'<h4>{inline(ln[5:])}</h4>'); i += 1; continue
    if ln.startswith('### '):
        flush(); body.append(f'<h3>{inline(ln[4:])}</h3>'); i += 1; continue

    if ln.strip() == '---':
        flush(); i += 1; continue

    if ln.startswith('|'):
        flush()
        rows = []
        while i < len(lines) and lines[i].startswith('|'):
            if not re.match(r'^\|[\s:\-|]+\|?\s*$', lines[i]):
                rows.append(split_row(lines[i]))
            i += 1
        body.append(render_table(rows))
        continue

    if ln.startswith('```'):
        flush()
        i += 1
        code = []
        while i < len(lines) and not lines[i].startswith('```'):
            code.append(html.escape(lines[i], quote=False))
            i += 1
        i += 1
        body.append('<div class="callout"><p><code>'
                    + '<br>'.join(code) + '</code></p></div>')
        continue

    if ln.startswith('> '):
        flush()
        # blank '>' lines separate paragraphs inside one blockquote
        chunks, cur = [], []
        while i < len(lines) and lines[i].startswith('>'):
            t = lines[i].lstrip('>').strip()
            if t:
                cur.append(t)
            elif cur:
                chunks.append(' '.join(cur)); cur = []
            i += 1
        if cur:
            chunks.append(' '.join(cur))
        body.append('<div class="callout big">'
                    + ''.join(f'<p>{inline(c)}</p>' for c in chunks)
                    + '</div>')
        continue

    if re.match(r'^[-*] ', ln):
        flush()
        items = []
        while i < len(lines) and (re.match(r'^[-*] ', lines[i])
                                  or (lines[i].startswith('  ') and items)):
            if re.match(r'^[-*] ', lines[i]):
                items.append(lines[i][2:].strip())
            else:
                items[-1] += ' ' + lines[i].strip()
            i += 1
        body.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in items)
                    + '</ul>')
        continue

    if re.match(r'^\d+\. ', ln):
        flush()
        items = []
        while i < len(lines) and (re.match(r'^\d+\. ', lines[i])
                                  or (lines[i].startswith('   ') and items)):
            if re.match(r'^\d+\. ', lines[i]):
                items.append(re.sub(r'^\d+\. ', '', lines[i]).strip())
            else:
                items[-1] += ' ' + lines[i].strip()
            i += 1
        cls = ' class="takeaways"' if len(items) >= 8 else ''
        body.append(f'<ol{cls}>'
                    + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ol>')
        continue

    if ln.startswith('*Prepared from'):
        flush(); i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith('>'):
            i += 1
        continue

    if not ln.strip():
        flush(); i += 1; continue

    buf.append(ln)
    i += 1

flush()

out = HEAD + MAST + '\n'.join(
    ('    ' + b) if not b.startswith(('<div class="wrap">', '  </section>',
                                     '  <section>', '    <h2>')) else b
    for b in body) + FOOT
open(DST, 'w', encoding='utf-8').write(out)
print(f'{n_sec} sections, {len(out.splitlines())} lines written')
