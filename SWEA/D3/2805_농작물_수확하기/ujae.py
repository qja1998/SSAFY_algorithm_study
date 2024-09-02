T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    crop_list=[]
    for i in range(N):
        crops = input()
        crop = list(map(int,str(crops)))
        crop_list.append(crop)
 
    result=0
    j=0
    for i in range(int(len(crop_list)/2)+1):
        result += sum(crop_list[i][int(len(crop_list)/2)-j:int(len(crop_list)/2)+j+1])
        j += 1
 
    j -= 2
    for k in range(i+1,len(crop_list)):
        result += sum(crop_list[k][int(len(crop_list)/2)-j:int(len(crop_list)/2)+j+1])
        j -= 1
 
    print(f"#{test_case} {result}")