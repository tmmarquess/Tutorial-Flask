import sqlite3
import os

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

"""
-> String = text
-> int = integer
-> float = real
-> binary = blob
"""
cursor.execute("create table gta (release_year integer, release_name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos"),
]

#  (release_year, release_name, city)
cursor.executemany("insert into gta values (?,?,?)", release_list)

for row in cursor.execute("select * from gta"):
    print(row)

print("*****************************")
cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})

print(cursor.fetchall())

cities = [
    ("Liberty City", "New York"),
    ("Vice City", "Miami")
]

cursor.execute("create table cities (gta_city text, real_city text)")

cursor.execute("insert into cities values (?,?)", ("Los Santos", "Los Angeles"))
cursor.executemany("insert into cities values (?,?)", cities)

print("*****************************")
for row in cursor.execute("select * from cities"):
    print(row)

print("*****************************")
for i in cursor.execute("select release_year, release_name, real_city from cities as c, gta as g where c.gta_city = g.city"):
    print(i)

connection.close()
os.system('rm -rf gta.db')
