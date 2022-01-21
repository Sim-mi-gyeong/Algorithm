# 플로이드

from xml.sax import make_parser


n = int(input())   # 도시의 수
m = int(input())   # 버스의 수
lst = [list(map(int, input().split())) for _ in range(m)]    # 시작 도시, 도착 도시, 비용
# lst = []
# for i in range(m):
#     a, b, c = map(int, input().split())
print(lst)
money = [[0] * n for _ in range(n)]
city = [[0] * n for _ in range(n)]
for i in lst:
    a, b, c = i[0], i[1], i[2]
    city[a-1][b-1] = 1
    money[a-1][b-1] = c
    # if money[a-1][b-1] < c:
    #     continue
    # money[a-1][b-1] = min(money[a-1][b-1], c)
# for i in lst:
#     a, b, c = i[0], i[1], i[2]
#     money[a-1][b-1] = c
print('중간 지점 처리 전 : ', city)
print()
print('중간 지점 처리 전 금액 : ', money)
ans = [[100000] * n for _ in range(n)]
for k in range(5):
    for i in range(5):
        for j in range(5):
            if city[i][j] == 1: 
                ans[i][j] = min(ans[i][j], money[i][j])
            # if city[i][j] == 1 or city[i][j] == 0: 
            #     ans[i][j] = money[i][j]
            # elif city[i][j] == 0: ans[i][j] = money[i][j]
            elif city[i][j] == 0 and city[i][k] == 1 and city[k][j] == 1:
                # 비용 더한 거 처리
                # money[i][j] = min(money[i][j], money[i][k] + money[k][j])
                ans[i][j] = min(ans[i][j], money[i][k] + money[k][j])
                # pass
                # city[i][j] = 1
print()            
# print('중간 지점 처리 후 : ', city)
print()
print('중간 지점 처리 후 금액 money: ', money)

print()
print('중간 지점 처리 후 금액 ans : ', ans)
