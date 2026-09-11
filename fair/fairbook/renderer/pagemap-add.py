import re, json, io, sys, warnings
warnings.filterwarnings('ignore'); import pypdf
r=pypdf.PdfReader(sys.argv[1]); flat=[]
def walk(o):
    for x in o:
        if isinstance(x,list): walk(x)
        else:
            try: flat.append((str(x.title).strip(), r.get_destination_page_number(x)+1))
            except Exception: pass
walk(r.outline)
md=io.open('addendum.v14.md',encoding='utf-8').read()
toc=[];cur=None
for l in md.split('\n'):
    m=re.match(r'^## (§(\d+)) — (.+)$', l)
    if m: cur=1; toc.append(('a'+m.group(2), f'{m.group(1)} — {m.group(3)}')); continue
    m=re.match(r'^### (§[\d.]+) — (.+)$', l)
    if m and cur: toc.append(('as'+re.sub(r'[^0-9]','_',m.group(1)), f'{m.group(1)} — {m.group(2)}')); continue
norm=lambda t: re.sub(r'\s+',' ',t).strip()
pm={};used=set()
for a,label in toc:
    for i,(t,p) in enumerate(flat):
        if i in used: continue
        if norm(t)==norm(label): pm[a]=str(p); used.add(i); break
print('outline entries:',len(flat)); print('mapped',len(pm),'of',len(toc))
miss=[x for x in toc if x[0] not in pm]
if miss: print('UNMAPPED:',miss)
json.dump(pm,open('pagemap-add.json','w'))
