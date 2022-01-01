# 문제 해결 아이디어
# 문자열 입력 시 문자를 하나씩 확인
# -> 숫자인 경우 따로 합 계산
# -> 알파벳은 별도의 리스트에 저장
# 리스트에 저장된 알파벳을 정렬해 출력 + 합계를 뒤에 붙여 출력

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)
# 알파벳을 오름차순 정렬
result.sort()
if value != 0:
    result.append(str(value))

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
# 최종 결과 출력(리스트 -> 문자열 변환)
print(''.join(result))