import sys

# 주사위를 적절히 회전시키고 쌓아서, N x N x N 크기의 정육면체를 만들려고 함
# 이 정육면체는 5개 면만 보인다.
# 보이는 5개의 면에 쓰여있는 수의 합의 최솟값을 출력하는 프로그램을 작성
# 바닥에 닿는 면은 따로 체크 필요

# 바닥에 닿지 않는 케이스
# 모서리, 꼭짓점, 면
# 면 -> 항상 가장 작은 숫자 * (n-2) * (n-2) * 5
# 모서리 -> 두 수의 합이 제일 적은 쪽으로 * (n-2) * 8
# 꼭짓점 -> 세수의 합이 가장 작은 쪽으로 * 4

# 바닥에 닿는 케이스
# 모서리 -> 가장 작은 수 * (n-2) * 4
# 꼭지점 -> 두 수의 합이 제일 적은 쪽으로 * 4

# A B C D E F
# 1 2 3 4 5 6

# 만나는 면 모음
# A, D, E -> 1 + 4 + 5 = 10
# A, C, E -> 1 + 3 + 5 = 9
# A, B, D -> 1 + 2 + 4 = 7
# A, B, C -> 1 + 2 + 3 = 6
# B, D, F -> 2 + 4 + 6 = 12
# B, C, F -> 2 + 3 + 6 = 11
# D, E, F -> 4 + 5 + 6 = 15
# C, E, F -> 3 + 5 + 6 = 14

# 예제 1
# (4 * 6) + (3 * 4) = 36

# 예제 2
# (1 * 5) + (3 * 8) + (6 * 4) + (1 * 4) + (3 * 4) = 5 + 24 + 24 + 4 + 12 = 69

# 알아야 할 것
# 가장 작은 수
# 가장 작은 두 수의 합
# 가장 작은 세수의 합

# 이게 안되는게 가장 작은 두개의 합, 가장 작은 세개의 합을 못 만들 수 도 있기 때문
# 가능한 조합 중에서 가장 작은 걸 찾고 아래 식을 돌려야 함
# 가능한 조합 인덱스 찾기
# 내가 생각한 수식보다 더 작은 경우의 수일 때가 존재하는건가

# AE, AD, AB, AC, DB, DE, DF, CE, CB, CF, EF, BF
# (0,4) (0,3) (0,1) (0,2) (1,3), (3,4), (3,5), (2,4), (2,3), (2,5), (4,5), (1,5)

# A, D, E -> 1 + 4 + 5 = 10, 0, 3, 4
# A, C, E -> 1 + 3 + 5 = 9, 0, 2, 4
# A, B, D -> 1 + 2 + 4 = 7, 0, 1, 3
# A, B, C -> 1 + 2 + 3 = 6, 0, 1, 2
# B, D, F -> 2 + 4 + 6 = 12, 1, 3, 5
# B, C, F -> 2 + 3 + 6 = 11, 1, 2, 5
# D, E, F -> 4 + 5 + 6 = 15, 3, 4, 5
# C, E, F -> 3 + 5 + 6 = 14, 2, 4, 5


si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
min_num = sorted(arr)[0]
min_two_sum = min(arr[0] + arr[4], arr[0] + arr[3], arr[0] + arr[1], arr[0] + arr[2], arr[1] + arr[3], arr[3] + arr[4],
                  arr[3] + arr[5], arr[2] + arr[4], arr[1] + arr[2], arr[2] + arr[5], arr[4] + arr[5], arr[1] + arr[5])
min_three_sum = min(arr[0] + arr[3] + arr[4], arr[0] + arr[2] + arr[4], arr[0] + arr[1] + arr[3],
                    arr[0] + arr[1] + arr[2],
                    arr[1] + arr[3] + arr[5], arr[1] + arr[2] + arr[5], arr[3] + arr[4] + arr[5],
                    arr[2] + arr[4] + arr[5])

# print(min_num, min_two_sum, min_three_sum)

# 밑의 점화식은 n >= 2 이상일때에 해당
# n == 1 일때를 고려해줘야 함

if n == 1:
    answer = sum(sorted(arr)[:len(arr) - 1])
else:
    answer = 0
    answer += min_num * (n - 2) * (n - 2) * 5
    answer += min_two_sum * (n - 2) * 8
    answer += min_three_sum * 4
    answer += min_num * (n - 2) * 4
    answer += min_two_sum * 4

print(answer)
