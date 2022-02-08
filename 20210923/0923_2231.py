# (2)번
#백준 2231번 분해합 구하기

# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라한다. 
# 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 
# 따라서 245는 256의 생성자가 된다. 
# 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 
# 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

def solution(nInput: int) -> int:
    # 9*6 = 최대 54번 전부터 생성자가 발생할 수 있음
    n_constructor = nInput-54 if nInput > 54 else 0

    for i in range(54):
        n_result = n_constructor + sum(map(int,str(n_constructor)))

        if n_result == nInput: return n_constructor

        n_constructor += 1

        #인풋이 54보다 작았던 경우 탈출
        if nInput - i < 0: break
    
    return 0


if __name__ == '__main__':
    print(solution(int(input())))
