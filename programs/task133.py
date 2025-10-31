def p(g):
 W,E,*J=30,enumerate;C,*B={B*W+D:A for B,C in E(g)for D,A in E(C)if A},
 def F(z):
  if A:=C.pop(z,0):H[0][z]=A;H[1].add(A);[F(z+A%3-1+A//3*W-W)for A in range(9)]
 while C:B+=[H:=({},set())];F(min(C))
 for D,N in B+B:
  I,=B[0][1]&B[1][1];Z=min(O:=[A for A in D if D[A]==I]);A=int(len(O)**.5);L,=N-{I};J+=[B-Z for B in D if(D[B]==L)==A]
  for T in J:
   for M in range(A*A):Q=Z+T*A+M//A*W+M%A;g[Q//W][Q%W]=L
 return g