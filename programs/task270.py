def p(g):
 for _ in[0]*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
   for e in r:
    if(k:={1:7,2:3}.get(e,9))in r[:(j:=r.index(e))]:r[r[:j].index(k)]=0;r[j-1]=k
 return g