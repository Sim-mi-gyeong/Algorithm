# 예산

n = int(input())
lst = list(map(int, input().split()))
total = int(input())
lst.sort()
start, end = 1, lst[-1]

def binarySearch(lst, start, end):
    tmpTotal = 0
    while start <= end:
        mid = (start + end) // 2
        tmpSum = 0
        for i in lst:
            if i <= mid:
                tmpSum += i
            else:
                tmpSum += mid
        if tmpSum <= total:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

if sum(lst) <= total:
    print(lst[-1])
else:
    ans = binarySearch(lst, start, end)
    print(ans)