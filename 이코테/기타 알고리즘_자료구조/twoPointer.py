n = 5   # 데이터의 개수 N
m = 5   # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5]

cnt = 0
intervalSum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while intervalSum < m and end < n:
        intervalSum += data[end]
        end += 1
    # 부분합이 m 일 때 카운트 증가
    if intervalSum == m:
        cnt += 1
    intervalSum -= data[start]

print(cnt)