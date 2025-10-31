def p(g):
 T=tuple;D={}
 for X in range(144):o=T(T(g[X//12+x][(j:=X%12):j+3])for x in(0,1,2));D[o]=(1+D.get(o,0))*all(map(max,o))
 return max(D,key=lambda x:(D[x]==max(D.values()))/sum(x,T()).count(0))