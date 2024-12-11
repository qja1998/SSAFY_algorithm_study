N, M = map(int, input().split())

trees = list(map(int, input().split()))

def count_tree(h):
    result = 0
    for tree in trees:
        result += max(0, tree - h)
    return result

def bisearch(l, r):
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        result = count_tree(mid)

        # print(l, r)
        # print(mid, result)
        if result > M:
            # 목표보다 많으면 올리기
            ans = max(ans, mid)
            l = mid + 1
        elif result < M:
            # 목표 도달 못했으면 내리기
            r = mid - 1
        else:
            # 도달했으면 return
            return mid
        if l == mid:
            break
    return ans

print(bisearch(0, max(trees)))