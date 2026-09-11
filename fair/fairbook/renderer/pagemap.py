import re, json, io, sys, warnings
warnings.filterwarnings('ignore')
import pypdf
pdf=sys.argv[1]
r=pypdf.PdfReader(pdf)
flat=[]
def walk(o):
    for x in o:
        if isinstance(x,list): walk(x)
        else:
            try: flat.append((str(x.title).strip(), r.get_destination_page_number(x)+1))
            except Exception: pass
walk(r.outline)

bk=io.open('draft.v14.md',encoding='utf-8').read()
toc=[];cur=None
for l in bk.split('\n'):
    m=re.match(r'^## (CC (\d+)) — (.+)$', l)
    if m: cur=1; toc.append(('ch'+m.group(2), f'{m.group(1)} — {m.group(3)}')); continue
    m=re.match(r'^### (CC [\d.]+) — (.+)$', l)
    if m and cur: toc.append(('sc'+re.sub(r'[^0-9]','_',m.group(1)), f'{m.group(1)} — {m.group(2)}')); continue
    m=re.match(r'^### ([A-Z].+)$', l)
    if m and cur:
        s=re.sub(r'[^a-z0-9]+','_',m.group(1).lower()).strip('_')[:38]
        toc.append(('sx'+s, m.group(1)))

norm=lambda t: re.sub(r'\s+',' ',t).strip()
pm={}; used=set()
for anchor,label in toc:
    for i,(t,p) in enumerate(flat):
        if i in used: continue
        if norm(t)==norm(label):
            pm[anchor]=str(p); used.add(i); break
print('outline entries:',len(flat))
print('mapped', len(pm), 'of', len(toc))
miss=[(a,l) for a,l in toc if a not in pm]
if miss:
    print('UNMAPPED:')
    for a,l in miss: print('   ',a,'|',l)
json.dump(pm, open('pagemap.json','w'))
