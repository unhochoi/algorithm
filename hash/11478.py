import sys

s = list(sys.stdin.readline().rstrip())

dict = {}
for size in range(1, len(s)+1):
    for start in range(len(s)-size+1):
        dict[''.join(s[start:start+size])] = 1

print(len(dict))