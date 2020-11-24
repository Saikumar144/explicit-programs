b=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
m,n=3,5
t,h=0,0
while t<m and h<n:
    for x in range(n):
        print(b[t][x])
    t=t+1
    for y in range(t,m):
        print(b[y][n-1])
    n=n-1
    if t<m:
        for x in range(n-1,h-1,-1):
            print(b[m-1][x])
        m=m-1
    if h<n:
        for y in range(m-1,t-1,-1):
            print(b[y][h-1])
        h=h+1
