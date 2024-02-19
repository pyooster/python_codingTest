from string import ascii_lowercase
from itertools import combinations

n, k = map(int, input().split())
k -= 5

remains = {'a', 'c', 'i', 'n', 't'}
alpha = {*ascii_lowercase} - remains
if k < 0:
    print(0)
    exit()

mx = 0

strset = [{*input()} for _ in range(n)]
for c in combinations(alpha, k):
    tmp = 0
    remains = remains | {*c}
    for s in strset:
        if remains.issuperset(s):
            # print(remains, *c)
            tmp += 1

    remains = remains - {*c}
    mx = max(mx, tmp)
print(mx)