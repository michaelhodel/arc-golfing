def p(g,R=enumerate):
 for _,_ in R([0]*4):
  for i,r in R(g:=[*map(list,zip(*g[::-1]))]):
   for j,e in R(r):
    if[2,0]==r[j:j+2]:
     for a in range(1,(r[j-1::-1]+[0]).index(0)+1):g[i-a][j:]=g[i+a][j:]=[3]*(X:=len(r[j:]));r[j:]=[2]*X
 return g