# 주사위

N = int(input())
arr = list(map(int, input().split()))

dice = [0, 0, 0]
dice[0] = min(arr[0], arr[5])
dice[1] = min(arr[1], arr[4])
dice[2] = min(arr[2], arr[3])
dice.sort()
# print(dice)

if N != 1:
    num1 = dice[0]
    num2 = dice[0] + dice[1]
    num3 = dice[0] + dice[1] + dice[2]

    edge = 4                             # 모서리 4개
    side2 = (N-1)*4 + (N-2)*4            # 세로 기둥 4개 윗면 모서리 빼고 4개
    side1 = (N-1)*(N-2)*4 + (N-2)**2     # 나머지 4개 윗면 가운데
    ans = side1 * num1 + side2 * num2 + edge * num3
    print(ans)
else:
    ans = sum(arr) - max(arr)
    print(ans)