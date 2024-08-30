test_case = int(input())

connect_dict = {
    # 상하좌우에 대해 어떤 면과 어떤 부분이 접하는지
    'u': [
        ['b', (-1, None)],
        ['r', (None, 0)],
        ['f', (0, None)],
        ['l', (None, -1)]
    ],
    'f': [
        ['u', (-1, None)],
        ['r', (None, 0)],
        ['d', (0, None)],
        ['l', (None, -1)]
    ],
    'r': [
        ['u', (-1, None)],
        ['b', (None, 0)],
        ['d', (0, None)],
        ['f', (None, -1)]
    ],
    'd': [
        ['f', (-1, None)],
        ['r', (None, 0)],
        ['b', (0, None)],
        ['l', (None, -1)]
    ],
    'b': [
        ['u', (-1, None)],
        ['l', (None, 0)],
        ['d', (0, None)],
        ['f', (None, -1)]
    ],
    'l': [
        ['u', (-1, None)],
        ['f', (None, 0)],
        ['d', (0, None)],
        ['b', (None, -1)]
    ],
}

def _turn_plane(plane, direction):
    if direction == '+':
        cube[plane] = list(zip(*cube[plane][::-1]))
    else:
        cube[plane] = list(zip(*cube[plane]))[::-1]

def _get_side_color(plane, y, x):
    if x is None:
        return cube[plane][y]
    return [row[x] for row in cube[plane]]

def _set_side_color(plane, y, x, new_color):
    if x is None:
        cube[plane][y] = new_color
        return
    for y in range(3):
        cube[plane][y][x] = new_color[y]

def _turn_side(plane, direction):
    if direction == '+':
        side_color_list = []
        for i, (side, (y, x)) in enumerate(connect_dict[plane]):
            if i >= 2:
                side_color_list += _get_side_color(side, y, x)[::-1]
            else:
                side_color_list += _get_side_color(side, y, x)
        # 시계방향 회전
        side_color_list = side_color_list.pop() + side_color_list
        
        for i in range(0, 12, 3):
            _set_side_color(side)
        
    else:
        pass

def turn_cube(plane, direction):
    _turn_plane(plane, direction)
    _turn_side(plane, direction)

for t in range(test_case):
    n = int(input())
    turn_list = list(map(int, input().split()))

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

    for turn in turn_list:
        plane, direction = turn[0], turn[1]

        turn_cube(plane, direction)