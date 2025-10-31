def p(g):
 D=len(g[0]);l=range;n=enumerate;P=[[0]*D];g=[[0]+r+[0]for r in P+g+P];(a,*_,b),(c,*_,d)=map(sorted,zip(*{(i,j)for i,r in n(g)for j,e in n(r)if e%2}));R=[r[c:d+1]for r in g[a:b+1]];F=[lambda x:x[::-1],lambda x:[*zip(*x)],lambda x:[r[::-1]for r in x],list]
 for Z in l(16):
  X=F[Z//4](F[Z%4](R));Y=eval(str(X).replace(*'10'));w=len(X[0])
  for i in l(len(g)-len(X)+1):
   for j in l(D+3-w):
    if all(v==g[i+k][j+l]for k,r in n(Y)for l,v in n(r)):
     for k,r in n(X):g[i+k][j:j+w]=r
 return[r[1:-1]for r in g[1:-1]]