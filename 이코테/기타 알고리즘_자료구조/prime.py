# 소수 판별 함수(2 이상의 자연수에 대해)
def is_prime_nuber(x):
    # 2부터 (x-1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어 떨어진다면,
        if x % i == 0:
            return False   # 소수 X
    return True

print(is_prime_nuber(4))
print(is_prime_nuber(7))