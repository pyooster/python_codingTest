# 조 짜기
import sys

si = sys.stdin.readline

# 가급적 실력차이가 많이 나도록 조를 편성하는 것이 유리
# 나이 차이가 많이 날 경우에는 오히려 부정적인 효과
# -> 연속된 학생들을 모두 같은 조에 포함시켜야 한다는 뜻(1과 9가 같은 조애 속해있다면, 그 사이에 있는 3, 4, 8, 6 도 모두 1, 9와 같은 조에 속해야 함
# 따라서 선생님들은 우선 나이 순서대로 정렬 후 적당히 학생들을 나누기로 함, 조의 개수는 상관x
# 각각의 조가 잘 짜여진 정도: 그 조에 속해있는 가장 점수가 높은 학생과 가장 낮은 학색의 점수 차이
# 각 조의 잘 짜여진 정도의 합의 최댓값을 구하자. (조에 한명만 속하면 합이 0)
n = int(si())
# 나이 순으로 정렬된 학생들의 점수
arr = list(map(int, si().split()))
# 2 5 7 1 3 4 8 6 9 3
# (2, 5), (7, 1), (3, 4, 8) (6, 9, 3)
# 3 + 6 + 5 + 6 = 20 (최대)

# dp[i] := i 번째 학생까지 고려했을때 조가 잘 짜여진 정도의 최댓값,

dp = [-sys.maxsize] * 1001
# 기저 조건
dp[0] = 0

# n ^ 2 -> 1000 x 1000 ㅆㄱㄴ
for i in range(1, n):
    # i번 학생을 새로운 조에 넣거나
    # 이전 조에 포함
    # min, max_score 를 현재 위치의 학생의 점수로 초기화
    min_score = max_score = arr[i]
    for j in range(i, -1, -1):
        # 현재 i 부터 0번 위치까지 탐색하여 가장 큰 값과 가장 작은 값을 찾아냄
        min_score = min(min_score, arr[j])
        max_score = max(max_score, arr[j])
        # j 가 0보다 클 경우
        if j > 0:
            # j - 1 번 위치의 학생까지 고려했을때 최댓값에 max_score - min_score 로 이뤄진 팀의 차이를 더함
            dp[i] = max(dp[i], dp[j - 1] + max_score - min_score)
        # j 가 0 일 경우
        else:
            dp[i] = max(dp[i], max_score - min_score)

print(dp[n - 1])
