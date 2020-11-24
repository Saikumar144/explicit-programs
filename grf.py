w=[0,1,1,2,2,3]
#c=int(input())
p=max(w)+1

m=[]
f=[]
i=0
j=0
for x in range(p):
    m.append(w.count(x))
print(m)
for x in range(len(m)):
    if m[x]%2==1:
        i=x
        print(i,i+1)
        

    



