def solution(n, lost, reserve):
    answer = n - len(lost)

    for i in range(len(reserve)):
        front = reserve[i] - 1
        back = reserve[i] + 1
        if front in lost:
            lost.remove(front)
            answer += 1
            continue
        if back in lost:    
            lost.remove(back)
            answer += 1
        else:
            continue
    return answer

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

print(solution(n, lost, reserve))

# cnt = n - len(lost)
# able = []

# for i in range(len(reserve)):
#     front = reserve[i] - 1
#     back = reserve[i] + 1
#     if front in lost:
#         lost.remove(front)
#         cnt += 1
#     elif back in lost:    
#         lost.remove(back)
#         # if (reserve[i] - 1) or (reserve[i] + 1) not in able:
#         #     able.append(reserve[i] - 1) or able.append(reserve[i] + 1)
#         cnt += 1
#     else:
#         continue

# print(cnt)
