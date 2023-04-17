import sys

sys.setrecursionlimit(10**4)
si = sys.stdin.readline

# dp[i][j] := 배열의 시작 인덱스를 i, 끝 인덱스를 j 라고 할 때, arr[i,,,j]가 펠린드롬 수 인지(1) 아닌지(0)

n = int(si())
arr = [0] + list(map(int, si().split()))
dp = [[-1] * (n + 1) for _ in range(n + 1)]
m = int(si())

# 기저조건 모든 dp[i][i] 는 펠린 드롬
# for i in range(1, n + 1):
#     dp[i][i] = 1

# 2 개도 채울 수 있지 않나? -> 같으면 1, 다르면 0
# for i in range(1, n):
#     if arr[i] == arr[i + 1]:
#         dp[i][i + 1] = 1
#
#     else:
#         dp[i][i + 1] = 0

# 바로 직전의 상황을 통해 판단 n, n - 1
# 구간 [s, e] 의 펠린드롬을 판별하기 위해 구간 [s + 1, e - 1] 의 펠린드롬 판별 결과를 이용(저장하고 있음)
# 재귀스럽다 -> 메모이제이션을 쓰는게 더 자연스러운 문제 같기도 하다...
# 근데 메모이제이션을 사용하는 풀이에 약하다.

# for i in range(1, n):
#     for j in range(i, n + 1):
#         if dp[i + 1][j - 1] == 1 and arr[i] == arr[j]:
#             dp[i][j] = 1

# 이건 다 채워버린 다음에 쿼리를 하나씩 푸는 문제인듯
# 홀 수 일때, 짝 수 일 때
#   1  2  1  3  1  2  1
# 1 1  0  1  0  0  0  1
# 2    1  0  0  0  1  0
# 1       1  0  1  0  0
# 3          1  0  0  0
# 1             1  0  1
# 2                1  0
# 1                   1

# 채워봤을때 보이는 규칙
# 펠린드롬 이전의 수는 펠린드롬이 아니다. 물론 모두 같은 수라면 말이 다르겠지

# 짝수, 홀수를 나눠서 풀 필요가 없다.
def memo(i, j):
    # 홀수의 기저 조건
    # 기저 조건 1, 2, 3...
    if i == j:
        return 1

    # 짝수의 기저 조건
    # 두자리 수 일 경우 11, 22, 33...
    elif i + 1 == j:
        if arr[i] == arr[j]:
            return 1
        else:
            return 0

    # 판단을 이전에 하였다면 (memoization)
    if dp[i][j] != -1:
        return dp[i][j]

    # 처음 인덱스의 값과 끝 인덱스의 값이 다르면
    if arr[i] != arr[j]:
        dp[i][j] = 0
    # 같으면 펠린드롬인지 검사해봄
    else:
        dp[i][j] = memo(i + 1, j - 1)

    return dp[i][j]


# 메모이제이션 풀이법은 먼저 전부를 채우는 방식이 아니다.

for _ in range(m):
    s, e = map(int, si().split())
    print(memo(s, e))