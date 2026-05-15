def solution(s1, s2):
    answer = 0
    for a in s1:
        for b in s2:
            if a == b:
                answer += 1
    return answer


def solution(s1, s2):
    answer = 0
    for a in s1:
        if a in s2:
            answer += 1
    return answer