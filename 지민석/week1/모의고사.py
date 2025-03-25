def solution(answers):
    #1번 수포자는 1,2,3,4,5..
    #2번 수포자는 2,1,2,3,2,4,2,5,...
    #3번 수포자는 3,3,1,1,2,2,4,4,5,5,...

    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]

    length = len(answers)

    answer = [0,0,0]

    for i in range(0,length):

        if student1[i%5]==answers[i]:
            answer[0]+=1
        if student2[i%8]==answers[i]:
            answer[1]+=1
        if student3[i%10]==answers[i]:
            answer[2]+=1
    max_value = max(answer)
    return_list = []

    for i in range(3):
        if max_value == answer[i]:
            return_list.append(i+1)



    return return_list