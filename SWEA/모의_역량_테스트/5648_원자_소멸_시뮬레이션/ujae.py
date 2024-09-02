T = int(input())
 
move = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]
 
for test_case in range(1, T + 1):
    N = int(input())
    atom_info = [list(map(int, input().split())) for _ in range(N)]
    result = 0
 
    for _ in range(4000):
        atom_dict = {}
        collision_energy = {}
 
        # 원자 위치 업데이트
        for e in range(len(atom_info)):
            atom_info[e][0] += move[atom_info[e][2]][0]
            atom_info[e][1] += move[atom_info[e][2]][1]
 
        # 딕셔너리에 원자 위치 및 에너지 값 저장
        for a in range(len(atom_info)):
            key = (atom_info[a][0], atom_info[a][1])
            if key not in atom_dict:
                atom_dict[key] = atom_info[a][3]
            else:
                if key not in collision_energy:
                    collision_energy[key] = atom_dict[key]
                collision_energy[key] += atom_info[a][3]
 
 
        # 충돌한 원자들의 에너지 합산
        for energy in collision_energy.values():
            result += energy
 
        # 충돌한 원자 제거
        atom_info = [atom for atom in atom_info if (atom[0], atom[1]) not in collision_energy]
        if not atom_info:
            break
 
    print(f'#{test_case} {result}')