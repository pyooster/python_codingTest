from bisect import bisect_left
res = [-1]
s = list()
for i in range(k:=int(input())):
    s.append(int(input()))

for i in range(k):
    if s[i] < res[-1]:
        res[bisect_left(res, s[i])] = s[i]
    
    else:
        res.append(s[i])

print(k - (len(res) - 1))