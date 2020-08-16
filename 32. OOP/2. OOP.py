import random


class Human():
    name = ''
    age = None
    sex = 'Male'

class Footbalist(Human):
    team = ''
    price = None
    position = ''
    number = None

names = ['حسین', 'مازیار', 'اکبر', 'نیما', 'مهدی', 'فرهاد', 'محمد', 'خشایار', 'میلاد', 'مصطفی', 'امین', 'سعید',
         'پویا', 'پوریا', 'رضا', 'علی', 'بهزاد', 'سهیل', 'بهروز', 'شهروز', 'سامان', 'محسن']
teams = ['team 1', 'team 2']*11
players = []

for i in range(22):
    a = Footbalist()
    temp_name, temp_team = random.choice(names), random.choice(teams)
    a.name, a.team = temp_name, temp_team
    players.append(a)
    names.remove(temp_name)
    teams.remove(temp_team)

for i in players:
    print('%s:%s' % (i.name, i.team))
