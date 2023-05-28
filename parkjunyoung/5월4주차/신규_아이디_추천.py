# 신규 아이디 추천

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()

    # 2
    check = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
             'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.']
    step2 = []
    for i in new_id:
        if i in check:
            step2.append(i)
    new_id = ''.join(step2)

    # 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4
    if new_id[0] == '.':
        if len(new_id) > 1:
            new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5
    if new_id == '':
        new_id = 'a'

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1] * (3 - len(new_id))

    answer = new_id
    return answer