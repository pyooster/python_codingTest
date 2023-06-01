import re


def solution(new_id):
    # 1단계: 소문자로 치환
    new_id = new_id.lower()

    # 2단계: 알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자 제거
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    # 3단계: .가 2번 이상 연속된 부분을 하나의 .로 치환
    new_id = re.sub('\.+', '.', new_id)

    # 4단계: 문자열의 앞뒤에 위치한 . 제거
    new_id = new_id.strip('.')

    # 5단계: 빈 문자열 이라면 a를 대입
    if new_id == '':
        new_id = 'a'

    # 6단계: 길이가 16자 이상이면 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')

    # 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id
