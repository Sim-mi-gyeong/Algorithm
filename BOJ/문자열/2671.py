# 잠수함식별

import re

s = input()
pattern = "(100+1+|01)+"  # pattern = "[100+1+|01]+"
regexPattern = re.compile(pattern)
# match, search : 정규식과 매치될 때 match 객체를 돌려줌
# group() : 매치된 문자열 출력
m = regexPattern.fullmatch(s)  # 매치할 경우 :  <re.Match object; span=(0, 15), match='100000000001101'>
if m:
    print("SUBMARINE")
else:
    print("NOISE")
