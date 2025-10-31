def p(g):
 A=sorted;n=enumerate;K=lambda P:[*map(min,zip(*P))];S=lambda P,d:A((i+d[0],j+d[1])for i,j in P)
 def H(o):
  for _ in g:o|={(x,y)for X,Y in o for(x,y)in[(X+x,Y+y)for x in(-1,0,1)for y in(-1,0,1)]if 15>x>-1<y<10 and g[x][y]}
  return frozenset(o)
 O=A({H({(i,j)})for i,r in n(g)for j,e in n(r)if e},key=K);R=K(O[0])[0];B=[*map(any,g[R+1:])].index(0)+R;E={e for P in O for e in P if K(P)[0]<=B};G=V=[];M=0;I,J=K(E)
 for P in O:
  T=K(P)[0];L=max([*zip(*P)][0])
  if T>B:
   if T>M+1:V and G.append(V);V=P;M=L
   else:V|=P;M=[M,L][L>M]
 for P in G+[V]:
  for(i,j)in max([{*S(S(A((i-I,j-J)for i,j in E),K(P)),d)}for d in[(0,2),(0,1),(0,0),(0,-1),(0,-2),(-1,0)]],key=lambda s:len(s&{*P})-K(s)[0]):
   if 15>i>-1<j<10:g[i][j]+=(g[i][j]<1)*(j>max([*zip(*P)][1]))
 return g