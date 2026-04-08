def solution(n, k):
    food = n * 12000
    drink = (k - (n//10)) * 2000
    answer = food + drink
    return answer