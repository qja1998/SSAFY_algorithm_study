N=int(input())
L1=list(map(int,input().split()))
L1.sort()
time=0
for i in range(N):
    for n in range(i+1):
        time+=L1[n]
print(time)