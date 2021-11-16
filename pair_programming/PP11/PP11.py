import sqlite3

db = sqlite3.connect('PP11.sqlite')
cursor = db.cursor()
content = []

#read the file
f = open("candidates.txt", "r")
f.readline()
for line in f:
    cand = line.rstrip('\n').split("|")
    if len(cand) == 4:
        cand.insert(3, "")
    content.append(tuple(cand))


cursor.execute("DROP TABLE IF EXISTS candidates")
cursor.execute('''CREATE TABLE candidates (
id INTEGER PRIMARY KEY NOT NULL,
first_name TEXT,
last_name TEXT,
middle_initial TEXT,
party TEXT NOT NULL)''')

db.commit()

for cand in content:
    cursor.execute('''INSERT INTO candidates
    (id, first_name, last_name, middle_initial, party)
    VALUES (?, ?, ?, ?, ?)''', cand)

db.commit()

cursor.execute("SELECT * FROM candidates")
all_rows = cursor.fetchall()
print(all_rows)

db.close()
