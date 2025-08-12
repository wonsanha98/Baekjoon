def solution(numLog):
    answer = ''
    start = numLog[0]
    for i in range(1, len(numLog)):
        if numLog[i] == start + 1:
            answer += 'w'
        elif numLog[i] == start - 1:
            answer += 's'
        elif numLog[i] == start + 10:
            answer += 'd'
        elif numLog[i] == start - 10:
            answer += 'a'
        start = numLog[i]

    return answer