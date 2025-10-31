def p(g):
 c=[*{*sum(g,[])}-{0,2}][F:=0];n=range(10)
 for _ in[0]*4:
  g=[*map(list,zip(*g[::-1]))]
  if F:continue
  A,B=[max([*zip(*(o:={(i,j)for j in n for i in n if g[i][j]==C}))][1])for C in(2,c)]
  if(F:=A>B):
   for i,j in o:g[i][-j+2*B+1]=c
 return eval(str(g).replace(*'03'))