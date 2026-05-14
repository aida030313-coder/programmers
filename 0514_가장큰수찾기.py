def solution(array):
    biggest = max(array)
    position = array.index(biggest)
    return [biggest, position]