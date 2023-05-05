import sys

input = sys.stdin.readline
 

def check():
    pos = -1
    while 1:
        try:
            if stack[pos] != boom[pos]:
                return False
        except Exception:
            if pos == -length - 1:
                return True
            return False
        pos -= 1


str = input().rstrip()
boom = input().rstrip()
length = len(boom)
stack = []
for i in str:
    stack.append(i)
    if check():
        for _ in range(length):
            stack.pop()


if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
