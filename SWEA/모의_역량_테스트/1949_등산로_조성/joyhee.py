## 51 中 29
import sys, pprint
sys.stdin = open("sample_input.txt", 'r')

def find_road(i, j, cnt, check):
    global already_fix, ans
    for dx, dy in dxy:
        nx, ny = i + dx, j + dy
        # 지도 범위를 넘어가면 안됨
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue
        # 계속계속 작아질거라서 체크는 없어도 되는걸까? 어차피 다음으로 나갔다면 되돌아올 수 없음. ㅏ 와서 공사할수도 있으니까, 안전상 체크ㅇ
        if check[nx][ny] != 0:
            continue
        # 이동하고자 하는 위치가 더 높으면 안됨
        if road_map[i][j] <= road_map[nx][ny]:
            # 선택지 1. 최대 K만큼 공사하고 진행하기 # 공사하는 선택지는 한번만 실행 가능.
            if road_map[nx][ny] - road_map[i][j] + 1 <= K and already_fix == False:
                # 공사할거면 already_fix를 True로 갱신
                already_fix = True
                cnt += 1
                check[nx][ny] = cnt
                temp = road_map[nx][ny]  # 원복에 사용하려고 기존 값 temp에 저장
                road_map[nx][ny] = road_map[i][j] - 1  # 공사
                # 다음 사방탐색
                ans = max(ans, cnt)
                find_road(nx, ny, cnt, check)
                cnt -= 1
                check[nx][ny] = 0
                road_map[nx][ny] = temp
                already_fix = False
            # 선택지 2. 안가기
            continue
        # 이동할 수 있는 상황이라면
        cnt += 1
        check[nx][ny] = cnt
        # 다음 사방탐색
        ans = max(ans, cnt)
        find_road(nx, ny, cnt, check)
        cnt -= 1
        check[nx][ny] = 0
    return ans

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
T = int(input())  # 총 테스트 케이스의 개수 T
for tc in range(1, 1+T):
    N, K = map(int, input().split())  # 지도의 한 변의 길이 N, 최대 공사 가능 깊이 K
    road_map = [list(map(int, input().split())) for _ in range(N)]  # N * N 크기의 지도 정보

    check = [[0]* N for _ in range(N)]

    # 정답은 가장 긴 등산로. max로 갱신하기 위해서 0으로 초기설정.
    ans = 0
    # 가장 높은 봉우리 찾기
    start = max(map(max, road_map))
    for i in range(N):
        for j in range(N):
            if road_map[i][j] == start:
                cnt = 1
                check[i][j] = cnt
                already_fix = False
                find_road(i, j, cnt, check)
                check[i][j] = 0

    print(f'#{tc} {ans}')