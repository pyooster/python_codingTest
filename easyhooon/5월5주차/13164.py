# 행복 유치원

# 키 순서대로 일렬로 세우고 k 개의 조로 나눔
# 각 조에는 원생이 최소 한명, 같은 조에 속한 원생들은 서로 인접
# 조마다 티셔츠를 맞추는 비용 = (가장 키가 큰 원생 - 가장 키가 작은 원생), 혼자면 비용이 없나보다
# 티셔츠를 만드는 비용의 합을 최소로
# 원생의 수 <= 30만 -> 2중 포문 불가능
# 처음 부터 정렬 되어 입력 됨
# 5 3
# (1, 3), (5, 6) 10
# 2 + 1 = 3
# 2 2 1 4
# 3 팀으로 나눴다 -> 2 지점을 택해서 잘랐다
import sys

si = sys.stdin.readline

n, k = map(int, si().split())

nums = list(map(int, si().split()))

diff = []

for i in range(1, n):
    diff.append(nums[i] - nums[i - 1])

diff.sort()

answer = 0
for i in range(n - k):
    answer += diff[i]

print(answer)