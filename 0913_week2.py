# 2주차_상호평가
# https://programmers.co.kr/learn/courses/30/lessons/83201

# No.      0     1       2     3    4
# 0	     100    90      98    88   65
# 1	     50     45      99    85   77
# 2	     47     88      95    80   67
# 3	     61     57      100   80   65
# 4      24     90      94    75   65
# 평균	45.5    81.25   97.2  81.6 67.8
# 학점    F      B       A     B    D

def solution(scores):
    answer: str = ''
    n_students: int = len(scores)
    
    for idx in range(n_students):
        lst_individual_scores: list = [ lst_score[idx] for lst_score in scores ]
        n_self_score: int = lst_individual_scores[idx]

        # 결과에 영향이 미치는 경우
        # 1. 유일한 최고/최소점을 자기자신에게 부여하여 결과에 영향을 미치는 경우 
        if ( lst_individual_scores.count(n_self_score) == 1 and (max(lst_individual_scores) == n_self_score or min(lst_individual_scores) == n_self_score)):
            try:
                # 리스트에서 제거하는 것 보다 빠름
                f_avg = ( sum(lst_individual_scores) - n_self_score ) / ( n_students-1 )
            except ZeroDivisionError as ze:
                print(ze)
                f_avg = -1

        else:
            f_avg = sum(lst_individual_scores)/n_students

        #결과 할당
        if   f_avg >= 90: answer += 'A'
        elif f_avg >= 80: answer += 'B'        
        elif f_avg >= 70: answer += 'C'
        elif f_avg >= 50: answer += 'D'
        else:             answer += 'F'
    
    return answer