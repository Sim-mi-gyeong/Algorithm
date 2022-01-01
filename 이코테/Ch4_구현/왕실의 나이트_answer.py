# 문제 해결 아이디어
# 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인
# 리스트를 이용해 8가지 방향에 대한 방향 벡터 정의

# 현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1   # ord(input_data[0]) 문자의 값을 아스키 코드 값으로 변환 

# 나이트가 이동할 수 있는 8가지 방향 정의
# dx, dy 두 개의 리스트 X -> 하나의 리스트로 표현
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대해 각 위치로 이동이 가능한지 확인ㅇ
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]   # row + step[1]: 행
    next_col = row + step[1]   # row + step[0]: 열
    # 해당 위치로 이동 가능하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1
print(result)