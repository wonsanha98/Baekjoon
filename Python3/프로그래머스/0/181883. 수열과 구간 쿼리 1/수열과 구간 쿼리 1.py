import copy

def solution(arr, queries):
    answer = arr
    for i in range(len(queries)):
        for j in range(len(arr)):
            if queries[i][0] <= j and j <= queries[i][1]:
                answer[j] += 1
                
    return answer