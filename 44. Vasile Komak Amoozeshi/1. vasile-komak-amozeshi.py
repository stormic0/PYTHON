n, ou = int(input()), []
lamp_num = list(map(int, input().split(' ')))
lamp_status = list(map(int, input().split(' ')))
for i in range(n):
	if lamp_status[i] == 1:
		ou.append(lamp_num[i])
ou.sort()
for i in ou:
	if i == ou[len(ou)-1]:
		print('%s' % i, end='')
	else:
		print('%s ' % i, end='')

