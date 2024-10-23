def find_circle(now_num):
    global key_set, value_set
    if now_num not in key_set:
        key_set.add(now_num)
        value_set.add(value_dict[now_num])
        find_circle(value_dict[now_num])
    else:
        return


N = int(input())
value_list = [int(input()) for _ in range(N)]
value_dict = {}
result_set = set()

for i in range(len(value_list)):
    value_dict[i+1] = value_list[i]
    if i+1 == value_list[i]:
        result_set.add(i+1)

result_list = []
dummy_key_set = set()

for i in range(1, N+1):
    key_set = set()
    value_set = set()
    key_set = key_set | result_set
    value_set = value_set | result_set
    find_circle(i)
    if key_set == value_set:
        dummy_key_set = dummy_key_set | key_set
        result_list = list(dummy_key_set)

print(len(result_list))
for val in sorted(result_list):
    print(val)
