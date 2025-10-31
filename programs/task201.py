def p(g):
 s=sum(g,[]);u=lambda S:divmod(S.index(4),13);i,j=u(s);x,y=u(s[::-1]);x=13-x;y=13-y;A,B,*_=g[i+1][j::y-j-1]
 for a in range(i,x):g[a][j:y]=[0]*(y-j)
 for _ in 1,1:g=[*filter(max,zip(*g))]
 N=y-j-2;P=[[4,*[0]*N,4]];return P+[[A,*r[::1-2*(max(max(r[:N//2])for r in g)==B)],B]for r in g]+P