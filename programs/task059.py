def p(g):
 X=0,1,2;c=max({*sum(g,[])}-{5});S={(i*4,j*4,a)for i in X for j in X for a in X};M={(i,j):sum(sum([g[i+A][j:j+3]for A in X],[]))/c for i,j,a in S}
 for i,j,a in S:g[i+a][j:j+3]=3*[c*(M[(i,j)]==max(M.values()))]
 return g