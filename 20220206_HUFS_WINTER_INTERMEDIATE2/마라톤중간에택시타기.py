n = int(input())

lstCoord = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


startSum = [0] * (n)
endSum = [0] * (n)

for i in range(1, n):
    x1, y1 = lstCoord[i-1]
    x2, y2 = lstCoord[i]
    startSum[i] = abs(x1-x2)+abs(y1-y2) + startSum[i-1]

    x3, y3 = lstCoord[n-i-1]
    x4, y4 = lstCoord[n-i]
    endSum[n-i-1] = abs(x3-x4)+abs(y3-y4) + endSum[n-i]


setRet = set()
for j in range(1, n-1):
    setRet.add(startSum[j-1] + abs(lstCoord[j+1][0]-lstCoord[j-1][0]) + abs(lstCoord[j+1][1]-lstCoord[j-1][1]) + endSum[j+1] )

print(min(setRet))