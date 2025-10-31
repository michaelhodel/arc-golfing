def p(g):
 def F(c):I,J=map(sorted,zip(*f(c)));return max(I[-1]-I[0],J[-1]-J[0])
 D=[2>len({*r})for r in g].index(1)+1;G=[r[::D]for r in g[::D]];d=len(G);n=enumerate;f=lambda c:{(i,j)for i,r in n(G)for j,e in n(r)if e==c};Z=f(max({*sum(G,[])}-{0},key=F))
 for i,j in Z:
  for x in-1,0,1:
   for y in-1,0,1:
    if d>(A:=x+i)>-1<(C:=y+j)<d:G[A][C]=max(G[a+x][b+y]for a,b in Z if d>a+x>-1<b+y<d)
 return[[[T:=g[0][D-1],G[i//D][j//D]][e!=T]for j,e in n(r)]for i,r in n(g)]