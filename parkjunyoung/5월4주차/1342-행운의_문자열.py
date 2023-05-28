# 행운의 문자열

S = list(input())
cnt = len(S)
alphabet = [0 for _ in range(26)]
ans = 0

for i in range(cnt):
    alphabet[ord(str(S[i])) - 97] += 1


def back(a, b):
    global ans
    if a == cnt:
        ans += 1
    for i in range(26):
        if alphabet[i] > 0 and i != b:
            alphabet[i] -= 1
            back(a+1, i)
            alphabet[i] += 1
        else:
            pass


back(0, -1)
print(ans)