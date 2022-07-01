import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
dl_graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
lst_visited = [False] * (n + 1)

# 그래프에 있는 모든 노드들에 대해
# 초기값을 전부 아주 큰 값으로 설정
lst_ret = [INT_MAX] * (n + 1) 

lst_path = [0] * (n + 1)

# 그래프를 인접행렬로 표현
# 양방향 그래프이므로 양쪽 다 표시해줍니다.
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    dl_graph[x][y] = z
    dl_graph[y][x] = z

# 시작, 끝 위치를 입력으로 받습니다.
start, end = tuple(map(int, input().split()))

# 시작위치에는 dist값을 0으로 설정
lst_ret[start] = 0

# O(|V|^2) 다익스트라 코드
for i in range(1, n + 1):
    # V개의 정점 중 
    # 아직 방문하지 않은 정점 중
    # dist값이 가장 작은 정점을 찾아줍니다.
    min_index = -1
    for j in range(1, n + 1):
        if lst_visited[j]:
            continue
        
        if min_index == -1 or lst_ret[min_index] > lst_ret[j]:
            min_index = j

    # 최솟값에 해당하는 정점에 방문 표시를 진행합니다.
    lst_visited[min_index] = True

    # 최솟값에 해당하는 정점에 연결된 간선들을 보며
    # 시작점으로부터의 최단거리 값을 갱신해줍니다.
    for j in range(1, n + 1):
        # 간선이 존재하지 않는 경우에는 넘어갑니다.
        if dl_graph[min_index][j] == 0:
            continue

        if lst_ret[j] > lst_ret[min_index] + dl_graph[min_index][j]:
            lst_ret[j] = lst_ret[min_index] + dl_graph[min_index][j]
            # path값을 갱신해줍니다.
            lst_path[j] = min_index

# 정점 A에서 정점 B로 가기 위한 최단거리를 출력합니다.
print(lst_ret[end])

# 도착지 B에서 시작하여
# 시작점 A가 나오기 전까지
# path를 따라 움직여줍니다.
x = end
lst_distance = []
lst_distance.append(x)

while x != start:
    x = lst_path[x]
    lst_distance.append(x)

# 거쳐간 순서를 거꾸로 출력합니다.
for num in lst_distance[::-1]:
    print(num, end=" ")