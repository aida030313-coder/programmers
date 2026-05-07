def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
        # isdigit() 오직 숫자로 구성되어있는지 아닌지 확인하는 매소드
        # true/false로 반환된다.
            answer += int(i)   # 문자열 안의 숫자는 '글자' 형태이기 때문에 숫자로 변환 필요
    return answer