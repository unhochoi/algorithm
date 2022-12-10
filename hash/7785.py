import sys

n = int(sys.stdin.readline())

dict = {}

for _ in range(n):
    name, info = sys.stdin.readline().split()
    if (info == "enter"):
        dict[name] = 1
    else:
        del dict[name]

result = sorted(dict.keys(), reverse = True)

for name in result:
    print(name)