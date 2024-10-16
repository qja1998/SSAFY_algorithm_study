import math

def make_num(mli, idx, num):
    global max_num, min_num

    # 모든 숫자를 다 계산했다면
    if idx == N:
        max_num = max(max_num, num)  # 최대값 갱신
        min_num = min(min_num, num)  # 최소값 갱신
        return

    for op_idx, op_cnt in enumerate(mli):
        # 남은 연산자가 없으면 지나가기
        if op_cnt == 0:
            continue
        tmp_num = num
        if op_idx == 0:  # +
            tmp_num += nli[idx]
        elif op_idx == 1:  # -
            tmp_num -= nli[idx]
        elif op_idx == 2:  # *
            tmp_num *= nli[idx]
        elif op_idx == 3:  # /
            # a/0은 안하기
            if nli[idx] == 0:
                return
            tmp_num = int(tmp_num / nli[idx])

        mli[op_idx] -= 1
        make_num(mli, idx + 1, tmp_num)
        mli[op_idx] += 1

N = int(input())
nli = list(map(int, input().split()))
mli = list(map(int, input().split()))

max_num = -math.inf
min_num = math.inf

init_num = nli[0]
init_idx = 1

# mli_ 덧, 뺄, 곱, 나
make_num(mli, init_idx, init_num)

print(max_num)
print(min_num)