def solution(my_string, overwrite_string, s):
    overwrite_len = len(overwrite_string)
    answer = my_string[:s] + overwrite_string[:overwrite_len] + my_string[s + overwrite_len:]
    return answer