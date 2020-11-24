from itertools import permutations
import time
n=8
sol=0
r=range(n)
for com in permutations(r):
    if n==len(set(com[i]+i for i in r))==len(set(com[i]-i for i in r)):
        sol+=1
        print('sol'+str(sol)+';'+str(com)+'\n')
    
