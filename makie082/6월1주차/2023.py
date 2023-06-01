n = int(input()) # n자리수

def checkSosu(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == n: # n자리 수이면
        print(num)
        return
    for i in range(1,10,2):
        if checkSosu(num*10+i):
            dfs(num*10+i)
    return

for a in [2,3,5,7]:
    dfs(a)