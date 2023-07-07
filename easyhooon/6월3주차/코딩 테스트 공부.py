# 각 문제마다 문제를 풀면 올라가는 알고력과 코딩력이 정해져 있음
# 같은 문제를 여러번 푸는 것이 가능
# 주어진 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단 시간을 구하려 함
# 모든 문제를 풀 수 있는 능력치에 도달하면 종료
# 마지막 문제를 푸는 시간을 더할 필요 없음
# 백트래킹 -> 메모이제이션 dp
# 알고력을 높이기 위해 알고 공부를 하냐, 코딩력을 높이기 위해 코딩 공부를 하냐
# 풀 수 있는 문제를 풀어 알고, 코딩력 모두를 올리냐 선택해서 최단 시간을 구하라
# 동일한 상태를 정의 하기 위한 요소
# 현재까지 고려한 위치(시간)
# 알고력
# 코딩력
# dp[i][j]:= 알고력 i, 코딩력이 j 를 도달하기 위한 최단 시간
# 기저 조건 dp[alp][cop] = 0
# 최소를 구하는 문제이므로 최대로 모든 배열을 초기화 시킴

# 알고리즘을 공부하여 알고력을 1 높이는 경우:
# dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)

# 코딩을 공부하여 코딩력을 1 높이는 경우:
# dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)

# 문제 하나를 선택하여 알고력과 코딩력을 높이는 경우:
# dp[i+alp_rwd][j+cop_rwd] =
# min(dp[i + alp_rwd][j + cop_rwd], dp[i][j] + cost) (단, i >= alp_req 이고 j >= cop_req)

import sys

INT_MAX = sys.maxsize


# alp, cop <= 150
# problem <= 100
# alp_req, cop_req <= 150
# alp_rwd, cop_rwd <= 30
# cost <= 100
def solution(alp, cop, problems):
    # 문제 중 최대 알고력
    max_alp = sorted(problems, reverse=True, key=lambda x: (x[0]))[0][0]
    # 문제 중 최대 코딩력
    max_cop = sorted(problems, reverse=True, key=lambda x: (x[1]))[0][1]

    # print(max_alp, max_cop)

    # dp[i][j]:= 알고력 i, 코딩력이 j 를 도달하기 위한 최단 시간
    dp = [[INT_MAX] * (max_cop + 1) for _ in range(max_alp + 1)]

    # 목표 알고력
    alp = min(alp, max_alp)
    # 목표 코딩력
    cop = min(cop, max_cop)

    # print(alp, cop)

    # 기저 조건
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 알고리즘 공부
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)

            # 코딩 공부
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            # 문제 풀이
            for (alp_req, cop_req, alp_rwd, cop_rwd, cost) in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp, next_cop = min(max_alp, i + alp_rwd), min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

    return dp[max_alp][max_cop]

# print(solution(0, 0, [[0, 0, 30, 2, 1], [150, 150, 30, 30, 100]]))
