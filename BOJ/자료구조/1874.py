# 스택 수열

n = int(input())
stack = []
cal = []   # 모든 수를 입력한 후에 'NO' or 계산 결과를 출력하기 위한 cal 저장 리스트
a = 1
ans = True   # 가능 / 불가능 여부 Check
for i in range(n):   # 입력 횟수를 위한 반복문
    target = int(input())
    while a <= target:
        stack.append(a)
        cal.append('+')
        a += 1
    if stack[-1] != target:
        ans = False
    elif stack[-1] == target:
        stack.pop()
        cal.append('-')
if ans:
    for i in cal: print(i)
else: print('NO')