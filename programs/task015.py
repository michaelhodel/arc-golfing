def p(g):
 for x in range(729):
  a=x%9//3-1;b=x%3-1;v=g[i:=x//81][j:=x%81//9]
  if a*a+b*b==v>0:g[i+a][j+b]=10-3*v
 return g