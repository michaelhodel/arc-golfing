def p(g):
 I=[x>0 for x in sum(g,[])].index(1);i,j=I//6+.5,I%6+.5;R=(-1,-1),(1,1),(-1,1),(1,-1);C=int
 for x,y in R:
  for X,Y in R:
   if 6>(a:=C(i-(X/2+2)*x))>-1<(b:=C(j-(Y/2+2)*y))<6:g[a][b]=g[C(i+x/2)][C(j+y/2)]
 return g