"""Build index.html (one page, a tab per section) from whiteboard/board.json.

Run from the repo root: python3 tools/build.py
"""
import json, html, re, sys

D = json.load(open('whiteboard/board.json'))
E = D['elements']; ORDER = D['meta']['order']

FILL = {'blue': '#dbe8fb', 'peach': '#fbd9b8', 'yellow': '#fdf0b0', 'white': '#ffffff',
        'green': '#d9efd3', 'pink': '#f9d6e0', 'purple': '#e6dcf7'}
INK = {'ink': '#1d1d1b', 'terracotta': '#b4532a', 'blue': '#2f5fa8', 'green': '#2f7a3a', 'purple': '#6a4fb3'}
SIZE = {'small': 14, 'body': 16, 'large': 28, 'title': 48, 'huge': 96}


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<i>\1</i>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    s = re.sub(r'\[(.+?)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', s)
    return s


def md(text):
    out, lst = [], None
    for line in text.split('\n'):
        m = re.match(r'^(\d+)\. (.*)', line); b = re.match(r'^- (.*)', line)
        if m or b:
            kind = 'ol' if m else 'ul'
            if lst != kind:
                if lst: out.append('</%s>' % lst)
                out.append(('<ol start="%s">' % m.group(1)) if m else '<ul>'); lst = kind
            out.append('<li>%s</li>' % inline((m.group(2) if m else b.group(1))))
        else:
            if lst: out.append('</%s>' % lst); lst = None
            out.append(inline(line) + '<br>')
    if lst: out.append('</%s>' % lst)
    s = ''.join(out)
    return re.sub(r'(<br>)+$', '', s)


def table_rows(d):
    cols = sorted(d['cols'].items(), key=lambda kv: kv[1]['at'])
    rows = sorted(d['rows'].values(), key=lambda r: r['at'])
    return cols, rows


def bbox(i):
    d = E[i]
    if d['type'] == 'table':
        cols, rows = table_rows(d)
        w = sum(c['w'] for _, c in cols)
        h = 0
        for r in rows:
            h += max(max(1, -(-len(str(r.get(k, ''))) // max(1, int((c['w'] - 20) / 7.6)))) for k, c in cols) * 21 + 16
        return d['x'], d['y'], w, h
    if d['type'] == 'text':
        fs = SIZE.get(d.get('size', 'body'), 16)
        w = d.get('wrap') or len(d['text'].replace('**', '')) * fs * .52
        lines = max(1, -(-len(d['text']) * fs * .52 // w))
        return d['x'], d['y'], w, lines * fs * 1.4
    return d['x'], d['y'], d.get('w', 0), d.get('h', 0)


def side_pt(i, side):
    x, y, w, h = bbox(i)
    return {'left': (x, y + h / 2), 'right': (x + w, y + h / 2),
            'top': (x + w / 2, y), 'bottom': (x + w / 2, y + h)}[side]


def route(d):
    a, b = d['from'], d['to']
    ax, ay, aw, ah = bbox(a); bx, by, bw, bh = bbox(b)
    acx, acy, bcx, bcy = ax + aw / 2, ay + ah / 2, bx + bw / 2, by + bh / 2
    if d.get('bends'):
        bends = d['bends']
        if bends[0] == 'v' and len(bends) == 2:
            ly = acy + bends[1]
            p0 = (acx, ay + ah if ly > acy else ay)
            p3 = (bcx, by if ly < by else by + bh)
            return [p0, (acx, ly), (bcx, ly), p3]
    fs, ts = d.get('fromSide', 'right'), d.get('toSide', 'left')
    p0, p3 = side_pt(a, fs), side_pt(b, ts)
    if fs in ('left', 'right') and ts in ('left', 'right'):
        if abs(p0[1] - p3[1]) < 2: return [p0, p3]
        mx = (p0[0] + p3[0]) / 2
        return [p0, (mx, p0[1]), (mx, p3[1]), p3]
    if fs in ('top', 'bottom') and ts in ('top', 'bottom'):
        if abs(p0[0] - p3[0]) < 2: return [p0, p3]
        my = (p0[1] + p3[1]) / 2
        return [p0, (p0[0], my), (p3[0], my), p3]
    if fs in ('top', 'bottom'):
        return [p0, (p0[0], p3[1]), p3]
    return [p0, (p3[0], p0[1]), p3]


def el_html(i, ox, oy):
    d = E[i]; t = d['type']
    if t == 'container':
        return ('<div class="ctr" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"></div>'
                '<div class="ctrt" style="left:%dpx;top:%dpx">%s</div>' % (
                    d['x'] - ox, d['y'] - oy, d['w'], d['h'], d['x'] - ox, d['y'] - oy - 30, inline(d['text'])))
    if t == 'shape':
        fill = FILL.get(d.get('color', 'green'), d.get('color', '#d9efd3'))
        al = d.get('textAlign', 'center')
        cls = 'shape'
        style = 'left:%dpx;top:%dpx;width:%dpx;min-height:%dpx;text-align:%s;font-size:%dpx;' % (
            d['x'] - ox, d['y'] - oy, d['w'], d['h'], al, SIZE.get(d.get('size', 'body'), 16) - 1)
        if d.get('kind') == 'diamond':
            return ('<div class="shape dia" style="%sheight:%dpx"><div class="diabg" style="background:%s"></div>'
                    '<div class="diat">%s</div></div>' % (style, d['h'], fill, md(d['text'])))
        if d.get('kind') == 'rect': style += 'border-radius:4px;'
        border = 'border:1px solid #cfccc2;' if d.get('color') == 'white' else ''
        return '<div class="%s" style="%sbackground:%s;%s"><div>%s</div></div>' % (cls, style, fill, border, md(d['text']))
    if t == 'text':
        fs = SIZE.get(d.get('size', 'body'), 16)
        st = 'left:%dpx;top:%dpx;font-size:%dpx;color:%s;' % (d['x'] - ox, d['y'] - oy, fs, INK.get(d.get('color', 'ink'), '#1d1d1b'))
        st += ('width:%dpx;' % d['wrap']) if d.get('wrap') else 'white-space:nowrap;'
        if fs >= 28: st += 'font-weight:700;' if fs >= 48 else 'font-weight:500;'
        return '<div class="txt" style="%s">%s</div>' % (st, md(d['text']))
    if t == 'image':
        src = html.escape(d['src'])
        return '<a href="%s" target="_blank"><img class="img" src="%s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx" loading="lazy"></a>' % (
            src, src, d['x'] - ox, d['y'] - oy, d['w'], d['h'])
    if t == 'table':
        cols, rows = table_rows(d)
        h = ['<table class="tbl" style="left:%dpx;top:%dpx;width:%dpx"><colgroup>%s</colgroup>' % (
            d['x'] - ox, d['y'] - oy, sum(c['w'] for _, c in cols), ''.join('<col style="width:%dpx">' % c['w'] for _, c in cols))]
        for n, r in enumerate(rows):
            tag = 'th' if n == 0 else 'td'
            h.append('<tr>' + ''.join('<%s>%s</%s>' % (tag, inline(str(r.get(k, ''))), tag) for k, _ in cols) + '</tr>')
        return ''.join(h) + '</table>'
    return ''


def stage(ids, ox, oy, W, H, sid):
    parts = [el_html(i, ox, oy) for i in ids if E[i]['type'] != 'arrow']
    svg = ['<svg width="%d" height="%d"><defs><marker id="ah%s" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1d1d1b"/></marker></defs>' % (W, H, sid)]
    labels = []
    for i in ids:
        d = E[i]
        if d['type'] != 'arrow': continue
        pts = route(d)
        path = 'M' + ' L'.join('%.1f,%.1f' % (x - ox, y - oy) for x, y in pts)
        svg.append('<path d="%s" fill="none" stroke="#1d1d1b" stroke-width="2"%s marker-end="url(#ah%s)"/>' % (
            path, ' stroke-dasharray="7 6"' if d.get('dash') else '', sid))
        if d.get('label'):
            segs = list(zip(pts, pts[1:]))
            (x1, y1), (x2, y2) = max(segs, key=lambda s: abs(s[0][0] - s[1][0]) + abs(s[0][1] - s[1][1]))
            labels.append('<div class="alab" style="left:%dpx;top:%dpx">%s</div>' % ((x1 + x2) / 2 - ox, (y1 + y2) / 2 - oy, inline(d['label'])))
    svg.append('</svg>')
    return '<div class="stage" data-w="%d" data-h="%d" style="width:%dpx;height:%dpx">%s%s%s</div>' % (
        W, H, W, H, ''.join(parts), ''.join(svg), ''.join(labels))


def inside(i, c):
    d = E[i]
    if d['type'] == 'arrow':
        return inside(d['from'], c) and inside(d['to'], c)
    x, y, w, h = bbox(i)
    return c['x'] <= x + 1 and x < c['x'] + c['w'] and c['y'] <= y + 1 and y < c['y'] + c['h']


draw = [i for i in ORDER]
boxes = [i for i in draw if E[i]['type'] != 'arrow']
conts = [i for i in ORDER if E[i]['type'] == 'container']
FULLW = max(bbox(i)[0] + bbox(i)[2] for i in boxes) + 40
FULLH = max(bbox(i)[1] + bbox(i)[3] for i in boxes) + 40

tabs = [('board', 'Whole board', stage(draw, -20, -20, FULLW + 20, FULLH + 20, 'all'))]
# overview tab: title + section 0
for c in conts:
    cd = E[c]
    ids = [i for i in draw if i == c or (i not in conts and inside(i, cd))]
    if c == conts[0]:
        ids = ['e1', 'e2', 'e3'] + ids
        oy = -20
    else:
        oy = cd['y'] - 50
    name = cd.get('tab') or cd['text'].split(':')[0]
    tabs.append(('s' + c, name, stage(ids, cd['x'] - 20, oy, cd['w'] + 40, cd['y'] + cd['h'] + 20 - oy, c)))

title = D['meta']['title']
CSS = '''
:root{--bg:#f4f3ef}
html,body{margin:0;background:var(--bg);color:#1d1d1b;font-family:system-ui,-apple-system,"Segoe UI",sans-serif}
header{position:sticky;top:0;z-index:20;background:#fffffff2;border-bottom:1px solid #ddd;padding:10px 16px 0}
header h1{font-size:18px;margin:0 0 2px}header p{margin:0 0 8px;font-size:13px;color:#666}
nav{display:flex;flex-wrap:wrap;gap:4px}
nav button{border:1px solid #ccc;border-bottom:none;background:#efede6;padding:7px 12px;font-size:13px;border-radius:8px 8px 0 0;cursor:pointer}
nav button.on{background:#fff;font-weight:600;border-color:#999}
.tools{position:absolute;right:16px;top:12px;font-size:13px}.tools button{padding:3px 9px;border:1px solid #bbb;border-radius:6px;background:#fff;cursor:pointer}
.tab{display:none;padding:16px;overflow:auto}.tab.on{display:block}
.holder{position:relative;transform-origin:0 0}
.stage{position:relative;transform-origin:0 0}
.ctr{position:absolute;border:1.5px solid #cbc7bb;border-radius:16px;background:#fbfaf7}
.ctrt{position:absolute;font-size:17px;font-weight:600;white-space:nowrap}
.shape{position:absolute;box-sizing:border-box;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;justify-content:center;line-height:1.42}
.shape ol,.shape ul,.txt ol,.txt ul{margin:2px 0;padding-left:20px;text-align:left}
.dia{background:none!important;padding:0}.diabg{position:absolute;inset:0;clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%);border:none}
.dia::before{content:"";position:absolute;inset:0;clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%);background:#bdb9ad;transform:scale(1.012)}
.diabg{z-index:1}.diat{position:relative;z-index:2;padding:0 22%;text-align:center}
.txt{position:absolute;line-height:1.4}
.img{position:absolute;object-fit:cover;border-radius:6px;box-shadow:0 1px 3px #0003}
.tbl{position:absolute;border-collapse:collapse;background:#fff;font-size:14px;table-layout:fixed}
.tbl th,.tbl td{border:1px solid #d9d6cc;padding:6px 9px;text-align:left;vertical-align:top;line-height:1.35}.tbl th{background:#efede6}
.alab{position:absolute;transform:translate(-50%,-50%);background:var(--bg);padding:2px 8px;font-size:13px;white-space:nowrap;border-radius:6px;z-index:5}
svg{position:absolute;left:0;top:0;pointer-events:none;overflow:visible;z-index:4}
code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.92em;background:#0000000d;padding:0 3px;border-radius:3px}
a{color:#b4532a}
'''
JS = '''
var zoom={};
function cur(){return document.querySelector('.tab.on')}
function apply(t){var st=t.querySelector('.stage'),h=t.querySelector('.holder'),z=zoom[t.id];
 st.style.transform='scale('+z+')';h.style.width=(st.dataset.w*z)+'px';h.style.height=(st.dataset.h*z)+'px';
 document.getElementById('zl').textContent=Math.round(z*100)+'%';}
function fit(t){t=t||cur();zoom[t.id]=Math.min(1,(window.innerWidth-40)/t.querySelector('.stage').dataset.w);apply(t)}
function z(d){var t=cur();zoom[t.id]=Math.max(.15,Math.min(2,(zoom[t.id]||1)+d));apply(t)}
function show(id){document.querySelectorAll('.tab,nav button').forEach(function(e){e.classList.remove('on')});
 document.getElementById(id).classList.add('on');document.querySelector('[data-t="'+id+'"]').classList.add('on');
 var t=cur();if(zoom[t.id]===undefined)fit(t);else apply(t);if(history.replaceState)history.replaceState(null,'','#'+id)}
document.querySelectorAll('nav button').forEach(function(b){b.onclick=function(){show(b.dataset.t)}});
var h0=location.hash.slice(1);show(h0&&document.getElementById(h0)?h0:'START');
addEventListener('resize',function(){fit()});
'''
start = tabs[1][0]
page = ['<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
        '<title>%s</title><style>%s</style></head><body>' % (html.escape(title), CSS),
        '<header><h1>%s</h1><p>Study notes, one tab per section. All images are original illustrations made with fal; click one to open it full size. See README for sources, credits and license.</p>' % html.escape(title),
        '<div class="tools">zoom <button onclick="z(-.1)">−</button> <span id="zl"></span> <button onclick="z(.1)">+</button> <button onclick="fit()">Fit width</button> <button onclick="zoom[cur().id]=1;apply(cur())">100%</button></div>',
        '<nav>' + ''.join('<button data-t="%s">%s</button>' % (tid, html.escape(n)) for tid, n, _ in tabs) + '</nav></header>']
for tid, n, s in tabs:
    page.append('<section class="tab" id="%s"><div class="holder">%s</div></section>' % (tid, s))
page.append('<script>%s</script></body></html>' % JS.replace('START', start))
open('index.html', 'w').write(''.join(page))
print('tabs', [(t, n) for t, n, _ in tabs], 'size', len(''.join(page)))
