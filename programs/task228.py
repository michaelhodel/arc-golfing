def p(g,n=enumerate):
 for _ in[0]*4:g=[r for*r,in zip(*g[::-1])];(a,*_,b),(c,*_,d)=map(sorted,zip(*{(i+1,j+1)for i,r in n(g)for j,e in n(r)if(sum(g,[]).count(e)>1)*e}));g[b][d]=g[a][c];g[a][c]=0
 return g