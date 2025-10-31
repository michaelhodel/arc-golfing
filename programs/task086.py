def p(g):
 n=enumerate;L=zip;_,b,a=[*{}.fromkeys(sum(g,[]))]
 def f(h):
  h=[*map(list,h)];O={(i,j)for i,r in n(h)for j,e in n(r)if(e==b)*(h[i-1][j]+h[i][j-1]<1)};T={(i,j)for i,j in O if h[i][j+3]<1}
  for k,S in(3,T),(4,O-T):
   for l in[0,1][:k-2]:
    for i,j in S:h[i-1-l][j:j+k]=h[i+k+l][j:j+k]=[a]*k
  return h
 return[[{b:a,a:b,0:0}[c|d]for c,d in L(*Z)]for Z in L(f(g),L(*f(L(*g))))]