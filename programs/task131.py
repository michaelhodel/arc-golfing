def p(g):
 for _ in[0]*4:
  g=[*map(list,zip(*g[::-1]))];X=[*filter(max,g)]
  if(D:=len(g))*max(X[0])>42:I=g.index(X[-1]);h=[len(g[0])*[8]]+X+g[I+1:];g=(D-len(h))*[g[I+1]]+h
 return g