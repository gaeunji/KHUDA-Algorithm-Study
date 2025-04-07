import re
def solution(new_id):
    answer = ''
    
    # Step 1
    new_id = new_id.lower()
    # step 2
    for char in new_id:
        if char.isalpha() or char.isdigit() or char in ['-', '_', '.']:
            answer += char
    # Step 3
    answer = re.sub(r'\.+', '.', answer)

    
    # Step 4
    if answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    # Step 5
    if answer == '':
        answer = 'a'
    # Step 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # step 7
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]
    
    return answer
