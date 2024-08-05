from collections import defaultdict

# 충돌하면 소멸

test_case = int(input())

# 상하좌우
dyx = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def move(y, x, d):
    nx, ny = x + dyx[d][0], y + dyx[d][1]
    if not (-1000 <= ny <= 1000 and -1000 <= nx <= 1000):
        return False
    return ny, nx


for t in range(test_case):
    n = int(input())

    atoms = defaultdict(list)

    result = 0
    for i in range(n):
        x, y, d, k = map(int, input().split())
        atoms[(y, x)].append([d, k, False])

    time = 0
    while atoms:
        visited = {}
        for y, x in list(atoms):
            if not atoms[(y, x)]:
                atoms.pop((y, x))
                continue
            for d, k, is_move in atoms[(y, x)]:
                if is_move:
                    continue
                is_collapsed = False
                nyx = move(y, x, d)

                atoms[(y, x)].remove([d, k, False])
                if not atoms[(y, x)]:
                    atoms.pop((y, x))
                # 범위 벗어나면 삭제
                if not nyx:
                    continue

                # 다음 위치에 아직 움직이지 않은 원자 있음 & 방향이 반대 -> 충돌
                for atom in atoms[nyx]:
                    if atom[2]:
                        continue
                    n_dy, n_dx = dyx[atom[0]]
                    dy, dx = dyx[d]
                    if (-dy, -dx) != (n_dy, n_dx):
                        continue
                    result += atom[1] + k
                    atoms[nyx].remove(atom)
                    if not atoms[nyx]:
                        atoms.pop(nyx)
                    is_collapsed = True
                    break
                if is_collapsed:
                    continue

                atoms[nyx].append([d, k, True])
                time += 1
        for y, x in list(atoms):
            if len(atoms[(y, x)]) >= 2:
                result += sum([atom[1] for atom in atoms[(y, x)]])
                atoms.pop((y, x))
                continue
            atoms[(y, x)][0][2] = False

    print(f"#{t + 1} {result}")