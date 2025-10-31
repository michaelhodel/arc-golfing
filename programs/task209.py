def p(g):
 R=range;n=enumerate;X=lambda G,S:{(i,j,e)for i,r in n(G)for j,e in n(r)if e in S};(a,*_,b),(c,*_,d),_=map(sorted,zip(*X(g,{4})));G=[r[c:d+1]for r in g[a:b+1]]
 for x in R(a,b+1):g[x][c:d+1]=[0]*(d-c+1);O=X(g,{*R(1,9)});M,N,_=map(min,zip(*O))
 for F in 2,3,4:
  for T in R(900):
   if X(G,{*R(9)}-{0,4})-(U:={((i-M)*F+x+T//30,(j-N)*F+y+T%30,c)for i,j,c in O for x in R(F)for y in R(F)})==O-O:
    for x,y,c in U:G[x][y]=c
    return G