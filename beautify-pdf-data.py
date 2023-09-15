data_dump = """2
1
2
1
6 10
6
9
5
1
6
5
1
8
8 10
2
5
9
3
1 10
6
6
5
1
3
6
5
2
9
9
9
4
5
1
2
6
2 10
2
7
3
1
5
8
6
9
1
1
6
5
7 10
8
2
4
4
2
1
2
6 10
6
8
5
5
3
5 10
8
3
2
1
6
2 10 10
1
5
4
1
4
5 10
4
7
7
4
6
8
5
7
3
2
3
1
9
9
1
4
1
4
4
9
5
3
1
4
9
5
3
9
5
2
9
3
1
7
2
2
6
1
2
6
7
6
6
8
5
5
1
6
9
9
1
1
1
3
8 10
2
1
3
2
6 10
8
5
5
7
1
4 10
2
2
2
1
4
9
5
6
5
6
4
8
2
7
9
7
9
2
2
5
9
6
1
2
6
4
1
5
8
4
1
9
2
2
8 10
4
4
2
5
4 10
3
3
8
4
7
6
4
6
4
2
1
3
1
5
9
8
4
3
5
9
8 10
2
5
6
2
2 10
7
4
2
1
5
1
8 10
6
5
3
9
3
6
5
3
9
1
2
7
9
7
5
3
2
1
2
9
9
6
6
6
1
5
2 10"""

d = data_dump.replace("\n", " ").split(" ")

data_low2high = []
data_high2low = []

# shape:
# 5 leftmost are l2h
# first 8 cols rows have 8 rows, others have 7

cutoff = 8*8  # differing amount of data
l2h = 0

for i, n in enumerate(d):
    if l2h < 5:
        data_low2high.append(n)
    else:
        data_high2low.append(n)
    if i >= cutoff:
        l2h += 1
        if l2h == 7:
            l2h = 0
    else:
        l2h += 1
        if l2h == 8:
            l2h = 0

# print(data_high2low)
data_l2h_sorted = []
for i in range(5):
    m = 0
    while m * 5 + i < len(data_low2high):
        data_l2h_sorted.append(data_low2high[m * 5 + i])
        m += 1

with open("low-to-high-data3.txt", "w") as f:
    f.write(" ".join(data_l2h_sorted))

# print(data_high2low)
data_h2l_sorted = []
cutoff = 8 * 3
for i in range(3):
    m = 0
    idx = i
    while idx < len(data_high2low):
        data_h2l_sorted.append(data_high2low[idx])
        m += 1
        if m > 8:
            if i == 2:
                break
            idx += 2
        else:
            idx += 3

data_h2l_sorted = data_h2l_sorted[:-1]

with open("high-to-low-data4.txt", "w") as f:
    f.write(" ".join(data_l2h_sorted))


