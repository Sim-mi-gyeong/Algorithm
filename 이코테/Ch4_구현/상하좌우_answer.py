# 문제 해결 아이디어

# n 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향  ->  나만의 방향(순서) 정해서 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]   # nx, ny 초기화 과정이 앞에 없어도 됨.
            ny = y + dy[i]

    # 공간을 벗어나는 경우는 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue   # 다음 순번의 loop를 돌도록 강제  / pass: 단순히 실행할 코드 없음
    # 이동 수행
    x, y = nx, ny

print(x, y)   # 3 4
