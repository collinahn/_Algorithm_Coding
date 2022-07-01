from sortedcontainers import SortedSet

n = int(input())

ssetCoord = SortedSet([
    tuple((lambda ip: (int(ip.split()[0]),ip.split()[1]))(input()))
    for _ in range(n)
])

print(ssetCoord)

if len(ssetCoord) % 2 == 0:
    print(ssetCoord[-1][0] - ssetCoord[0][0])
else:
    caseA = ssetCoord[-2][0] - ssetCoord[0][0]
    caseB = ssetCoord[-1][0] - ssetCoord[1][0]

    print(max(caseA, caseB))
