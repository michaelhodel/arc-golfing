def p(g):
 L=len;R=range;n=[];f=[divmod(sum(g,[]).index(1),L(g[0]))]
 for y,x in f:
  if L(g[0])>x>-1<y<L(g)and(y,x)not in n and g[y][x]:
   n+=(y,x),
   for i in-1,0,1:
    for j in-1,0,1:f+=(y+i,x+j),
 Y,X=zip(*n);o=[];H=[r[min(X):max(X)+1]for r in g[min(Y):max(Y)+1]]
 for _ in[0]*4:H=[*zip(*H)];o+=H,;H=H[::-1];o+=H,
 for y in R(L(g)):
  for x in R(L(g[0])):
   for c in o:
    V=R(L(c[0]));W=R(L(c))
    if all(i+y<L(g)and j+x<L(g[0])and(g[i+y][j+x]==(T:=c[i][j])or T%2)for i in W for j in V):
     for i in W:
      for j in V:g[i+y][j+x]=c[i][j]
 return g