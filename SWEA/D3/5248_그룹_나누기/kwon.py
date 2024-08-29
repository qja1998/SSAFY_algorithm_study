from collections import deque, defaultdict

test_case = int(input())

for t in range(test_case):
    n, m = map(int, input().split())
    papers = list(map(int, input().split()))

    group_dict = defaultdict(list)
    for i in range(0, len(papers), 2):
        group_dict[papers[i]].append(papers[i+1])
        group_dict[papers[i+1]].append(papers[i])

    cnt = 0
    visited = defaultdict(bool)
    for student in range(1, n+1):
        if visited[student]:
            continue
        cnt += 1
        q = deque([student])
        while q:
            cur_std = q.popleft()
            for n_std in group_dict[cur_std]:
                if visited[n_std]:
                    continue
                q.append(n_std)
                visited[n_std] = True
    
    print(f"#{t+1} {cnt}")