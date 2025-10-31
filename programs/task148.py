def p(g):
 n=enumerate;a,*m,b=[i for i,r in n(g)if 2 in r];d=(len(m)+2)//2;b=b-d+1
 for i,r in n(g[a:a+d]):
  if(X:=8 in r):A,B=sorted(map(r.index,(2,8)));g[a+i]=[[[e,4][e>5],8][A<X<B]for X,e in n(r)]
  g[b+i]=[[e,8][(e<1)*X]for e in g[b+i]]
 return g