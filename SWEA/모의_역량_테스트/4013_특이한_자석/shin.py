from collections import deque


def rotate_magnetic_check(mag, rot, visited):
    if visited[mag] != 0: return

    visited[mag] = rot

    # 오른쪽 자석을 체크
    if mag < 3 and magnetic[mag][RIGHT_POS] != magnetic[mag + 1][LEFT_POS]:
        rotate_magnetic_check(mag + 1, -rot, visited)

    # 왼쪽 자석을 체크
    if mag > 0 and magnetic[mag][LEFT_POS] != magnetic[mag - 1][RIGHT_POS]:
        rotate_magnetic_check(mag - 1, -rot, visited)


def rotate_magnetic(mag_list, visited):
    for i, v in enumerate(visited):
        if v == 1:
            mag_list[i].rotate(1)
        elif v == -1:
            mag_list[i].rotate(-1)


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    MAGNETIC_NUM = 4
    magnetic = [deque(list(map(int, input().split()))) for _ in range(MAGNETIC_NUM)]
    turn_list = [list(map(int,input().split())) for _ in range(K)]
    ARROW_POS, LEFT_POS, RIGHT_POS = 0, 6, 2

    for tl in turn_list:
        magnetic_order, rotate_dir = tl
        visited = [0] * 4

        rotate_magnetic_check(magnetic_order - 1, rotate_dir, visited)

        rotate_magnetic(magnetic, visited)

    result = sum(2 ** i for i in range(MAGNETIC_NUM) if magnetic[i][0] == 1)
    print(f"#{tc} {result}")
