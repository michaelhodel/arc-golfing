def p(g):
 for I in range(100):
  if g[i:=I//10][j:=I%10]:
   o={(i,j)}
   for _ in g:o|={(x,y)for X,Y in o for x,y in[(X-1,Y),(X+1,Y),(X,Y-1),(X,Y+1)]if(10>x>-1<y<10)and g[x][y]}
   for a,b in o:g[a][b]=5-len(o)
 return g