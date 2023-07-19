# binary 라는 이진수의 L번지 부터 R번지 까지가 올바르게 포화 이진트리로 표현되느냐?
def solve(binary, L, R):
    if L == R:
        return True

    mid = (L + R) // 2
    root = binary[mid]

    left_child = binary[(L + (mid - 1)) // 2]
    right_child = binary[((mid + 1) + R) // 2]

    if left_child == '1' and root == '0':
        return False

    if right_child == '1' and root == '0':
        return False

    return solve(binary, L, mid - 1) and solve(binary, mid + 1, R)


def solution(numbers):
    answer = []

    for elem in numbers:
        binary = bin(elem)[2:]
        tree_size = 1

        while tree_size < len(binary):
            tree_size = tree_size * 2 + 1

        binary = '0' * (tree_size - len(binary)) + binary

        if solve(binary, 0, len(binary) - 1):
            answer.append(1)
        else:
            answer.append(0)

    return answer
