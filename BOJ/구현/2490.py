# 윷놀이
lst = [list(map(int, input().split())) for _ in range(3)]
for i in lst:
    if i.count(0) == 1: print('A')
    elif i.count(0) == 2: print('B')    
    elif i.count(0) == 3: print('C')
    elif i.count(0) == 4: print('D')
    else: print('E')