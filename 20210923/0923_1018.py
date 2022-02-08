# (4)번

# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다. 
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 
# 지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.

# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
# 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
# 당연히 8*8 크기는 아무데서나 골라도 된다. 
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 입력 예시
# 10 13
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB

# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW


from multiprocessing import Process, Queue

DEFAULT_SIZE = 8

def get_least(nIdxCol: int, tplSize: tuple, lstBoard: list, q: Queue) -> None:
    n_retry: int = tplSize[0] - DEFAULT_SIZE + 1 #프로세스에서 반복할 횟수 - row
    n_count: int
     
    # 시작 타일 W
    for idx_row in range(n_retry):
        n_count = 0
        for row in range(idx_row, idx_row+DEFAULT_SIZE):
            for column in range(nIdxCol, nIdxCol+DEFAULT_SIZE):

                if (
                    (row + column) % 2 == 0
                    and lstBoard[row][column] != 'W'
                    or (row + column) % 2 != 0
                    and lstBoard[row][column] != 'B'
                ):
                    n_count += 1

        q.put(min(n_count, 64-n_count)) # 시작 타일이 W인경우와 B인경우 칠할 칸수의 합은 64


def solution(tplSize: tuple, lstBoard: list) -> int:
    n_processes: int = tplSize[1] - DEFAULT_SIZE + 1
    q = Queue(maxsize=tplSize[0]*tplSize[1]) # 반환값 받아올 큐

    lst_process = [ 
        Process(target=get_least, args=(idx, tplSize, lstBoard, q)) 
        for idx in range(n_processes) 
    ]

    for worker in lst_process:
        worker.start()

    for worker in lst_process:
        worker.join()

    lst_q = []
    while not q.empty():
        lst_q.append(q.get())
    
    return min(lst_q)


if __name__ == '__main__':
    tpl_size = tuple(map(int, input().split()))
    lst_board = [ input() for _ in range(tpl_size[0]) ]

    print(solution(tpl_size, lst_board))




