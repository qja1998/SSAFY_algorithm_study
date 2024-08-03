import sys
from collections import defaultdict
input = sys.stdin.readline

def topological_sort(xy_dict, d_list, first_val, counts, target):
    times = {val:d_list[val - 1] for val in first_val}
    q = first_val
    
    while q:
        cur = q.pop(0)
        if cur == target: return times[target]
        for next in xy_dict[cur]:
            if next not in times:
                times[next] = times[cur] + d_list[next - 1]
            else:
                times[next] = max(times[cur] + d_list[next - 1], times[next])
            counts[next] -= 1
        tmp = list(counts.keys())[:]
        for i in tmp:
            if counts[i] == 0:
                q.append(i)
                del counts[i]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    xy_dict = defaultdict(list)
    d_list = list(map(int, input().split()))
    
    counts = defaultdict(int)
    first_val = list(range(1, n + 1))
    for i in range(k):
        x, y = map(int, input().split())
        xy_dict[x].append(y)
        counts[y] += 1
        try: first_val.remove(y)
        except: pass
    target = int(input())
        
    if target in counts:
        print(topological_sort(xy_dict, d_list, first_val, counts, target))
    else:
        print(d_list[target - 1])