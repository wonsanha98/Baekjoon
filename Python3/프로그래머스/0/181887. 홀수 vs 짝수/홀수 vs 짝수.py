def solution(num_list):
    answer = []
    for i in range(0, len(num_list), 2):
        answer.append(num_list[i])
    print(answer)

    if sum(answer) >= sum(num_list) - sum(answer):
        return sum(answer)
    else:
        return sum(num_list) - sum(answer)