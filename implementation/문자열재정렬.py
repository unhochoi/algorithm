import sys
import re

s = sys.stdin.readline().rstrip()

first_rule = re.compile('[A-Z]')
second_rule = re.compile('[0-9]')

first_result = sorted(first_rule.findall(s))
second_reulst = sum(map(int, second_rule.findall(s)))

result = ''.join(first_result)
result += str(second_reulst)

print(result)

