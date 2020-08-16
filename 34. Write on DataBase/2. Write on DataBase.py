import mysql.connector


cnx = mysql.connector.connect(user='root',
                              password='', host='127.0.0.1', database='login')   # edit database
cursor = cnx.cursor()
while True:
    username = input('username: ')
    password = input('password: ')
    if '@' not in username or '.' not in username.split('@')[1]:
        print('Please enter your email in correct form: \"expression@string.string\"')
        continue
    else:
        break
cursor.execute("INSERT INTO info VALUES (\'%s\', \'%s\')" % (username, password))  # edit table
cnx.commit()
cnx.close()