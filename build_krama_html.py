#!/usr/bin/env python3
"""Rebuild chart-reading.html from vedic-chart-analysis.md, into the page's
existing design system.  The <head>/CSS block is preserved verbatim."""
import html
import re

SRC = '/home/user/Analyse-/bhava-krama.md'
DST = '/home/user/Analyse-/bhava-krama.html'
import os
OLD = open(DST if os.path.exists(DST) else
           '/home/user/Analyse-/chart-reading.html', encoding='utf-8').read()
HEAD = OLD.split('</style>')[0] + '</style>\n'

MAST = '''
<div class="wrap">
  <header class="masthead">
    <div class="eyebrow">Par&#257;&#347;ari bhava krama &middot; twelve houses &middot; ten steps &middot; in order</div>
    <h1>The chart, judged in classical order</h1>
    <p class="standfirst">Every house taken in turn through the classical sequence &mdash; bhava, lord, k&#257;raka, varga, planetary strength, bhava strength, affliction, dasha, ashtakavarga &mdash; with no technique given a percentage weight and none allowed to speak before its turn.</p>

    <dl class="facts">
      <div class="fact"><dt>Lagna</dt><dd>27&deg;37&prime; Kanya</dd></div>
      <div class="fact"><dt>Empty bhavas</dt><dd>8 of 12</dd></div>
      <div class="fact"><dt>Untouched</dt><dd>1st &middot; 5th &middot; 7th</dd></div>
      <div class="fact"><dt>All twelve lords</dt><dd>in 3 houses</dd></div>
      <div class="fact"><dt>Strongest bhava</dt><dd>the 12th</dd></div>
      <div class="fact"><dt>Weakest bhava</dt><dd>the 8th</dd></div>
    </dl>
  </header>
</div>
'''

FOOT = '''
    <p class="pull">The chart is not twelve departments.<br>It is three rooms administering twelve.</p>

    <footer>
      Every house judged in the Par&#257;&#347;ari sequence: subject, bhava, bhava lord, natural k&#257;raka, relevant varga, planetary strength, bhava strength, affliction and yoga, dasha, and ashtakavarga last. Computed by <code>verify_krama_all.py</code> from the verified birth moment; strength figures from the supplied Shadbala, Bhava Bala and Ashtakavarga tables, independently reproduced by <code>verify_bala.py</code>. No technique carries a percentage weight. The 63-section reading in <code>vedic-chart-analysis.md</code> holds the derivations, the alternative methods and the record of every correction; this is that material re-judged in order, not a replacement for it.
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
        m = re.match(r'## Bhava (\d+) — (.*)', ln)
        body.append('<div class="wrap">\n  <section>')
        if m:
            body.append(f'    <h2><span class="num">{int(m.group(1)):02d}</span> '
                        f'{inline(m.group(2))}</h2>')
        else:
            body.append(f'    <h2>{inline(ln[3:])}</h2>')
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
