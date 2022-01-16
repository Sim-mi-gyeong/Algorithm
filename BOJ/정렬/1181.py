# 단어 정렬

words = []
for i in range(int(input())):
    s = input()
    if s not in words:
        words.append(s)
words.sort(key=lambda x : (len(x),x) )
for i in words: print(i)