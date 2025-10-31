def p(g):
 s=sum(g,[]);n=enumerate;b=max(s,key=s.count);a=min(s,key=lambda v:f"{b}, {v}, {b}"in str(g+[*zip(*g)]));o=[[[b,a][v==a]for v in r[::2]]for r in g[::2]];m=[r*2 for r in g*2]
 for i,r in n(m):
  for j,_ in n(r):
   for k in{*s}:
    if[[[b,a][v==k]for v in r[j:j+len(o[0])]]for r in m[i:i+len(o)]]==o:s=g;return[(s:=[[[b,k][v==k]for v in i]for i in zip(*s)if k in i])for _ in'  '][1]