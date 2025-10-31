def p(g):
 T=[*{}.fromkeys(sum(g,[]))];N=enumerate;_,S,X=[{(i,j)for i,r in N(g)for j,e in N(r)if e==c}for c in T]
 for i,j in X:g[i][j]=T[1]*((i,15-j+max(range(-8,8),key=lambda x:{(i,15-j+x)for i,j in S}-(S|X)==S-S))in S)
 return g