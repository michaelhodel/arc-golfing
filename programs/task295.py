def p(g):
 for _ in[0]*(len(g[0])//2-1):g+=[g[-1][:1]+g[-1][:-1]]
 return g