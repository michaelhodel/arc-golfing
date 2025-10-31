def p(g,R=range(18)):
 P=[i for i in R if{*g[i]}-{0,1}==set()][1]
 for _ in R:g=[[max(g[j][i%P::P])for j in R]for i in R]
 return g