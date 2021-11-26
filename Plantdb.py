# This file is use for creating tables of plant and customer and storeing values init.
# You have to comment the code after creating and storeing values init (Don't comment out the conneection to database).

import sqlite3

# Open connection to data base
conn = sqlite3.connect('Plant_DB.db')
# print ("Opened database successfully")

# # Creating plant Table
# conn.execute('''CREATE TABLE PLANTINFO (ID INT PRIMARY KEY,PLANT_NAME TEXT NOT NULL, QUANTITY INT, PRICE REAL);''')
# print ("PlantInfo Table created successfully")

# # Creating customer table
# conn.execute('''CREATE TABLE USERINFO (PHONE_NUMBER INT PRIMARY KEY,NAME TEXT);''')
# print ("UserInfo Table created successfully")
# conn.commit()
# # Adding Data in plant table
# conn.execute("INSERT INTO PLANTINFO (ID,PLANT_NAME,QUANTITY,PRICE) \
#       VALUES (1, 'MANGO', 10000, 130.36 ), (2, 'ORANGE', 25000, 110.50),(3, 'APPLE',4200,70.00),(4, 'CUSTARD APPLE', 8000,90.26 ),(5,'LEMON',19000,45.50)");
# conn.commit()
# print("PlantInfo Table Done")
# # Adding Data in customer table
# conn.execute("INSERT INTO USERINFO (PHONE_NUMBER,NAME) \
#       VALUES (7020576985, 'Vedant_Kashettiwar'), (8208191188, 'Abhishek_Wagmare')")
# conn.commit()
# print("UserInfo Table Done")