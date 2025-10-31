def p(g):
 A=min(len(g),len(g[0]));p,c=[r[:A]for r in g[:A]],[r[-A:]for r in g[-A:]];X=range(A*A)
 if max(p[0]+p[1])>7:p,c=c,p
 return[[p[y//A][x//A]/8*c[y%A][x%A]for x in X]for y in X]