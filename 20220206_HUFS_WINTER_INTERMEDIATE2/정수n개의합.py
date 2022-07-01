n, m = map(int, input().split())

lstN = list(map(int, input().split()))

totalSum = 0
elemCnt = 0

hitCnt = 0

for idx, startElement in enumerate(lstN):
    totalSum = 0
    elemCnt = 0
    while elemCnt + idx < n: # 인덱스 에러 방지
        totalSum += lstN[idx+elemCnt]
        elemCnt += 1
        if totalSum == m:
            hitCnt += 1
            break
        if totalSum > m:
            break

print(hitCnt)