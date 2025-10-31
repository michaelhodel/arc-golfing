def p(g,E=enumerate):
 e={r[0]:y for y,r in E(g)if all(r)}
 if not e:return[*zip(*p([*map(list,zip(*g))]))]
 for y,r in E(g):
  for x,v in E(r):
   g[y][x]=0
   if v in e:g[(Y:=e[v])-(y<Y)+(y>Y)][x]=v
 return g