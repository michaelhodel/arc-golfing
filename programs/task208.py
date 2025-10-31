def p(g):
 R=range;s=sum(g,[]);c=min(s,key=s.count);(i,j),(x,y)=[divmod(x.index(c),21)for x in(s,s[::-1])];m=20-x-i;n=20-y-j
 for a in R(21-m):
  for b in R(21-n):
   if all(1>sum(g[l][b+1:(X:=b+n)])for l in R(a+1,a+m)):
    for I in R(a,a+m+1):g[a][b:X]=g[a+m][b:X]=[c]*n;g[I][b]=g[I][X]=c
 return g