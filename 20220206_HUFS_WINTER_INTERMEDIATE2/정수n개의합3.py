n, k = map(int, input().split())

lstlstElem = []
lstlstElem.append([0] * (n+1))

for _ in range(1, n+1):
    lstRow = [0]
    lstRow += list(map(int, input().split()))
    lstlstElem.append(lstRow)

lstlstSum = [
    [
        0
        for _ in range(n+1)
    ]
    for _ in range(n+1)
]

for i in range(1, n+1):
    for j in range(1, n+1):
        lstlstSum[i][j] = lstlstSum[i-1][j]+lstlstSum[i][j-1]-lstlstSum[i-1][j-1]+lstlstElem[i][j]

setRet = set()
for idx in range(1, n-k+2):
    for jdx in range(1, n-k+2):
        setRet.add(lstlstSum[k+idx-1][k+jdx-1] - lstlstSum[idx-1][k+jdx-1] - lstlstSum[k+idx-1][jdx-1] + lstlstSum[idx-1][jdx-1])

print(max(setRet))