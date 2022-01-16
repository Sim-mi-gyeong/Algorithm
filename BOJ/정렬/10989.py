# 수 정렬하기3
# 다시(메모리 초과 해결)
import sys

num = [map(int, sys.stdin.readlines().split()) for _ in range(int(sys.stdin.readlines()))]
num.sort()
for i in num: print(i)