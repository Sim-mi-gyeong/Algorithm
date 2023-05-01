def solution(s):
    answer = False

    stack = []

    # s[0] == ')' 인 경우
    if s[0] == ")":
        return answer
    # ( 이면 넣고, 가장 위가 ( 인데, ) 를 넣으려고 하면 pop
    for tmp in s:
        if tmp == "(":
            stack.append(tmp)
        elif tmp == ")" and len(stack) > 0 and stack[-1] == "(":
            stack.pop()

    if len(stack) == 0:
        answer = True

    return answer
