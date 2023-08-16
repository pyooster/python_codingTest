"""
    Solution code for "BaekJoon 여러분의 다리가 되어 드리겠습니다!".

    - Problem link: https://www.acmicpc.net/problem/17352

    입력
        - 섬의 개수 : (2 ≤ N ≤ 300,000)
        - 다리의 개수 : N - 2

    출력
        - 연결해야하는 1개의 다리
"""
from sys import stdin as input
# input = open('./test4.txt')

island_count = int(input.readline())
parent = [i for i in range(island_count + 1)]


def find(node: int) -> int:
    if parent[node] == node:
        return parent[node]

    parent[node] = find(parent[node])
    return parent[node]


def union(node1: int, node2: int) -> None:
    parent1, parent2 = find(node1), find(node2)
    if parent1 > parent2:
        parent[parent1] = parent[parent2]
    else:
        parent[parent2] = parent[parent1]


def main() -> None:
    for _ in range(island_count - 2):
        node1, node2 = map(int, input.readline().split())
        union(node1, node2)

    answer = {find(parent[node]) for node in range(1, len(parent))}
    print(*answer)


if __name__ == '__main__':
    main()