def solution(my_string):
    answer = []
    temp = []

    for ch in my_string:
        if ch != ' ':
            temp += ch
        else:
            if temp:
                answer.append("".join(temp))
                temp = []
                
    if temp:
        answer.append("".join(temp))

    return answer