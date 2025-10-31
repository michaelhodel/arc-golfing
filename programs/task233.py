def p(g):
 T=tuple;R=range;i=R(9);c={};f=lambda a:[a(p,s,[g[p+a//3][s+a%3]for a in i])for p in R(len(g)-2)for s in R(len(g[0])-2)]
 def p(p,s,n):
  if(len(r:={*n})>1)*(r&{0,2}=={2}):
   n=T(a==2 for a in n);k={n:sum(r)-2}
   for a in R(4):c[n]=k;n=T(n[a%3*3+2-a//3]for a in i)
   for a in i:g[p+a//3][s+a%3]=0
 O=lambda x:[*map(list,zip(*filter(any,x)))];f(p);g=O(O(g));[f(lambda p,s,n:(t:=c.get(n:=T(a<1 for a in n)))and(a or n in t)and(r:=t.popitem()[1],[g[p+a//3].__setitem__(s+a%3,(r,2)[n[a]])for a in i]))for a in R(2)];return g