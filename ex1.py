n = int(input())
lstA = list(map(int, input().split()))

m = int(input())
lstM = list(map(int, input().split()))

lstA.sort()
for m in lstM:
    check = False
    start, end = 0, len(lstA) - 1
    while start <= end:
        mid = (start + end) // 2
        if lstA[mid] < m:
            start = mid + 1
        else:
            end = mid - 1

        if lstA[mid] == m:
            check = True
    if check:
        print(1)
    else:
        print(0)
