def p(g):
 t=lambda M:M(s:=sum(g,[]),key=s.count)
 for L in 0,0,1,1:g=[r for*r,in zip(*g)if[4,len(g)*.6][L]<r.count(t(max))]
 c=t(min);n=enumerate;I,J=zip(*[(i,j)for i,r in n(g)for j,e in n(r)if e==c]);return[[[e,c][i in I or j in J]for j,e in n(r)]for i,r in n(g)]