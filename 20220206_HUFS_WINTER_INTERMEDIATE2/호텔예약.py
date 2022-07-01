n = int(input())

lstReception = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

lstX1X2 = []
for idx, (x1, x2) in enumerate(lstReception):
    lstX1X2.append((x1, 1, idx))
    lstX1X2.append((x2, -1, idx))

lstX1X2.sort()

totalSum = 0
maxRoom = 0
isSameRoom = False
prevDay = (0, 0)
overheadCnt = 0

for idxCnt, (x, value, i) in enumerate(lstX1X2):
    if x == prevDay[0] and value != prevDay[1]:
        value += 1
        overheadCnt += 1
    elif overheadCnt:
        value -= overheadCnt
        overheadCnt = 0

    totalSum += value

    maxRoom = max(totalSum, maxRoom)
    
    if idxCnt:
        prevDay = (lstX1X2[idxCnt][0], lstX1X2[idxCnt][1])

print(maxRoom)