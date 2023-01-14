x, a, b = input().split()
l = len(x)


def get_minimum_l_value():  # 길이가 l 인 수 중 최소 수를 만들어 주는 함수
    if a == "0":
        return b + a * (l - 1)
    return a * l


if get_minimum_l_value() > x:
    # 정답의 길이는 (l-1) 이 되는 것 -> 그 자리 수만큼 b 로 채워주기
    if l == 1:
        print(-1)
    else:
        print(b * (l - 1))
    exit()

SMALL = False
ans = []
for i in range(l):
    if SMALL:  # 이미 X 보다 작은게 확정됐으니까, 더 큰 숫자인 B 를 사용해도 된다.
        ans.append(b)
    elif x[i] > b:
        ans.append(b)
        SMALL = True
    elif x[i] == b:
        ans.append(b)
    elif x[i] > a:
        ans.append(a)
        SMALL = True
    elif x[i] == a:
        ans.append(a)
    else:  # i 번째 위치에 사용할 수 있는 숫자가 없는 경우
        for j in range(i - 1, -1, -1):
            # 뒤에서 부터 -> B 를 사용한 최초의 위치를 찾아, 그 위치의 숫자를 양보
            if ans[j] == b:  # 양보할 수 있는 위치가 찾아진 상황
                ans[j] = a
                SMALL = True  # 해당 위치 이후는 전부 B 로 채우기
                for k in range(j + 1, i):  # j 이후는 전부 B
                    ans[k] = b
                break

print(*ans, sep="")


"""
866666475 6 8
68888888
"""

