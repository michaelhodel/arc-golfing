def p(g,n=range):
 i=len(g);a=lambda g:[*map(list,zip(*g[::-1]))]
 for k in n(4):
  h=[(t,z)for t in n(i)for z in n(i)if g[t][z]];(z,*_,G),(f,*_,e)=map(sorted,zip(*h));t=g[z][f];d=g[z].count(t)
  if d<g[G].count(t):
   h,m=f+d//2,e-d//2
   for t in n(G):g[t][h:m+1]=[4]*(m-h+1)
   for t in n(z+1,G):g[t][f+1:e]=[4]*(e-f-1)
   for u in n(z+1):
    t=z-u;g[t][h-u]|=4*(h>=u)
    if m+u<i:g[t][m+u]=4
   for t in n(4-k):g=a(g)
   return g
  g=a(g)