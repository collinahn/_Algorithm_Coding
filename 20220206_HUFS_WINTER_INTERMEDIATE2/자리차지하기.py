n, m =  map(int, input().split())

lstRule = list(map(int, input().split()))

dctRet = {}
cnt = 0

for target in lstRule:
    idx = target
    while idx > 0:
        if not dctRet.get(idx):
            dctRet[idx] = True
            cnt += 1
            break
        
        idx -= 1
        if idx == 0:
            print(cnt)
            import sys
            sys.exit()

print(len(dctRet))
            

    