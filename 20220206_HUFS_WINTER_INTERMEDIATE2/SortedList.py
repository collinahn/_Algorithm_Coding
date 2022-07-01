from sortedcontainers import SortedSet


setRet = SortedSet()
lstInputSet = [
    input().split() for _ in range(int(input()))
]

for command in lstInputSet:
    if command[0] == 'add':
        setRet.add(command[1])

    elif command[0] == 'remove':
        setRet.remove(command[1])

    elif command[0] == 'find':
        print('true' if command[1] in setRet else 'false')

    elif command[0] == 'lower_bound':
        try:
            print(setRet[setRet.bisect_left(command[1])])
        except IndexError:
            print(None)

    elif command[0] == 'upper_bound':
        try:
            print(setRet[setRet.bisect_right(command[1])])
        except IndexError:
            print(None)

    elif command[0] == 'largest':
        if not setRet:
            print(None)
            continue

        print(max(setRet))

    elif command[0] == 'smallest':
        if not setRet:
            print(None)
            continue

        print(min(setRet))