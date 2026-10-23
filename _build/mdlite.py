"""A small Markdown subset to HTML: headings, paragraphs, lists, tables, bold, italic, code, links.
Enough for the standard's drafts; no dependency to install."""
import html, re

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<em>\1</em>', t)
    t = re.sub(r'\[([^\]]+)\]\(((?:https?://|mailto:|/)[^)]+)\)', r'<a href="\2">\1</a>', t)
    t = re.sub(r'(?<![">=])(https?://[^\s<)]+)', r'<a href="\1">\1</a>', t)
    t = re.sub(r'(\S+?)((?:\[\d+\])+)', lambda m: '<span class="nb">' + m.group(1) + ''.join(
        f'<sup class="fn">[{n}]</sup>' for n in re.findall(r'\d+', m.group(2))) + '</span>', t)  # one or more marks, e.g. [1][2]
    return t

def table(lines, cell=inline):
    rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in lines]
    head, body = rows[0], [r for r in rows[2:]]
    h = ''.join(f'<th>{cell(c)}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{cell(c)}</td>' for c in r) + '</tr>' for r in body)
    return f'<div class="tw"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

def convert(md, cell=inline, hshift=0):
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    out, lines, i = [], md.split('\n'), 0
    while i < len(lines):
        l = lines[i]
        if not l.strip(): i += 1; continue
        m = re.match(r'^(#{1,6})\s+(.*)', l)
        if m:
            n = min(6, len(m.group(1)) + hshift)
            out.append(f'<h{n}>{inline(m.group(2))}</h{n}>'); i += 1; continue
        if l.lstrip().startswith('|'):
            blk = []
            while i < len(lines) and lines[i].lstrip().startswith('|'): blk.append(lines[i]); i += 1
            out.append(table(blk, cell)); continue
        if re.match(r'^\s*([-*]|\d+\.)\s', l):
            tag = 'ol' if re.match(r'^\s*\d+\.', l) else 'ul'
            items = []
            while i < len(lines) and re.match(r'^\s*([-*]|\d+\.)\s', lines[i]):
                items.append(re.sub(r'^\s*([-*]|\d+\.)\s', '', lines[i])); i += 1
                while i < len(lines) and lines[i].startswith('  ') and lines[i].strip() and not re.match(r'^\s*([-*]|\d+\.)\s', lines[i]):
                    items[-1] += ' ' + lines[i].strip(); i += 1
            out.append(f'<{tag}>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + f'</{tag}>'); continue
        if l.startswith('>'):
            q = []
            while i < len(lines) and lines[i].startswith('>'): q.append(lines[i].lstrip('> ')); i += 1
            out.append('<blockquote><p>' + inline(' '.join(q)) + '</p></blockquote>'); continue
        if l.startswith('```'):
            i += 1; blk = []
            while i < len(lines) and not lines[i].startswith('```'): blk.append(lines[i]); i += 1
            i += 1; out.append('<pre>' + html.escape('\n'.join(blk)) + '</pre>'); continue
        p = [l]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|\||\s*[-*]\s|\s*\d+\.\s|>|```)', lines[i]):
            p.append(lines[i]); i += 1
        out.append('<p>' + inline(' '.join(x.strip() for x in p)) + '</p>')
    return '\n'.join(out)
