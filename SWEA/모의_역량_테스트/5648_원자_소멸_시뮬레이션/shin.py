# 실제로는 1초당 1의 거리만큼 움직이지만, 0.5초에 만나는 경우도 있기 때문에 0.5씩 움직이도록 함
# 시뮬레이션 좌표(방향 벡터)
direction = {0:(0,0.5), 1:(0,-0.5), 2:(-0.5,0), 3:(0.5,0)}

# 충돌 확인 함수
def new_atom_info(atom_info):
    new_energy_info_dict = {}  # 각 좌표 마다 충돌 여부에 따른, energy(value) 값 들어가는 딕셔너리
    new_dir_info_dict = {}  # 해당 좌표 방향 저장 딕셔너리, 충돌은 상관 없음
    collision_crds = set()  # 충돌 되는 좌표 모음
    collision_egy = 0  # 충돌 되고 나온 에너지 합

    for a in atom_info:
        coord = (a[0], a[1])
        dir_info = a[2]
        power = a[3]
        # 충돌 했다면, 있는 좌표에 더하기 및 충돌 set에 추가
        if coord in new_energy_info_dict:
            new_energy_info_dict[coord] += power
            collision_crds.add(coord)
        # 충돌 안했다면, 딕셔너리에 정보 저장
        else:
            new_energy_info_dict[coord] = power
            new_dir_info_dict[coord] = dir_info
    
    # 새로운 리스트 받기
    result = []
    for crd, egy in new_energy_info_dict.items():
        # 충돌 확인 되면 값이 더해 지도록, 아니면 리스트에 추가
        if crd in collision_crds:
            collision_egy += egy
        else:
            # 좌표가 범위 내라면, 새 리스트에 추가
            if -1000 <= crd[0] <= 1000 and -1000 <= crd[1] <= 1000:
                result.append([crd[0], crd[1], new_dir_info_dict[crd], egy])

    return result, collision_egy


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nuclear_power_plant = [list(map(int, input().split())) for _ in range(N)]
    energy = 0

    # 모든 원자가 사라질때 까지
    while nuclear_power_plant:
        # 계속해서 움직임을 좌표에 더함
        for atom in nuclear_power_plant:
            dx, dy = direction[atom[2]]
            atom[0] += dx
            atom[1] += dy

        nuclear_power_plant, collision_energy = new_atom_info(nuclear_power_plant)
        # 반복 되면서 나온 에너지들 점차 더함
        energy += collision_energy

    print(f"#{tc} {energy}")
