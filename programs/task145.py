def p(g):
 h,w=len(g),len(g[0]);n=range;O=[{(i,j)}for i in n(h)for j in n(w)if g[i][j]<1]
 for _ in n(h+w):O=[o|{(x,y)for X,Y in o for x,y in[(X-1,Y),(X+1,Y),(X,Y-1),(X,Y+1)]if h>x>-1<y<w and g[x][y]<1}for o in O]
 a,*_,b=sorted(map(len,O))
 for o in O:
  for i,j in o:g[i][j]={a:8,b:1}.get(len(o),0)
 return g