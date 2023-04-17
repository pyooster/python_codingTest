# 펠린드롬?
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
hong = list(map(int,input().split(' ')))
dp = list([-2]*N for _ in range(N))

def palindrome(start,end):
    if dp[start][end] != -2 :
        return(dp[start][end])
    
    if start == end :
        return 1
    
    if hong[start] == hong[end] :
        if start + 1 == end :
            return 1
        else :
            dp[start][end] = palindrome(start+1,end-1)
            return(dp[start][end])
    else :
        return 0

                
for _ in range(int(input())):
    start,end = map(int,input().split(' '))
    print(palindrome(start-1,end-1))
