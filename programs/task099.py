def p(g):
 for c in{*(s:=sum(g,[]))}-{1}:
  R=[-2,-1,0,1];a,b=divmod(s.index(c),10)
  for i in[*R,-2-g[a-2][b-1]]:
   for j in[*R,2]:g[a+i][b+j]+=c*(g[a+i][b+j]<1)
 return g