def p(g):
 n=enumerate;Z=zip;s=sum(g,[]);b=max(s,key=s.count);C={*s}-{b};O=[{(i-(X:=[*map(min,Z(*o))])[0],j-X[1])for i,j in o}for o in[{(i,j)for i,r in n(g)for j,e in n(r)if e==c}for c in C]];A,B=Z(*[map(max,Z(*o))for o in O]);D=max(A+B)+1;G=[D*[b]for _ in[0]*D]
 for c,o,h,w in Z(C,O,A,B):
  for i,j in o:G[i+(D-h)//2][j+(D-w)//2]=c
 return G