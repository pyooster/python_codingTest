# 숫자 야구
import sys

si = sys.stdin.readline

n = int(si())

# preprocess
nums = []
for i in range(123, 988):
    num = str(i)
    # 0 이 존재하거나, 같은 숫자가 반복되어 나오는 경우 제외
    if '0' not in num and len(set(num)) == 3:
        nums.append(num)


def check(test, num, strike, ball):
    strike_count = 0
    for i in range(3):
        if str(test)[i] == str(num)[i]:
            strike_count += 1

    ball_count = 0
    for s in test:
        if s in num:
            ball_count += 1

    ball_count -= strike_count

    return (strike_count == strike) and (ball_count == ball)


for _ in range(n):
    test, strike, ball = map(int, si().split())
    test = str(test)

    new_nums = []
    for num in nums:
        if check(test, num, strike, ball):
            new_nums.append(num)
    nums = new_nums

print(len(nums))
