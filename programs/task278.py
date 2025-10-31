def p(g):
 n=enumerate;s,b=[{(i,j)for i,r in n(g)for j,e in n(r)if e==c}for c in(2,0)]
 for i,j in{(i+x,j+y)for x in(-1,0,1)for y in(-1,0,1)for i,j in{(i+x,j+y)for x,y in((1,0),(0,1),(-1,0),(0,-1))for i,j in s}&s}&b:g[i][j]=3
 return g