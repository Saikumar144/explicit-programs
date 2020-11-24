v=int(input())
b=[11,9,7,5,3,1]
d=v//6
r=v%6
if r>0 and d%2==1:
    print((v-b[-r]))
elif r>0 and d%2==0:
    print(v+b[r-1])
if r==0 and d%2==1:
    print(v+1)
elif r==0 and d%2==0:
    print(v-11)
