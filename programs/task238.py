def p(g):
 T=lambda x,s:[r for*r,in zip(*x)if{*r}&s];B,O=[T(T(g,s),s)for s in({8},{*range(10)}-{8,0})];D=len(B)
 for X in range(D*D):i=X//D;j=X%D;x=i>j;y=i<j;v=i+j<D-1;w=i+j>D-1;O[i+1][j+1]=[O[1][0],O[-1][1],O[0][1],O[1][-1],8][[x*v,x*w,y*v,y*w,1].index(1)]*B[i][j]/8
 return O