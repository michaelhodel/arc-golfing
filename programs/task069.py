def p(g,E=enumerate):
 P=[[r,c,C]for r,R in E(g)for c,C in E(R)if C%8]
 for r,R in E(g):
  for c,C in E(R):
   if C==8:
    for a,b,d in P:q,v,w=P[0];g[r+a-q][c+b-v]=d;g[a][b]=0
 return g