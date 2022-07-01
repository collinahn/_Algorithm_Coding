from sortedcontainers import SortedSet

n,m = map(int, input().split())

ssetCoord = SortedSet([
    tuple(map(int, input().split()))
    for _ in range(n)
])

for _ in range(m):
    query = int(input())
    idx = ssetCoord.bisect_left((query,0))
    if idx == n:
        print(-1, -1)
    else:
        print(ssetCoord[idx])
        ssetCoord.pop(idx)
