def p(g):
 for _ in[0]*13:
  for i,r in enumerate((g:=[*map(list,zip(*g[::-1]))])[:8]):r[i:17-i:2]=[r[i]|r[18-i]]+[r[i+2]|g[i+2][i]]*(8-i)
 return g