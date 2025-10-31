def p(g):
 n=enumerate;x=range;B={(i,j)for i,r in n(g)for j,e in n(r)if e};I,J,_=max([(i,j,i+len(B&{(a+i,b+j)for a,b in B}))for i in x(4)for j in x(4)][1:],key=lambda x:x[2]);h=[10*[0]for _ in g[0]]
 for k in x(10):
  for i,j in B:
   if(a:=i+I*k)<10>(b:=j+J*k):h[a][b]=max(g[0])
 return h 