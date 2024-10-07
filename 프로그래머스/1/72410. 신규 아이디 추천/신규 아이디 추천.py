def solution(new_id):
    answer = ''
    # 1단계: 대문자를 소문자로 치환
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']
    
    # 대문자 -> 소문자로 치환
    for i in new_id:
        answer += i.lower() if i.isupper() else i

    # 2단계: 허용된 문자만 남기기
    new_id = ''
    for i in answer:
        if i in x:
            new_id += i

    # 3단계: 연속된 마침표 처리
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계: 처음이나 끝에 있는 마침표 제거
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]

    # 5단계: 빈 문자열인 경우 "a" 대입
    if not new_id:
        new_id = 'a'

    # 6단계: 길이가 16자 이상이면 15자로 줄이기
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]

    # 7단계: 길이가 2자 이하인 경우 마지막 문자 반복
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
