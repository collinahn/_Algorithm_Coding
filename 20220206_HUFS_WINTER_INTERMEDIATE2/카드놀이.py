import heapq

n = int(input())
lst_card = [
    int(input())
    for _ in range(n)
]

# 2n 최대값
pq = []

for card in lst_card:
    heapq.heappush(pq, card)

win = 0

spq = set(pq)

for idx in range(1, 2*n+1):
    if idx in spq:
        continue

    if idx > pq[0]:
        win += 1
        heapq.heappop(pq)

print(win)