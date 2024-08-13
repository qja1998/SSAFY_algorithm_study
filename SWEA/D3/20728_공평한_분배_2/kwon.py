test_case = int(input())

# 전체 조합을 구할 경우 50C25 = 1000조 -> 완탐으로 풀 수 없으므로 그리디로 접근

for t in range(test_case):
    n, k = map(int, input().split())

    candies = sorted(list(map(int, input().split())))

    result = float('inf')
    for i in range(n - k + 1):
        result = min(result, candies[i + k - 1] - candies[i])

    print(f"#{t + 1} {result}")