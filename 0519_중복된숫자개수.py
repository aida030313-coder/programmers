def solution(array, n):
    duplicate = []
    for i in array:
        if i == n:
            duplicate += [i]
    return len(duplicate)