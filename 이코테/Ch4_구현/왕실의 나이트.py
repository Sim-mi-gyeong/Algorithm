import time
start_time = time.time()
string = input()
row = int(string[1])
col_old = string[0]
col_str = [i for i in 'abcdefgh']
col_int = [i for i in range(1,9)]   # -> col_int[col_str.index(col)]]
col = col_int[col_str.index(col_old)]

cnt = 0
# 이동방법
path1 = {'l_u' : [-2, -1], 'l_d': [-2, 1], 'r_u': [2, -1], 'r_d' : [2, 1]}   # 수평(col) 2 / 수직(row) 1
path2 = {'l_u' : [-1, -2], 'l_d': [-1, 2], 'r_u': [1, -2], 'r_d' : [1, 2]}  # 수평 1 / 수직 2
for i in path1.values():
    if row + i[1] < 1 or row + i[1] > 8 or col + i[0] < 1 or col + i[0] > 8:
        continue
    else:
        cnt += 1

for i in path2.values():
    if row + i[1] < 1 or row + i[1] > 8 or col + i[0] < 1 or col + i[0] > 8:
        continue
    else:
        cnt += 1
end_time = time.time()
print(cnt)
print('걸린 시간 : ', end_time - start_time)