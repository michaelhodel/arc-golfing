def p(g):
 P=[[5]*len(g[0])]*2;g=[[5,5]+r+[5,5]for r in P+g+P];R=range;H=len(g);W=len(g[0])
 for h in R(3,H):
  for w in R(3,W):
   for i in R(1,H-h):
    for j in R(1,W-w):
     if all(b==sum([g[I][j+a:j+w-a]for I in R(i+a,i+h-a)],[]).count(5)for a,b in((0,h+h+w+w-4),(1,0)))*any(3>L.count(5)for L in[[g[x+I][y+J]for x,y in((0,1),(1,0),(-1,0),(0,-1))]for I,J in((i,j),(i+h-1,j),(i,j+w-1),(i+h-1,j+w-1))]):
      for I in R(i+1,i+h-1):g[I][j+1:j+w-1]=[4]*(w-2)
 return[r[2:-2]for r in g[2:-2]]