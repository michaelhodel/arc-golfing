def p(g):
 for _ in[0]*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
   if(8 in r)*r[0]:r[r.index(8)]=r[0]
 return g