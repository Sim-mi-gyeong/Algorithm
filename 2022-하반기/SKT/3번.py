import sys

input = sys.stdin.readline

n = int(input())
target = input().strip()
word_set = set()  # 각 단어의 집합을 set 에 저장 -> 단어를 거꾸로 좌우 반전시켜 Trie에 저장도 가능
for _ in range(n):
    word = input().strip()
    word_set.add(word)

# dp 테이블 초기화
dp = [-1 for _ in range(len(target) + 1)]
# 0번째가 아닌, 첫번째에 0 으로 값을 세팅
dp[1] = 0  # j = 1 일 때 dp[1] = 0 과 같이 dp[1] 에 0이 써있어야 첫 번째 단어를 선택할 수 있기 때문

# dp 테이블의 i 번째를 채우고 싶은데,
for i in range(2, len(target) + 1):
    # 마지막 단어가 j ~ i 번째까지 라고 생각을 하고,
    # last word : target 의 j 번째 문자 ~ i 번째 문자
    # -> 이때의 파티션 값은, j 번째 단어까지 잘 만들어지고, 거기다가 + last word 가 뒤에 붙는 것
    for j in range(i - 9, i):
        # if target[j - 1 : i] in word_set : in 이라는 연산을 빨리 수행하고자 word_set 을 저장할 때 set() 을 사용 -> hash set() 은 in 연산의 시간 복잡도가 O(1)
        if j >= 1 and dp[j] != -1 and target[j - 1 : i] in word_set:
            dp[i] = max(dp[i], dp[j] + 1)  # dp[i] + 1 : j 번째까지 단어 뒤에 last word 가 붙는 것

print(dp[len(target)])
print(dp)


"""
8
abcdefghij
abcde
dfgh
hij
abcd
de
efg
ghi
ij

ans : 5
"""
