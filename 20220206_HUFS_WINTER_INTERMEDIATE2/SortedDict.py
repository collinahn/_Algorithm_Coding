# print(*list(map(lambda x: x**2, list(map(int, input().split())))))


# print(*(lambda x: [x.count(_) for _ in range(1, 10)])(list(map(int, input().split()))), sep='\n')


# print(*map(lambda x: sum(x), [ list(map(int, input().split())) for _ in range(4)]), sep='\n')



from sortedcontainers import SortedDict

# 변수 선언 및 입력:
n = int(input())
d = SortedDict()

for _ in range(n):
    command = input()

    if command.startswith("add"):
        _, k, v = tuple(command.split())
        k, v = int(k), int(v)
        d[k] = v

    elif command.startswith("remove"):
        k = int(command.split()[1])
        d.pop(k)

    elif command.startswith("find"):
        k = int(command.split()[1])
        if k not in d:
            print("None")
        else:
            print(d[k])

    else:
        # SortedDict가 비어있는 경우에 대해서는
        # None을 출력합니다.
        if not d:
            print("None")
        else:
            # key가 오름차순으로 정렬된 상태에서
            # value 값만 순서대로 가져옵니다.
            for value in d.values():
                print(value, end=" ")
            print()