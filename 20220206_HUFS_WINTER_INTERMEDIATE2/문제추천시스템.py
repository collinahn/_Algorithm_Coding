from sortedcontainers import SortedSet

n = int(input())

ssetBank = SortedSet([
    tuple(map(int, reversed(input().split())))
    for _ in range(n)
])

m = int(input())

lstCommand = [
    tuple(
        (lambda x: (x.split()[0], (int(x.split()[2] if len(x.split())==3 else -1), int(x.split()[1]))))(input()) # 난이도, 문제번호 순으로 저장
    ) for _ in range(n)
]

for command in lstCommand:
    if command[0] == 'ad':
        ssetBank.add(command[1])
    elif command[0] == 'sv':
        targetIdx = ssetBank.bisect_left(command[1])
        ssetBank.pop(targetIdx)
    elif command[0] == 'rc':
        if command[1][1] == 1:
            print(ssetBank[-1][1])
        elif command[1][1] == -1:
            print(ssetBank[0][1])
            