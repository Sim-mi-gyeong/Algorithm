n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k) : cnt += 1

print('전체 : ', cnt)