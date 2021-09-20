# 5주차_모음사전
# https://programmers.co.kr/learn/courses/30/lessons/84512

def _solution(word):
    dct_idx = { 
        'A':0, 
        'E':1, 
        'I':2, 
        'O':3, 
        'U':4,
    }
    
    answer = len(word)
    n_unit_count = (((5 + 1)*5 + 1)*5 + 1)*5 + 1
    for c_letter in word:
        answer += n_unit_count * dct_idx[c_letter]
        n_unit_count = (n_unit_count - 1) // 5
        
    return answer

    

if __name__ == '__main__':
    print(((((5 + 1)*5 + 1)*5 + 1)*5 + 1)*5)
    print(_solution('UUUUU'))