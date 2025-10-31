def p(g):
 for j,e in enumerate(sum(g,[])):
  if e:J=j%9-1;g[I:=j//9][J:J+3]=1,0,1;g[I-1][J:J+3]=g[I+1][J:J+3]=5,1,5
 return g