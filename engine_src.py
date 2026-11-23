import json,os,urllib.request as q
U=os.environ.get("MAKEFUN_ENV_URL")
def post(p,b):return json.load(q.urlopen(q.Request(U+p,json.dumps(b).encode())))
V={"P":100,"N":320,"B":330,"R":500,"Q":900,"K":20000}
WN=(-21,-19,-12,-8,8,12,19,21);WK=(-11,-10,-9,-1,1,9,10,11);WD=(-11,-9,9,11);WR=(-10,-1,1,10)
F="abcdefgh"
T={}
T["P"]="0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,50,10,10,20,30,30,20,10,10,5,5,10,25,25,10,5,5,0,0,0,20,20,0,0,0,5,-5,-10,0,0,-10,-5,5,5,10,10,-20,-20,10,10,5,0,0,0,0,0,0,0,0"
T["N"]="-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,0,15,20,20,15,0,-30,-30,5,10,15,15,10,5,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50"
T["B"]="-20,-10,-10,-10,-10,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-20,-10,-10,-10,-10,-10,-10,-20"
T["R"]="0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,0,0,0,5,5,0,0,0"
T["Q"]="-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,5,5,5,0,-10,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,-5,-10,5,5,5,5,5,0,-10,-10,0,5,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20"
T["K"]="-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20,20,0,0,0,0,20,20,20,30,10,0,0,10,30,20"
PST={k:[int(x) for x in v.split(",")]for k,v in T.items()}
class Bd:
 def __init__(s,f):
  s.b=["?"]*120
  for r in range(2,10):s.b[10*r+1:10*r+9]=["."]*8
  p=f.split();r=x=0
  for c in p[0]:
   if c=="/":r+=1;x=0
   elif c.isdigit():x+=int(c)
   else:s.b[21+x+10*r]=c;x+=1
  s.w=p[1]=="w";s.cr=p[2]
 def kq(s,w):return s.b.index("K"if w else"k")
 def atk(s,q,by):
  b=s.b
  for D,T2 in((WR,"RQ"),(WD,"BQ")):
   for d in D:
    i=q+d
    while b[i]==".":i+=d
    if b[i].isupper()==by and b[i].upper()in T2:return 1
  for D,T2 in((WN,"N"),(WK,"K")):
   for d in D:
    if b[q+d].isupper()==by and b[q+d].upper()in T2:return 1
  for d in((9,11)if by else(-11,-9)):
   if b[q+d].isupper()==by and b[q+d].upper()=="P":return 1
  return 0
 def mv(s):
  b=s.b;w=s.w;ms=[]
  for q in range(21,99):
   p=b[q]
   if p=="."or p=="?"or p.isupper()!=w:continue
   t=p.upper()
   if t=="P":
    d=-10 if w else 10;r=q//10-2
    pr=r==(1 if w else 6)
    if b[q+d]==".":
     if pr:
      for c in("QRBN"if w else"qrbn"):ms.append((q,q+d,c))
     else:
      ms.append((q,q+d))
      if r==(6 if w else 1)and b[q+2*d]==".":ms.append((q,q+2*d))
    for dd in(d-1,d+1):
     t2=b[q+dd]
     if t2 not in".?"and t2.isupper()!=w:
      if pr:
       for c in("QRBN"if w else"qrbn"):ms.append((q,q+dd,c))
      else:ms.append((q,q+dd))
   elif t=="N"or t=="K":
    for d in(WN if t=="N"else WK):
     t2=b[q+d]
     if t2=="."or(t2!="?"and t2.isupper()!=w):ms.append((q,q+d))
    if t=="K":
     o=70 if w else 0
     if s.cr.count("K"if w else"k")and b[28+o].upper()=="R"and b[26+o]==b[27+o]=="."and not s.atk(25+o,not w)and not s.atk(26+o,not w)and not s.atk(27+o,not w):ms.append((q,27+o))
     if s.cr.count("Q"if w else"q")and b[21+o].upper()=="R"and b[22+o]==b[23+o]==b[24+o]=="."and not s.atk(25+o,not w)and not s.atk(24+o,not w)and not s.atk(23+o,not w):ms.append((q,23+o))
   else:
    for d in(WR+WD if t=="Q"else(WR if t=="R"else WD)):
     i=q+d
     while b[i]==".":ms.append((q,i));i+=d
     if b[i]!="?"and b[i].isupper()!=w:ms.append((q,i))
  return ms
 def mk(s,m):
  a,b2=m[0],m[1];b=s.b;cap=b[b2];pb=b[a]
  b[b2]=m[2]if len(m)==3 else pb;b[a]="."
  if pb in"Pp"and cap=="."and a%10!=b2%10:b[b2+(10 if s.w else-10)]="."
  if pb in"Kk"and abs(a-b2)==2:
   o=a-25
   if b2>a:b[26+o]=b[28+o];b[28+o]="."
   else:b[24+o]=b[21+o];b[21+o]="."
  s.w=not s.w
  return cap
 def un(s,m,cap):
  a,b2=m[0],m[1];b=s.b
  s.w=not s.w
  pb=b[b2]
  if len(m)==3:pb="P"if s.w else"p"
  b[a]=pb;b[b2]=cap
  if pb in"Pp"and cap=="."and a%10!=b2%10:b[b2+(10 if s.w else-10)]="p"if s.w else"P"
  if pb in"Kk"and abs(a-b2)==2:
   o=a-25
   if b2>a:b[28+o]=b[26+o];b[26+o]="."
   else:b[21+o]=b[24+o];b[24+o]="."
 def ev(s):
  sc=0
  for q in range(21,99):
   p=s.b[q]
   if p in".?":continue
   t=p.upper();r=q//10-2;x=q%10-1
   i=(r*8+x)if p.isupper()else((7-r)*8+x)
   v=V[t]+PST[t][i]
   sc+=v if p.isupper()else-v
  return sc if s.w else-sc
K1=[None]*24;K2=[None]*24;H={}
def ab(d,al,be,bd,chk):
 global nodes,AB
 nodes+=1
 if nodes>BUD:AB=1
 if AB:return bd.ev()
 inchk=bd.atk(bd.kq(bd.w),not bd.w)
 if inchk and not chk and d<18:d+=1
 if d==0:
  e=bd.ev()
  if e>=be:return e
  if e>al:al=e
  qonly=1
 else:qonly=0
 dd=d%24;k1=K1[dd]if d<24 else None;k2=K2[dd]if d<24 else None
 ms=bd.mv()
 def sc(m):
  t=bd.b[m[1]]
  v=V.get(t.upper(),0)*16-V.get(bd.b[m[0]].upper(),0)if t!="."else 0
  if m==k1:v+=900
  elif m==k2:v+=800
  else:v+=H.get(m,0)
  return v
 ms.sort(key=sc,reverse=True)
 best=e if d==0 else-999999
 for m in ms:
  cap=bd.b[m[1]]
  if qonly and cap=="."and len(m)<3:continue
  cap=bd.mk(m)
  if bd.atk(bd.kq(not bd.w),bd.w):bd.un(m,cap);continue
  v=-ab(d-1 if d else 0,-be,-al,bd,inchk)
  bd.un(m,cap)
  if AB:return best if best>-999999 else bd.ev()
  if v>best:
   best=v
   if v>al:
    al=v
    if al>=be:
     if cap==".":H[m]=H.get(m,0)+d*d
     if 0<d<24:K2[d]=K1[d];K1[d]=m
     break
 return best
# Node budget instead of wall-clock time: the competition requires the search
# to be deterministic (a replay must be byte-identical), so the per-move limit
# is a node count, not a timer.
BUD=70000;nodes=0;AB=0;CUR=set();CURG=0
def choose(fen,legal):
 global nodes,AB
 bd=Bd(fen);S=lambda u:F.index(u[0])+21+(8-int(u[1]))*10
 ms=[[S(u[0:2]),S(u[2:4])]+([u[4].upper()]if len(u)==5 else[])for u in legal]
 best=ms[0]
 for d in range(1,24):
  nodes=0;AB=0;al=-999999;bs=None
  order=[best]+[m for m in ms if m!=best]
  for m in order:
   cap=bd.mk(m)
   rep=("".join(bd.b)+str(bd.w))in CUR
   v=-ab(d-1,-999999,-al,bd,0)
   bd.un(m,cap)
   if AB:break
   if rep:v-=40
   if v>al:al=v;bs=m
  if AB:break
  best=bs or best
  if al>90000:break
  K1=[None]*24;K2=[None]*24
 a,b2=best[0],best[1]
 return F[a%10-1]+str(10-a//10)+F[b2%10-1]+str(10-b2//10)+(best[2].lower()if len(best)==3 else"")
while 1:
 g=post("/game",{})
 if g["status"]=="done":break
 if g["game"]!=CURG:CURG=g["game"];CUR={g["fen"]}
 CUR.add(g["fen"])
 while g["status"]=="your_move":
  g=post("/move",{"game":g["game"],"move":choose(g["fen"],g["legal_moves"])})
  CUR.add(g["fen"])
