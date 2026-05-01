def solution(num_list):
    num_list.reverse()   # .reverse()는 .앞의 배열 자체를 뒤집어버림
    return num_list      # .reverse()로 뒤집어진 num_list 출력


def solution(num_list):
    answer = list(reversed(num_list))
    # reversed(배열)로 뒤집은 결과를 list()로 다시 리스트에 담아줘야함
    return answer


