def solution(my_string):
    answer = ''
    for x in my_string:
        if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u':
            answer += x
    return answer


def solution(my_string):
    answer = ''
    for x in my_string:
        if x not in 'aeiou':
            answer += x
    return answer