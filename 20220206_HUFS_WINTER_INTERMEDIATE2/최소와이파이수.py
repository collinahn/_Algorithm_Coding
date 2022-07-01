population, wifiCoverage = map(int, input().split())

lstInput = list(map(int, input().split()))


wifiPut = 0
idxTarget = 0
for idx, home in enumerate(lstInput):
    if idxTarget > idx: continue
    if home:
        if idx >= idxTarget:
            wifiPut += 1
            idxTarget = idx + 2 * wifiCoverage + 1

print(wifiPut)