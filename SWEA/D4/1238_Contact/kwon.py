from collections import defaultdict, deque

TC = 10

def contact_search(contact_dict, start):
    q = deque([[start, 0]])

    visited = defaultdict(bool)
    visited[start] = True

    last_people = []
    time = 0
    last_time = 0
    while q:
        cur_person, time = q.popleft()
        if last_time < time:
            last_time = time
            last_people = [cur_person]
        else:
            last_people.append(cur_person)
        for n_person in contact_dict[cur_person]:
            if visited[n_person]:
                continue
            q.append([n_person, time+1])
            visited[n_person] = True
        # print(q)
        # print(last_people)
    return max(last_people)

for t in range(1, TC+1):
    n, start = map(int, input().split())

    nums = list(map(int, input().split()))

    contact_dict = defaultdict(list)

    for i in range(0, n, 2):
        contact_dict[nums[i]].append(nums[i+1])
    
    print(f"#{t} {contact_search(contact_dict, start)}")