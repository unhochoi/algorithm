import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

load = list(map(int, sys.stdin.readline().split()))

sorted_load = sorted(load)

interver = []
for i in range(1, n):
    interver.append(sorted_load[i]-sorted_load[i-1])

sorted_interver = sorted(interver, reverse=True)

print(sum(sorted_interver[k-1:]))