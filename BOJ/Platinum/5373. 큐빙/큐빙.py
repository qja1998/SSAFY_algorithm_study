test_case = int(input())

def show_cube(cube):
    planar = []

    plane_b = [row[::-1] for row in cube['b'][::-1]]
    plane_l = list(map(list,zip(*cube['l'][::-1])))
    plane_r = list(map(list, zip(*cube['r'])))[::-1]

    planar.append([' ']*3 + plane_b[0])
    planar.append([' ']*3 + plane_b[1])
    planar.append([' ']*3 + plane_b[2])

    planar.append(plane_l[0] + cube['u'][0] + plane_r[0])
    planar.append(plane_l[1] + cube['u'][1] + plane_r[1])
    planar.append(plane_l[2] + cube['u'][2] + plane_r[2])

    planar.append([' ']*3 + cube['f'][0])
    planar.append([' ']*3 + cube['f'][1])
    planar.append([' ']*3 + cube['f'][2])

    planar.append([' ']*3 + cube['d'][0])
    planar.append([' ']*3 + cube['d'][1])
    planar.append([' ']*3 + cube['d'][2])

    return planar

connect_dict = {
    # 상하좌우에 대해 어떤 면과 어떤 부분이 접하는지
    'u': [
        ['b', (0, None)],
        ['r', (0, None)],
        ['f', (0, None)],
        ['l', (0, None)]
    ],
    'f': [
        ['u', (-1, None)],
        ['r', (None, 0)],
        ['d', (0, None)],
        ['l', (None, -1)]
    ],
    'r': [
        ['u', (None, -1)],
        ['b', (None, 0)],
        ['d', (None, -1)],
        ['f', (None, -1)]
    ],
    'd': [
        ['f', (-1, None)],
        ['r', (-1, None)],
        ['b', (-1, None)],
        ['l', (-1, None)]
    ],
    'b': [
        ['u', (0, None)],
        ['l', (None, 0)],
        ['d', (-1, None)],
        ['r', (None, -1)]
    ],
    'l': [
        ['u', (None, 0)],
        ['f', (None, 0)],
        ['d', (None, 0)],
        ['b', (None, -1)]
    ],
}

def _turn_plane(plane, direction):
    if direction == '+':
        cube[plane] = list(map(list, zip(*cube[plane][::-1])))
    else:
        cube[plane] = list(map(list, zip(*cube[plane])))[::-1]

def _get_side_color(plane, y, x):
    if x is None:
        return cube[plane][y]
    return [row[x] for row in cube[plane]]

def _set_side_color(plane, y, x, new_color, direction):
    if x is None:
        cube[plane][y] = new_color
        return
    # if plane == 'b':
    #     # 위치 반전
    #     if direction == '+':
    #         # u -> l 로 넘어갈 때 반전
    #         x = abs(x-2)
    #         pass
    #     else:
    #         x = abs(x-2)
    #         pass
    for y in range(3):
        cube[plane][y][x] = new_color[y]

'''
R, L: B로 오고 갈 때 반전 필요(열 내)
F: U-L, D-R로 넘어갈 때 반전 필요(열 내)
B: U-L, D-R로 넘어갈 때 반전 필요(위치, 열 내)
'''

def _turn_side(plane, direction):
    side_color_list = []
    for i, (side, (y, x)) in enumerate(connect_dict[plane]):
        side_color_list += _get_side_color(side, y, x)
    if direction == '+':
        if plane == 'r':
            # 넘어가기 전에 u, b 반전
            side_color_list = side_color_list[:3][::-1] + side_color_list[3:6][::-1] + side_color_list[6:]
        elif plane == 'l':
            # 넘어가기 전에 d, b 반전
            side_color_list = side_color_list[:6] + side_color_list[6:9][::-1] + side_color_list[9:][::-1]
        elif plane == 'f':
            # 넘어가기 전에 r, l 반전
            side_color_list = side_color_list[:3] + side_color_list[3:6][::-1] + side_color_list[6:9] + side_color_list[9:][::-1]
        elif plane == 'b':
            # 넘어가기 전에 d, u 반전
            side_color_list = side_color_list[:3][::-1] + side_color_list[3:6] + side_color_list[6:9][::-1] + side_color_list[9:]
        # 시계방향 회전
        side_color_list = side_color_list[-3:] + side_color_list[:-3]
    else:
        if plane == 'r':
            # 넘어가기 전에 d, b 반전
            side_color_list = side_color_list[:3] + side_color_list[3:6][::-1] + side_color_list[6:9][::-1] + side_color_list[9:]
        elif plane == 'l':
            # 넘어가기 전에 u, b 반전
            side_color_list = side_color_list[:3][::-1] + side_color_list[3:9] + side_color_list[9:][::-1]
        elif plane == 'f':
            # 넘어가기 전에 d, u 반전
            side_color_list = side_color_list[:3][::-1] + side_color_list[3:6] + side_color_list[6:9][::-1] + side_color_list[9:]
        elif plane == 'b':
            # 넘어가기 전에 r, l 반전
            side_color_list = side_color_list[:3] + side_color_list[3:6][::-1] + side_color_list[6:9] + side_color_list[9:][::-1]
            
        # 반시계 회전
        side_color_list = side_color_list[3:] + side_color_list[:3]
    
    for i, (side, (y, x)) in enumerate(connect_dict[plane]):

        _set_side_color(side, y, x, side_color_list[i*3:i*3+3], direction)

def turn_cube(plane, direction):
    _turn_plane(plane, direction)
    _turn_side(plane, direction)

for t in range(test_case):
    n = int(input())
    turn_list = input().split()

    cube = {
        'u': [
            ['w', 'w', 'w'],
            ['w', 'w', 'w'],
            ['w', 'w', 'w']
        ],
        'f': [
            ['r', 'r', 'r'],
            ['r', 'r', 'r'],
            ['r', 'r', 'r']
        ],
        'r': [
            ['b', 'b', 'b'],
            ['b', 'b', 'b'],
            ['b', 'b', 'b']
        ],
        'd': [
            ['y', 'y', 'y'],
            ['y', 'y', 'y'],
            ['y', 'y', 'y']
        ],
        'b': [
            ['o', 'o', 'o'],
            ['o', 'o', 'o'],
            ['o', 'o', 'o']
        ],
        'l': [
            ['g', 'g', 'g'],
            ['g', 'g', 'g'],
            ['g', 'g', 'g']
        ],
    }

    # cube = {
    #     'u': [
    #         ['w1', 'w2', 'w3'],
    #         ['w4', 'w5', 'w6'],
    #         ['w7', 'w8', 'w9']
    #     ],
    #     'f': [
    #         ['r1', 'r2', 'r3'],
    #         ['r4', 'r5', 'r6'],
    #         ['r7', 'r8', 'r9']
    #     ],
    #     'r': [
    #         ['b1', 'b2', 'b3'],
    #         ['b4', 'b5', 'b6'],
    #         ['b7', 'b8', 'b9']
    #     ],
    #     'd': [
    #         ['y1', 'y2', 'y3'],
    #         ['y4', 'y5', 'y6'],
    #         ['y7', 'y8', 'y9']
    #     ],
    #     'b': [
    #         ['o1', 'o2', 'o3'],
    #         ['o4', 'o5', 'o6'],
    #         ['o7', 'o8', 'o9']
    #     ],
    #     'l': [
    #         ['g1', 'g2', 'g3'],
    #         ['g4', 'g5', 'g6'],
    #         ['g7', 'g8', 'g9']
    #     ],
    # }

    for turn in turn_list:
        plane, direction = turn[0], turn[1]
        turn_cube(plane.lower(), direction)
    for row in cube['u']:
        print(''.join(row))