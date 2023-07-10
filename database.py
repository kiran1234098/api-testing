import mysql.connector

# Establishing the database connection
connection =mysql.connector.connect(
    host="your_hostname",
    port="your_port",
    user="your_username"
    password ='your_password'
    database="your_database_name"
    
)
# creating a cursor object to excute queries
cursor =connection.cursor()

# Running a query
query = "select * from your_table_name"

cursor.execute(query)

import mysql.connector
connection = mysql.connector.connect(
    host="your_hostname",
    port = "your_port",
    user ="your_username",
    password ="your_password",
    database='yourdatabase'
)

cursor=connection.cursor()
cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
connection.close()    