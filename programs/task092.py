def p(g):
 for _ in 0,0:
  for r in(g:=[*map(list,zip(*g))]):
   for v in r:r[:]=[[e,v*(v in r[j:])*(v in r[:j])][e<1]for j,e in enumerate(r)]
 return g