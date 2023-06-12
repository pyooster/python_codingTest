from re import sub


def solution(new_id):
    # 1 단계
    new_id = new_id.lower()
    # 2 단계
    new_id = sub("[^a-z0-9\-\_\.]", "", new_id)
    # 3 단계
    new_id = sub("\.+", ".", new_id)
    # 4 단계
    new_id = sub("^\.|\.$", "", new_id)
    # 5 단계
    if len(new_id) == 0:
        new_id = "a"
    # 6 단계
    new_id = new_id[:15]
    new_id = sub("\.$", "", new_id)
    # 7 단계
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id
