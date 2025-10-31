def p(g):
 w=len(g[0]);f=sum(g,[]);d,e,b,c=sorted({*f},key=f.count);i=f.index(d);o=[f[Y+X]for Y,X in[(i,1),(i,-1),(i+w,0),(i-w,0)]if w>i%w+X>-1<Y<w*len(g)].count
 for p,v in[*enumerate(f)]:
  for Y,X in(w,1),(w,-1),(-w,-1),(-w,1):
   i=p;x=p%w
   while v in[d,e]and w>x>-1<i<w*len(g):
    for(A,B,C)in(b,e,d),(c,d,e):
     if f[i]==A:f[i]=[B,C][o(b)>o(c)]
    i+=Y+X;x+=X
 return[*zip(*w*[iter(f)])]