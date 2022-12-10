import sys

n, m = map(int, sys.stdin.readline().split())

# 팀 : 멤버
team_member = {}

# 멤버 : 팀
member_team = {}

for _ in range(n):
    
    team = sys.stdin.readline().rstrip()
    member_count = int(sys.stdin.readline())
    member_list = []
    for _ in range(member_count):        
        member = sys.stdin.readline().rstrip()
        member_list.append(member)
        member_team[member] = team
    member_list.sort()
    team_member[team] = member_list

for _ in range(m):
    
    name = sys.stdin.readline().rstrip()
    category = int(sys.stdin.readline().rstrip())
    
    if (category == 0):
        for member in team_member[name]:
            print(member)
    else:
        print(member_team[name])
