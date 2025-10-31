def p(g):
 i,j=divmod(sum(g,[]).index(5),len(g[0]));g[i][j]=0;x,y=[[{*r}!={0}for r in x].index(1)for x in(g,zip(*g))]
 for X in range(9):a=X//3;b=X%3;g[i+a-1][j+b-1]=g[x+a][y+b]
 return g