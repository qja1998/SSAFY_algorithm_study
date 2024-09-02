def gop(n,m):
    if m==0 or m==1:
        return n
    else:
        return n*gop(n,m-1)
 
for test_case in range(10):
    T = int(input())
    n,m = map(int,input().split())
    print(f"#{T} {gop(n,m)}")