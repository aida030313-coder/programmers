def solution(money):
    coffee = money // 5500
    change = money % 5500
    answer = [coffee, change]
    return answer

def solution(money):
    answer = [money // 5500, money % 5500]
    return answer