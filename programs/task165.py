def p(g):
 n=enumerate;C=sum(g,[]);A=[*filter(int,C)][-1];D={*C}-{0,A}
 for(E,B)in n(zip(*g)):
  if D&{*B}and A in B[(G:=19-B[::-1].index(*D))+1:]:
   for F,r in n(g[G:20]):r[E]=r[E]or A
 return g