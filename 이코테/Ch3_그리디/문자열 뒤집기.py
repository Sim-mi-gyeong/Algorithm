# 선택지는 0과 1뿐이다!!
import time
start_time = time.time()

s = input()   # 전부 1로 혹은 0으로 바꾸기
num = [0, 1]  
cnt0 = 0
cnt1 = 0

# for i in range(len(s)):
#     for j in range(len(s[1:])):   
#         if s[i] == s[j]:   # i번째 원소에 대해 j번째 원소와 같으면 넘어가고, 
#             pass
#         else:
#             s[j] == s[i]   # 같지 않을 때는 j번째 원소를 i번째 원소로 바꾸어주고
#             cnt += 1   # 바꾼 횟수 += 1
#             if s[i] == s[j]:   # 만약, j번째 원소가 다시 i번째 원소와 같아지면  i += 1
#                 break

# for i in s:
#     if s[0] == 0:   # 시작이 0으로 시작하면 0으로 바꾸어주고
#         cnt0 = 0
#     else:   # 시작이 1로 시작하면 1로 바꾸어주기
#         cnt1 = 1
if s[0] == 0:   # 시작이 0으로 시작하면 0으로 바꾸어주고
    cnt0 = 0
else:   # 시작이 1로 시작하면 1로 바꾸어주기
    cnt1 = 1

for i in s:
    if i == 0:
        pass



print()
end_time = time.time()
print("걸린 시간 : ", end_time - start_time)