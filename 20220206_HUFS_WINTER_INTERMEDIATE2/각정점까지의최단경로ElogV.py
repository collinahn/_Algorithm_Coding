import heapq
import sys

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
k = int(input())

dl_graph = [[] for _ in range(n + 1)]
lst_heapq = []

lst_ret = [INT_MAX] * (n + 1)

# 양방향 그래프
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    dl_graph[x].append((y, z))
    dl_graph[y].append((x, z))

lst_ret[k] = 0

heapq.heappush(lst_heapq, (0, k))  # k는 정점번호

while lst_heapq: # O(|E|log|V|)
    # 근접한 원소 탐색 후 제거
    min_dist, min_idx = heapq.heappop(lst_heapq)

    if min_dist != lst_ret[min_idx]:
        continue

    for target_idx, target_dist in dl_graph[min_idx]:
        new_dist = lst_ret[min_idx] + target_dist
        if lst_ret[target_idx] > new_dist:
            lst_ret[target_idx] = new_dist
            heapq.heappush(lst_heapq, (new_dist, target_idx))

for i in range(1, n + 1):
    print(-1) if lst_ret[i] == INT_MAX else print(lst_ret[i])
