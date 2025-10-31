def p(g):
 s=sum(g,[]);a,b,*_=sorted({*s},key=s.count);W=len(g[0]);D=divmod(s.index(a),W);O={D};
 for _ in g*4:O|={(X,Y)for i,j in O for X,Y in((i,j+1),(i+1,j),(i-1,j),(i,j-1))if len(g)>X>-1<Y<W and g[X][Y]in(0,b)}
 for i,j in O:g[i][j]=[a,b][(sum(D)-i-j)%2]
 return g