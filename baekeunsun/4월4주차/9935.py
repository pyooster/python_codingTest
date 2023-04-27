# 문자열 폭발
string = input()
bomb = input()

stack = []
length = len(bomb)
lastChar = bomb[-1]

for char in string:
    stack.append(char)
    if char == lastChar :
        if ''.join(stack[-length:]) == bomb:
            del stack[-length:]
    
if not stack :
    print("FRULA")
else :
    print(''.join(stack))
