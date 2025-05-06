import re

def solution(new_id):
    # 1단계: 소문자 치환
    new_id = new_id.lower()
    
    # 2단계: 알파벳 소문자, 숫자, '-', '_', '.' 제외한 문자 제거
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    
    # 3단계: 연속된 마침표를 하나로
    new_id = re.sub('\.+', '.', new_id)
    
    # 4단계: 처음과 끝의 마침표 제거
    new_id = new_id.strip('.')
    
    # 5단계: 빈 문자열이면 'a' 대입
    if not new_id:
        new_id = 'a'
    
    # 6단계: 길이가 16자 이상이면 첫 15자만, 끝에 마침표 제거
    new_id = new_id[:15].rstrip('.')
    
    # 7단계: 길이가 2자 이하라면 마지막 문자 반복
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
