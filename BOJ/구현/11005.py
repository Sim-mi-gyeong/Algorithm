# 진법 변환 2

n, b = map(int, input().split())
result = []
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# A -> 65 / Z -> 90
while (
    n
):  # 연산 과정에서 n < b 인 경우, 나누어진 값 n 을 진법 변환한 결과로 나타내기 위해 나머지 처리하고자 한 번 더 나눠 -> 몫을 0으로 만들고 & 나머지로
    if n % b >= 10:
        num = n % b + 55
        s = chr(num)
        result.append(s)
    else:
        result.append(n % b)
    n //= b

print("".join(map(str, result[::-1])))
