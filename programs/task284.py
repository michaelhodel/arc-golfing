def p(g):
 F=lambda x:[x,[*map(list,zip(*x))]][any(2<len({*r})for r in g)];h=F(g);n=enumerate;(x,y,a),(i,j,b)=[(i,j,e)for i,r in n(h)for j,e in n(r)if e];M=(i+x)//2
 for o,k,c in((-1,0,a),(2,1,b)):h[M+o][y-2:y+3]=[c]*5;h[M+k][y-2]=h[M+k][y+2]=c
 for k in range(x,i+1):h[k][y]=[b*(k>M+1),a][k<M]
 return F(h)