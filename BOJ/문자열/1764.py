# 듣보잡
# 두 개의 리스트에서 중복되는 원소
# [1] set 으로 만들어 교집합만 찾기
# [2] b 리스트를 입력받을 때, a 에 있는지 확인 후 넣기
n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
a.sort()
b.sort()
ans = []
# for i in a:
#     if i in b: ans.append(i)
ans = list(set(a) & set(b))
ans.sort()
print(len(ans))
for i in ans: print(i)

# 'in' 연산자 시간 복잡도
# list, tuple : 평균 O(n) / set, dictionary : O(1)