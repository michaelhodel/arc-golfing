def p(g,p=enumerate,e=range):
 t={(n,a)for(n,t)in p(g)for(a,l)in p(t)if l}
 while t:
  a={n:[]for n in t}
  for l in e(3):
   for h in e(11):
    for f in e(11):
     if(n:={(h+[n//2,n,0][l],f+[n%2,0,n][l])for n in e((4,3,3)[l])})<=t:[a[t].append(n)for t in n]
  f=min(t,key=lambda n:len(a[n]));n=a[f][0];t-=n
  for(a,l)in n:g[a][l]=(len(n)-3)*6+2
 return g