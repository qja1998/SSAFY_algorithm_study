from math import factorial as fac
fac_num = fac(int(input()))
cnt = 0
while fac_num // 10 != 0 and fac_num % 10 == 0:
    fac_num = fac_num // 10
    cnt += 1
print(cnt)

