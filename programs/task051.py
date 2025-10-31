def p(g):
 s=sum(g,[]);F=s.count;a,b,_=sorted({*s},key=F)
 for _ in[0]*4:
  w=len(g);g=[r for*r,in zip(*g[::-1])];s=sum(g,[]);G=s.index;A=G(a)
  if(X:=A//w)==G(b)//w:
   for x in range(X+F(b)//4+1,len(g)):g[x][A%w]=a
 return g