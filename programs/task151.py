def p(g):
 E,k=[[*map(all,c)].index(1)for c in(g,zip(*g))]
 for o in(-1,0,1):g[E+o][k-1:k+2]=4,[4,g[E][k]][o==0],4
 return g