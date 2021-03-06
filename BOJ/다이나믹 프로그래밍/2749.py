# 피보나치 수 3
# 피사노 주기(피보나치 수를 어떤 수로 나눈 나머지를 구하라) -> 배열 X
# k 로 나눈 나머지가 항상 같은 주기를 갖게 되는 것
# 주기가 p 일 때, [ n 번째 피보나치 수를 m으로 나눈 나머지 ] = [ (n % p) 번째 피보나치 수를 m 으로 나눈 나머지]
# 나누려는 수 m = 10^k -> k > 2 일 때, 주기 p = 15 * 10^(k-1)

n = int(input())
m = 1000000
p = 1500000
n %= p
def fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b % m, (a + b) % m
    return a   # n 번째 수
print(fibo(n)) 