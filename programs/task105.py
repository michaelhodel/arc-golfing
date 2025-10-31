def p(g,n=enumerate):
 for _ in[B:={(i,j)for i,r in n(g)for j,e in n(r)if e}]*2:
  g=[*map(list,zip(*g))];B={(j,i)for i,j in B};(i,*_,j),(x,*_,y)=map(sorted,zip(*B));g[i][x:y+1]=g[j][x:y+1]=(S:=[2]*(y-x+1))
  for r in g[i+1:j]:
   if r[x+1:y].count(1)>1:r[x+1:y]=S[2:]
 for i,j in B:g[i][j]=1
 return g