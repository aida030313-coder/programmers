def solution(n):
    for i in range(1001):
        if i ** 2 == n:
            return 1
    return 2


def solution(n):
    if int(n ** 0.5) ** 2 == n:
        return 1
    else: 
        return 2