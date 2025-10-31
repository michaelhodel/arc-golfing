def p(g):
 u=range;E=len({*sum(g,[])})-1;A=5*E;g=[[g[W//E][l//E]for l in u(A)]for W in u(A)]
 for k in u(A,0,-1):
  for X in u((Y:=A-k+1)*Y):
   if(J:=g[W:=X//Y][l:=X%Y])*all(r[l:l+k]==k*[J]for r in g[W:W+k]):
    for a,C in(-1,-1),(-1,k),(k,-1),(k,k):
     e=W+a;K=l+C
     while(A>e>-1<K<A)*(1>g[e][K]):g[e][K]=2;e+=a>0 or-1;K+=C>0 or-1
    return g