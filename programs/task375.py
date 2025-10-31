def p(g):
 for A,r in enumerate(g):r[A]=g[-A-1][A]=0
 return g