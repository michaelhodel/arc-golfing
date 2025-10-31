def p(g,p=1,d=range,o=len):
 for t in d(4):
  g=[*map(list,zip(*g[::-1]))];f,i=o(g),o(g[0])
  if p:
   for t in d(f):
    if(g[t][0]>7)*(2 in g[0]+g[-1]):
     p=0
     for e in d(i):
      if 0<=t+(p:=p+(g[0][e]==2)-(g[-1][e]==2))<f:g[t+p][e]=8
     p=0
 return g