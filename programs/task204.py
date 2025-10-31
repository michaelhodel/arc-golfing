def p(g,r=range):
 for h in(T:=r(3,11)):
  for w in T:
   for x in r((X:=len(g)+1)-h):
    for y in r(X-w):
     if all(g[x][y:y+w]+[*[*zip(*g)][y][x:x+h]]):
      for i in r(x+1,x+h-1):g[i][y+1:y+w-1]=[2+h%2*5]*(w-2)
 return g