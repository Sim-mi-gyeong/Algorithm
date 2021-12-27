import time
start_time = time.time()

s = input()
num = [0, 1]
cnt = 0
# for i in s:
#     if i==0:
#         i==1
#     else:
#         i==0
re_s = ""
while(True):
    for i in range(len(s[:-1])):
        if s[i] != s[i+1]:
            s[i] = s[i+1]
            cnt += 1
            if s == s[::-1]:
                break
            
print(cnt)
end_time = time.time()
print("걸린 시간 : ", end_time - start_time)