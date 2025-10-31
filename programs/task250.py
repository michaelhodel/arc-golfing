def p(g):
 n=enumerate;R,G=[{(i,j)for i,r in n(g)for j,e in n(r)if e==c}for c in(2,5)]
 for i,j in G:x,y=min(R,key=lambda X:(X[0]-i)**2+(X[1]-j)**2);g[i][j]=0;g[x-(x>i)+(x<i)][y-(y>j)+(y<j)]=5
 return g