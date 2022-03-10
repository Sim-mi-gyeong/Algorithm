# 랜선 자르기

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]
lst.sort()
start, end = 0, lst[-1]
def binarySearch(lst, n, start, end):
    while start <= end:
        # 여기서 이 부분을 해주면, 자르게 되는 길이 정보가 반복문 시작부터 start(=mid+1) 값으로 초기화 
        # -> 조건 만족 여부와 관계없이 이전 반복문에서 조건을 만족했을 때 start = mid+1 값이 length에 저장되는 것
        # length = start = 0  
        cnt = 0
        mid = (start + end) // 2
        if mid == 0: mid = end
        for i in lst:
            cnt += (i // mid)
        if cnt >= n:
            length = max(0, mid)
            start = mid +1
        else:
            end = mid - 1

    return length

print(binarySearch(lst, n, start, end))

'''
[입력 예시]
9 3785
73085
6747
87849
30807
79944
26905
92558
15313
2016
[출력 예시]
109

[입력 예시]
4 4
4
1
5
5
[출력 예시]
2

[입력 예시]
4 4
9
9
9
10
[출력 예시]
9
'''