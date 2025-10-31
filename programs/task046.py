def p(g):
 l=enumerate;t=[-1]+[t for(t,a)in l(zip(*g))if 1-any(a)]+[len(g[0])];a=[[n[X+1:t[a+1]]for n in g]for a,X in l(t[:-1])if X+1<t[a+1]];n=a[:1]
 for u in a[1:]:t=n[-1];r,t=[[a for(a,t)in l(X)if(t)*(t[-I]==5)][0] for I,X in l((u,t))];r=t-r;t=[[0]*len(u[0])]*3;n+=[(t+u+t)[3-r:6-r]]
 return[sum(t,[])for t in zip(*[[[[t,a][t==5]for t in t]for t in t]for(t,a)in zip(n,[[t for a in t for t in a if t%5][0]for t in a])])]