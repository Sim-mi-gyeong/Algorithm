from collections import defaultdict


def solution(genres, plays):
    answer = []
    dic = dict()
    dic2 = defaultdict(list)

    for i in range(len(genres)):
        dic2[genres[i]].append((plays[i], i))

    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = plays[i]
        else:
            dic[genres[i]] += plays[i]

    dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    for key in dic.keys():
        dic2[key].sort(key=lambda x: (x[0], -x[1]), reverse=True)
        for music in dic2[key][:2]:
            answer.append(music[1])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
