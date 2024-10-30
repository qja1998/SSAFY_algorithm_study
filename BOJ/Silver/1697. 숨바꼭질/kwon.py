# def solution(N, K):

#     if N == K:
#         return 0
#     if N == 0:
#         N += 1

#     n = 0

#     while N * 2**n <= K:
#         # print(N * 2**n, K)
#         n += 1
#     # print(N * 2**n)
#     before_diff = K - N * 2**(n-1)
#     after_diff = N * 2**n - K
#     # print(before_diff, after_diff)
#     # print()
#     if before_diff < after_diff:
#         n -= 1
#         remain = before_diff
#     else:
#         remain = after_diff


#     # remain = K % (N * 2^n)
#     # print(n, remain)
#     # print()

#     result = n

#     while N >= 0:
#         # print(remain)
#         # print(N, 2**N, remain // 2**N)
#         result += remain // 2**N
#         remain %= 2**N
#         N -= 1
#         # print(result)
    
#     return result

from collections import deque

def solution(N, K):
    q = deque([(N, 0)])
    visited = set([N])

    if N == K:
        return 0

    while q:
        cur_pos, time = q.popleft()
        if cur_pos > K:
            n_pos_list = [cur_pos - 1]
        else:
            n_pos_list = [cur_pos + 1, cur_pos - 1, cur_pos * 2]

        for n_pos in n_pos_list:
            if n_pos < 0:
                continue
            if n_pos in visited:
                continue
            if n_pos == K:
                return time+1
            q.append((n_pos, time+1))
            visited.add(n_pos)

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solution(N, K))