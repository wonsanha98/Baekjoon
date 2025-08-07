def solution(names):
    answer = []
    name_cnt = len(names)
    index = 0
    answer.append(names[index])
    
    if name_cnt % 5 == 0:
        name_cnt = name_cnt // 5
        name_cnt -= 1
    else:
        name_cnt = name_cnt // 5
    
    for _ in range(name_cnt):
        index += 5
        answer.append(names[index])
    
    return answer