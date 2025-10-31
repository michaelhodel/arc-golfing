def p(g):
 def f(i,j):
  if i<n>j and g[i][j]<1:g[i][j]=1;f(i+1,j);f(i,j+1)
 for i in range(n:=len(g)):f(i,0);f(0,i)
 return[[3*(c<1)for c in r]for r in g]