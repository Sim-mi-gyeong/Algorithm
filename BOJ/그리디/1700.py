# 멀티탭 스케줄링

n, k = map(int, input().split()) 
lst = list(map(int, input().split()))
cnt = 0

plug = []

for i in range(k):
    # 사용하려고 하는 전기용품이 꽂혀있는 경우, 뽑지 않아도 됨
    if lst[i] in plug:
        continue
    # 멀티탭이 비어있는 자리가 있는 경우, 꽂기
    elif len(plug) < n:
        plug.append(lst[i])
        continue
    # 꽉차있는데 사용하려고 하는 전기용품이 꽂혀있지 않는 경우 -> 뽑아야 함
    else:
        idx = -1e9
        isExist = True   # 존재 여부
        for k, v in enumerate(plug):
            # 앞으로 사용하지 않는 제품은 뽑는다
            if v not in lst[i+1:]:
                plug[k] = lst[i]   # 뽑아서 현재 제품으로 꽂기
                isExist = False
                break
            # 이후에 사용하게 될 경우, 최대한 나중에 등장하는 것 찾기
            else:
                # 리스트를 자르는 경우, 인덱스가 원래 리스트와 동일하지 않으므로 -> 자른만큼 더해주기
                idx = max(idx, lst[i+1:].index(v) + i + 1)
        if idx != -1e9 and isExist == True:x      
            # 플러그에서 뽑아서 현재 제품으로 꽂기
            plug[plug.index(lst[idx])] = lst[i]
        cnt += 1
print(cnt)