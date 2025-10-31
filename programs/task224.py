def p(g):
 n=enumerate;c=max({*sum(g,[])}-{5});(i,*_,j),(x,*_,y)=map(sorted,zip(*{(i,j)for i,r in n(g)for j,e in n(r)if e==5}));g[i+1][x+1:y]=g[j-1][x+1:y]=[c]*(y-x-1)
 for r in g[i+1:j]:r[x+1]=r[y-1]=c
 return g