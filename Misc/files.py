import os
import sqlite3

for subdir, dirs, files in os.walk('./'):
    for file in files:
        print(file)


conn1 = sqlite3.connect('example.db')

c = conn1.cursor()

# Create table
#c.execute('''CREATE TABLE stocks
 #            (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()


conn.execute("select * from stocks")


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()