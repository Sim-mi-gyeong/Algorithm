def solution(tickets):
    answer = []
    n = len(tickets) + 1

    visited = [0] * n  # tickets 에 존재하는 항공권 종류별(index)로 사용 여부

    def dfs(target, path):
        if len(path) == n:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            start, end = ticket[0], ticket[1]

            # 각 항공권들에 대해(반복) 시작 위치 == target 인 경우
            # idx 번째 항공권을 사용하지 않은 경우
            if start == target and not visited[idx]:
                visited[idx] = 1
                dfs(end, path + [end])
                visited[
                    idx
                ] = 0  # 여러가지 경로가 존재할 수 있으므로, 즉 지나갔던 공항으로 다시 돌아와서 다른 경로를 탐색할 수 있으므로 백트래킹 가능하도록

    # 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 -> 여러개의 경로 존재 가능
    dfs("ICN", ["ICN"])

    answer.sort()
    answer = answer[0]

    return answer
