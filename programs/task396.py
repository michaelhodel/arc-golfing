def p(g):
 G=g;H=len(g);W=len(g[0]);Z=range
 for X in Z(H*W):
  h=X//W+3;w=X%W+3
  for i in Z(H-h+1):
   for j in Z(W-w+1):S=[g[a][j:j+w]for a in Z(i,i+h)];U=sum(S,[]);G=[G,S][({U[0]}=={*S[0]}|{*S[-1]}|{*[*zip(*S)][0]})*(h*w-(Y:=U.count)(0)-Y(U[0])>0)]
 X=G[0][0];return eval(str(G).replace(*(f'{X}{max({*sum(G,[])}-{0,X})}')))