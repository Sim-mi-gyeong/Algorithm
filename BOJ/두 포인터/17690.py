# 회문
import sys

input = sys.stdin.readline

n = int(input())


def checkPalindrome(s):
    check = True
    reverseS = s[::-1]
    for i in range(len(s)):
        if s[i] != reverseS[i]:
            check = False

    return check


def checkPseudoPalindrome(s):
    check = True
    start, end = 0, len(s) - 1
    cnt = 0
    while start <= end:
        if s[start] == s[end]:
            pass
        else:
            if s[start + 1] == s[end] and s[start] == s[end - 1]:
                if s[start + 2] == s[end - 1] and s[start + 1] != s[end - 2]:
                    cnt += 1
                    start += 1
                elif s[start + 2] != s[end - 1] and s[start + 1] == s[end - 2]:
                    cnt += 1
                    end -= 1
            elif s[start + 1] == s[end]:
                cnt += 1
                start += 1
            elif s[start] == s[end - 1]:
                cnt += 1
                end -= 1
            else:
                check = False
        start += 1
        end -= 1

    if cnt > 1:
        check = False

    return check


for _ in range(n):
    s = input().rstrip()
    if checkPalindrome(s):
        print(0)
        continue
    elif checkPseudoPalindrome(s):
        print(1)
        continue
    else:
        print(2)

