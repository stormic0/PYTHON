teams = ['Iran', 'Spain', 'Portugal', 'Morocco']
wins, loses, draws, goal_difference, points= {}, {}, {}, {}, {}
for team in teams:
    wins[team],loses[team],goal_difference[team],draws[team],points[team] = 0,0,0,0,0
input1 = ['Iran', 'Iran', 'Iran', 'Spain', 'Spain', 'Portugal']
input2 = ['Spain', 'Portugal', 'Morocco', 'Portugal', 'Morocco', 'Morocco']
for i in input1:
    for j in input2:
        t1, t2 = map(int, input().split('-'))
        if t1 > t2:
            wins[i] += 1
            loses[j] += 1
            points[i] += 3
            goal_difference[i] += t1 - t2
            goal_difference[j] -= t1 - t2
        elif t1 < t2:
            wins[j] += 1
            loses[i] += 1
            points[j] += 3
            goal_difference[j] += t2 - t1
            goal_difference[i] -= t2 - t1
        else:
            draws[i] += 1
            draws[j] += 1
            points[i] += 1
            points[j] += 1
        input2.remove(j)
        break
OU = []
for team in teams:
    OU.append((team, wins[team], loses[team], draws[team], goal_difference[team], points[team]))
OU.sort(key=lambda x: x[5], reverse=True)
x = 0
while x <= len(OU):
    for i in range(3):
        if OU[i][5] == OU[i+1][5]:
            if OU[i][1] < OU[i+1][1]:
                OU[i], OU[i+1] = OU[i+1], OU[i]
            if OU[i][1] == OU[i+1][1]:
                if OU[i][0] > OU[i+1][0]:
                    OU[i], OU[i+1] = OU[i+1], OU[i]
    x += 1
for i in OU:
    print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' % (i[0],i[1],i[2],i[3],i[4],i[5]))
