def solution(genres, plays):
    answer = []
    dic = {i: [] for i in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        dic[e[0]].append([e[1], e[2]])

    # x : list(dic.keys()) 의 원소
    # y : dic[x]의 원소
    genreSort = sorted(
        list(dic.keys()), key=lambda x: sum(map(lambda y: y[0], dic[x])), reverse=True
    )
    for genre in genreSort:
        tmp = [music[1] for music in sorted(dic[genre], key=lambda x: (x[0], -x[1]), reverse=True)]
        answer += tmp[:2]
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
