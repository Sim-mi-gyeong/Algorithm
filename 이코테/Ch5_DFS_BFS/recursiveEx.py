def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, ' 번째 재귀함수에서 ', i+1, ' 번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, ' 번째 재귀함수를 종료합니다.')

recursive_function(1)
# 1번째에서 ~ 2번째 호출 / 1번째 종료 사이에 계속해서 '호출 - 종료' 가 누적
#  함수에 대한 정보가 스택에 담긴 것과 같이, 차례대로 호출되었다가 가장 마지막에 호출된 함수부터 차례대로 종료