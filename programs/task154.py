def p(g):
 for _ in[0]*2:
  g=[*map(list,zip(*g))];s=sum(g,[]);i=s.index(2)//15
  for a in(i-3,11-s[::-1].index(2)//15)[:2*({*g[i+2]}=={0})]:g[a:a+2],g[a+5:a+7]=g[a+6:a+4:-1],g[a:a+2][::-1]
 return g