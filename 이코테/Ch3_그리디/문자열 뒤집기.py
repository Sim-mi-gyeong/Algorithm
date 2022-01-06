# 실제로 바꿀 필요는 없고, 횟수만 count
import time
start_time = time.time()

s = input()   # 전부 1로 혹은 0으로 바꾸기
cnt0 = 0
cnt1 = 0
if s[0] == '1':   # 첫 번째 원소가 1인 경우 cnt0(모두 0으로 만들 때까지의 횟수)에 + 1하고 시작(1 -> 0으로 바꿀 때의 횟수)
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        # 다음 수가 0인 경우 -> 1로 바꾸기
        if s[i+1] == '0':
            cnt1 += 1
        # 다음 수가 1인 경우 -> 0으로 바꾸기
        else:
            cnt0 += 1

end_time = time.time()
print(min(cnt0, cnt1))
print("걸린 시간 : ", end_time - start_time)

# 바로 옆의 원소끼리만 비교하면 됨! -> i 와 i + 1 의 위치만 확인하므로 i, j 위치에 대한 이중 for문 필요 X

# for i in range(len(s)):
#     for j in range(len(s[1:])):   
#         if s[i] == s[j]:   # i번째 원소에 대해 j번째 원소와 같으면 넘어가고, 
#             pass
#         else:
#             s[j] == s[i]   # 같지 않을 때는 j번째 원소를 i번째 원소로 바꾸어주고
#             cnt += 1   # 바꾼 횟수 += 1
#             if s[i] == s[j]:   # 만약, j번째 원소가 다시 i번째 원소와 같아지면  i += 1
#                 break