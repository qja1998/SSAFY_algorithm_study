test_case = int(input())
for t in range(test_case):
    bi_dict = {
        "00": 0,
        "01": 0,
        "10": 0,
        "11": 0,
    }

    bi_cnt = list(map(int, input().split()))

    bi_dict["00"] = bi_cnt[0]
    bi_dict["01"] = bi_cnt[1]
    bi_dict["10"] = bi_cnt[2]
    bi_dict["11"] = bi_cnt[3]
    
    result = ''
    if bi_dict["01"] == 0 and bi_dict["10"] == 0:
        if bi_dict["00"] == 0:
            result += "1" * bi_dict["01"] + "1"
        elif bi_dict["11"] == 0:
            result += "0" * bi_dict["01"] + "0"

    else:
        if bi_dict["01"] == bi_dict["10"]:
            