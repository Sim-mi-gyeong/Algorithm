# 괄호
# 제시된 테스트 케이스에서는 괄호 쌍이  [') (']는 VPS가 아님을 의미 
for i in range(int(input())):
    stack = []
    string = list(input())

    for i in string:
        if i == '(':
            stack.append(i)
        # ')' 일 때, 이전에 '('를 입력받지 않았으면 False(즉, ')'는 append 대상이 X)
        else: 
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break       
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')