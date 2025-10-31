def p(g,n=enumerate):
 for o in[{(i,j)}for i,r in n(g)for j,e in n(r)if e]:
  for _ in g:o|={(x,y)for X,Y in o for x,y in[(X-1,Y),(X+1,Y),(X,Y-1),(X,Y+1)]if len(g)>x>-1<y<len(g[0])and g[x][y]}
  for k,l in o:(i,*_,j),(x,*_,y)=map(sorted,zip(*o));g[k][l]=j-i+1+y-x==len(o)or(1>sum((i<a<j)*(x<b<y)for a,b in o)and 6)or 2
 return g