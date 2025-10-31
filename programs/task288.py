def p(g):
 d=len(g)//2;c=g[-1][d];k=g[-1].count(c)//2
 for i in range(d-k):r=g[-3-i];r[d-k-i-1]=r[d+k+i+1]=c
 return g