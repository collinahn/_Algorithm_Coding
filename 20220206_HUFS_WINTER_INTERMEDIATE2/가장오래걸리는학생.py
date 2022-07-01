import heapq
import sys

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))

graph = [
    [0] 
    for _ in range(n + 1)
]

pq = []

dist = [INT_MAX] * (n + 1)

# 그래프를 인접리스트로 표현합니다.
# 양방향 그래프이므로
# 양쪽에 추가해줘야함에 유의합니다.
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x].append((y, z))
    graph[y].append((x, z))

# 시작위치에는 dist값을 0으로 설정
dist[n] = 0

# 우선순위 큐에 시작점을 넣어줍니다.
# 거리가 가까운 곳이 먼저 나와야 하며
# 해당 지점이 어디인지에 대한 정보도 필요하므로
# (거리, 정점 번호) 형태로 넣어줘야 합니다.
heapq.heappush(pq, (0, n))

# O(|E|log|V|) 다익스트라 코드
# 우선순위 큐에
# 원소가 남아있다면 계속 진행해줍니다.
while pq:
    # 가장 거리가 가까운 정보를 받아온 뒤, 원소를 제거해줍니다.
    min_dist, min_index = heapq.heappop(pq)

    # 우선순위 큐를 이용하면
    # 같은 정점의 원소가 
    # 여러 번 들어가는 문제가 발생할 수 있어
    # min_dist가 최신 dist[min_index]값과 다르다면
    # 계산할 필요 없이 패스해줍니다.
    if min_dist != dist[min_index]:
        continue

    # 최솟값에 해당하는 정점에 연결된 간선들을 보며
    # 시작점으로부터의 최단거리 값을 갱신해줍니다.
    for target_index, target_dist in graph[min_index]:
        # 현재 위치에서 연결된 간선으로 가는 것이 더 작다면
        new_dist = dist[min_index] + target_dist
        if dist[target_index] > new_dist:
            # 값을 갱신해주고, 우선순위 큐에 해당 정보를 넣어줍니다.
            dist[target_index] = new_dist
            heapq.heappush(pq, (new_dist, target_index))

# 답을 구해줍니다.
ans = 0
# 최댓값을 구해줍니다.
for i in range(1, n):
    ans = max(ans, dist[i])

print(ans)



