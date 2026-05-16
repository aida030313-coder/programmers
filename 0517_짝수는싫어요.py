def solution(n):
    answer = []
    for i in range(n + 1):
        if i % 2 == 1:
            answer += [i]
    return answer


def solution(n):
    return list(range(1, n + 1, 2))
    # 1부터 n+1 직전까지 2칸씩 건너뛰며 가져와라