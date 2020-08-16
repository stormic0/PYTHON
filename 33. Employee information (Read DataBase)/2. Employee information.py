import mysql.connector


cnx = mysql.connector.connect(user='root',
                              password='', host='127.0.0.1', database='human')
cursor = cnx.cursor()
query = "SELECT*FROM ID"
cursor.execute(query)
ou_list = []
for (name, weight, height) in cursor:
    ou_list.append((name, height, weight))
ou_list.sort(key=lambda x: x[1], reverse=True)
a = 0
while a < len(ou_list):
    for j in range(len(ou_list)-1):
        if ou_list[j][1] == ou_list[j+1][1] and ou_list[j][2] > ou_list[j+1][2]:
            ou_list[j], ou_list[j+1] = ou_list[j+1], ou_list[j]
    a += 1
for i in ou_list:
    print('{} {} {}'.format(i[0], i[1], i[2]))
cnx.close()