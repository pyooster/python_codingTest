# 빗물
H, W = map(int,input().split(' '))
block = list(map(int,input().split(' ')))
answer = 0

for i in range(1,len(block)-1):
    left = max(block[:i])
    right = max(block[i+1:])

    wall = min(left,right)

    if wall > block[i]:
        answer += wall - block[i]

print(answer)
