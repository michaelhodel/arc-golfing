def p(g):
 s=[*map(list,g)];D=-1,0,1;E=[(i,j)for i in D for j in D if i|j]
 for A in range((len(g)-1)*(X:=len(g[0])-1)):
  a=A//X;b=A%X
  for t in(0,1,2,3)[:(len(set(V:=g[a][b:b+2]+g[a+1][b:b+2]))>3)*4]:
   x=a+(t>1);y=b+(t&1);K=x>a;L=y>b;A=a+a+1;B=b+b+1;q=[(x,y)];g[x][y]=0
   if(k:=V[t])*any(k==g[x+i][y+j]for i,j in E):
    while q:
     x,y=q.pop()
     for t in 0,1,2,3:s[(x,A-x)[(t>>1)!=K]][(y,B-y)[(t&1)!=L]]=V[t]
     for i,j in E:
      u=x+i;v=y+j
      try:
       if g[u][v]==k:g[u][v]=0;q+=[(u,v)]
      except:0
    break
 return s