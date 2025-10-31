def p(g,l=range(6)):
 for _ in[0]*4:g=[*zip(*g[::-1])];g=g[0][2]==8==g[2][0]and[[g[i//3][j//3]/3*g[i+3][j+3]for j in l]for i in l]or g
 return g