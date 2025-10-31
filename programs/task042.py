def p(g):
 for Z in range(162):
  if(g:=g[::-1])[i:=Z//18][j:=Z//2%9]==3==g[i-1][j+1]!=g[i][j+1]:
   k=j+1
   while g[i-1][k]:k+=1;N=k-j-1
   for X in range(N*N):
    for(a,b)in(i+N+X//N,j+X%N+N+1),(i-N-X//N-1,j-X%N-N):
     if(0<=a<10>b>=0):g[a][b]=8
 return g