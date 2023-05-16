from itertools import permutations

t = int(input())
nums = list(permutations([1,2,3,4,5,6,7,8,9],3))

for _ in range(t):
    guess, strike, ball = map(int,input().split())
    guess = list(str(guess))
    checked = []
    removed_cnt = 0
    
    for num in nums:
        b = 0
        s = 0

        for n in range(3):
            if str(num[n]) in guess:
                if n == guess.index(str(num[n])): # 위치까지 같으면
                    s += 1 # strike 올려줌
                else: # 위치는 다르면
                    b += 1 # ball 추가
        
        if s != strike or b != ball:
            checked.append(num)

        nums = set(nums) - set(checked)
        nums = list(nums)
            
print(len(nums))