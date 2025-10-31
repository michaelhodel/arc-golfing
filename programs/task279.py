def p(g):
 h=len(g);w=len(g[0]);v=set()
 for I in range(h*w):
  if(g[i:=I//w][j:=I%w]<2)*(1-((i,j)in v)):
   s=[(i,j)];c=[];e=0;v|={(i,j)}
   while s:
    y,x=s.pop();c+=[(y,x)]
    for Y,X in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
     if h>Y>-1<X<w and g[Y][X]<2:
      e+=1
      if((Y,X)in v)-1:v|={(Y,X)};s+=[(Y,X)]
   for y,x in c:g[y][x]+=7*(e>=2*len(c))
 return g