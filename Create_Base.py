import sqlite3 as sql

base= sql.connect('users.sqlite')
c = base.cursor()

#varchar - строковый тип данных в sqlite3
#c.execute('''CREATE TABLE user (login varchar,password varchar)''')

#base.commit()

login = input("Plz enter your login")
password = input ("Plz enter your password")

c.execute("INSERT INTO user (login,password) VALUES('%s','%s')"%(login,password))

base.commit()

c.execute("DELETE FROM user WHERE login='Segey'")

c.execute("SELECT * FROM user")

line = c.fetchall()

for l in line:
    print("Login:",l[0],"Password:",l[1])

print(line)

c.close()
base.close()