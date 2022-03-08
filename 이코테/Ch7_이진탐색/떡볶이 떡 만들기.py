# 절단기에 설정 가능한 높이 값이 커지게 되면 -> 잘린 떡의 길이 합은 감소
# 절단기에 설정 가능한 높이 값이 작아지게 되면 -> 잘린 떡의 길이 합은 증가


n, m = map(int, input().split())
lst = list(map(int, input().split()))
h = max(lst)
sum = 0
# 적어도 m 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값
while(True):
    for i in lst:
        if i > h:
            gap = i - h
        else: gap = 0
        sum += gap
    if sum >= m: break
    else:
        h -= 1
        sum = 0

print(h)

'''
[입력 예시]
4 6
19 15 10 17
[출력 예시]
15
'''