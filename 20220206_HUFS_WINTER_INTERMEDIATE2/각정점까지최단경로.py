import sys

INT_MAX = sys.maxsize
n, m = tuple(map(int, input().split()))

dl_graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
lst_visited = [False] * (n + 1)

lst_dist = [INT_MAX] * (n + 1) 

for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    dl_graph[x][y] = z

lst_dist[1] = 0

for _ in range(1, n + 1): # O(|V|^2)
    min_idx = -1
    for j in range(1, n + 1):
        if lst_visited[j]:
            continue
        
        if min_idx == -1 or lst_dist[min_idx] > lst_dist[j]:
            min_idx = j

    lst_visited[min_idx] = True

    for j in range(1, n + 1):
        if dl_graph[min_idx][j] == 0:
            continue

        lst_dist[j] = min(lst_dist[j], lst_dist[min_idx] + dl_graph[min_idx][j])

for i in range(2, n + 1):
    print(-1) if lst_dist[i] == INT_MAX else print(lst_dist[i])