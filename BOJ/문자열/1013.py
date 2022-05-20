# Contact

import re

t = int(input())
for _ in range(t):
    s = input()
    regex = re.compile("(100+1+|01)+")
    if regex.fullmatch(s):
        print("YES")
    else:
        print("NO")

"""
regex = re.compile('정규식') : compile() - 패턴 객체 반환
regex.match(s) : match() - 검색 메서드(매칭되는 것을 반환, 매칭 위치 반환) <re.Match object; span=(0, 6), match='100101'>
"""
