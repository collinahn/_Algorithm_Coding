import sys

n, k = map(int, input().split())

lstN = list(map(int, input().split()))
minSize = sys.maxsize

for idx, startElement in enumerate(lstN):
    targetCnt = 0
    sizeCnt = 0

    while idx + sizeCnt < n:
        if lstN[idx+sizeCnt] == 1:
            targetCnt += 1

        if targetCnt >= k:
            minSize = min(minSize, targetCnt)
            break
            
        sizeCnt += 1

if minSize == sys.maxsize:
    print(-1)
    sys.exit()

print(minSize)