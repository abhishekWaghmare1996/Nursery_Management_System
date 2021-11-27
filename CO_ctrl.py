# Nursery Managment System (NMS).
# This file contain code of the NMS.

from Plantdb import*
from datetime import date, datetime 
import random
import math
import pyfiglet 

class Head:
    def Display(self,quote):
        today = date.today()
        now = datetime.now()     
        current_time = now.strftime("%H:%M")
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("                                          WELCOME TO VEDAABHI NURSERY                                                           ")
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("                                                     QUOTE                                                                           ")
        print()
        print(quote)
        print("                               ----------------------------------------------------                                                     ")
        print("WE CARE")
        print("----------------------------------")
        print("Today Date is: ",today)
        print("Current Time:", current_time)
        print("----------------------------------")

class Controls(Head):
    def Con(self):
        user=input("Select User\nStaff/Customer:").capitalize()
        if user=="Staff":
            showdb=input("Show Plant database\nYes/No:").capitalize()
            if showdb=="Yes":
                show=conn.execute("SELECT * from PLANTINFO")
                for row in show:
                    ID,PLANT_NAME,QUANTITY,PRICE=row
                    print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY}, price= ₹{PRICE}\n")
    
            showudb=input("Show Customer database\nYes/No:").capitalize()
            if showudb=="Yes":
                show=conn.execute("SELECT * from USERINFO")
                for row in show:
                    PHONE_NUMBER,NAME=row
                    print(f"PHONE NUMBER={PHONE_NUMBER} ,NAME={NAME}\n")

            add=input("Do you want to add plant data in database\nYes/No:").capitalize()
            if add=="Yes":
                n=int(input("Enter the amount of plant you want to add:"))
                for ir in range (0,n):
                    a=int(input("Enter Id:"))
                    b=input("Enter plant name:").capitalize()
                    c=int(input("Enter quantity:"))
                    d=float(input("Enter price:"))
                    conn.execute(f"INSERT INTO PLANTINFO (ID,PLANT_NAME,QUANTITY,PRICE) \
                    VALUES ({a}, '{b}', {c}, {d})")
                    conn.commit()
                show=conn.execute("SELECT * from PLANTINFO")
                for row in show:
                    ID,PLANT_NAME,QUANTITY,PRICE=row
                    print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY}, price= ₹{PRICE}\n")

            remove=input("Do you want to remove plant from database?\nYes/No:").capitalize()
            if remove=="Yes":
                n=int(input("Enter the amount of plant you want to remove:"))
                for ir in range (0,n):
                    EnterId=int(input("Enter Id of plant:"))
                    removes=conn.execute(f"DELETE FROM PLANTINFO WHERE ID = {EnterId}")
                    conn.commit()
                show=conn.execute("SELECT * from PLANTINFO")
                for row in show:
                    ID,PLANT_NAME,QUANTITY,PRICE=row
                    print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY}, price= ₹{PRICE}\n")

            update=input("Do you want to update plant quantity?\nYes/No:").capitalize()
            if update=="Yes":
                n=int(input("Enter the amount of plant you want to update:"))
                for ir in range (0,n):
                    uid=int(input("Enter Id of plant you want to update:"))
                    uquantity=int(input("Enter the new quantity:"))
                    conn.execute(f"UPDATE PLANTINFO set Quantity = {uquantity} WHERE ID = {uid}")
                    conn.commit()
                show=conn.execute(f"SELECT * FROM PLANTINFO")
                for row in show:
                    ID,PLANT_NAME,QUANTITY,PRICE=row
                    print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY}, price= ₹{PRICE}\n")
           
            updatep=input("Do you want to update price of plant?\nYes/No:").capitalize()
            if updatep=="Yes":
                n=int(input("Enter the amount of plant you want to update:"))
                for ipr in range (0,n):
                    uid=int(input("Enter Id of plant you want to update:"))
                    uprice=float(input("Enter the new price:"))
                    conn.execute(f"UPDATE PLANTINFO set PRICE= {uprice} WHERE ID = {uid}")
                    conn.commit()
                show=conn.execute(f"SELECT * FROM PLANTINFO")
                for row in show:
                    ID,PLANT_NAME,QUANTITY,PRICE=row
                    print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY}, price= ₹{PRICE}\n")
           


        if user=="Customer":
                ephone=int(input("Enter Number:"))
                cur=conn.execute(f"SELECT PHONE_NUMBER FROM USERINFO WHERE PHONE_NUMBER= {ephone}")
                row=cur.fetchone()
                if row != None:
                    showdb=input("Show Plant database\nYes/No:").capitalize()
                    if showdb=="Yes":
                        show=conn.execute("SELECT * from PLANTINFO")
                        for row in show:
                            ID,PLANT_NAME,QUANTITY,PRICE=row
                            print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY},price= ₹{PRICE}\n")

                    purchase = input("Do you want to purchase\nYes/No:").capitalize()
                    if purchase == "Yes":
                        Total_bill=0
                        n=int(input("Enter the number of plant you want:"))
                        for val in range(0,n):
                            plant_id = int(input("Enter the Plant Id:"))
                            quantity = int(input("Enter the Quantity:"))
                            cursor = conn.execute(f"SELECT quantity from PLANTINFO where id={plant_id}")
                            price = conn.execute(f"SELECT PRICE FROM PLANTINFO WHERE ID = {plant_id}")
                            for row in price:
                                ip=row[0]
                                Total_bill+=ip*float(quantity)
                            for row in cursor:
                                a = row[0]
                                remaining_quant = a-quantity
                                conn.execute(f"UPDATE PLANTINFO set QUANTITY = {remaining_quant} where id = {plant_id}")
                                conn.commit()
                        print(f"Original bill is ₹{Total_bill}")
                        discount=Total_bill*0.05
                        Finalprice=Total_bill-discount
                        print("Congratulations You Recived 5% Discount On Your Bill")
                        print(f"Discounted bill Is ₹{math.ceil(Finalprice)}")
                        result = pyfiglet.figlet_format("Thankyou For Shopping", font = "digital" )
                        print(result)
                else:
                    cname=input("Enter Your Name:")
                    cphone=int(input("Enter Phone Number:"))
                    conn.execute(f"INSERT INTO USERINFO (PHONE_NUMBER,NAME) \
                    VALUES ({cphone}, '{cname}')")
                    conn.commit()
                    showdb=input("Show Plant database\nYes/No:").capitalize()
                    if showdb=="Yes":
                        show=conn.execute("SELECT * from PLANTINFO")
                        for row in show:
                            ID,PLANT_NAME,QUANTITY,PRICE=row
                            print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY},price= ₹{PRICE}\n")
                            
                    Total_bill=0
                    n=int(input("Enter the number of plant you want:"))
                    for val in range(0,n):
                        plant_id = int(input("Enter the Plant Id:"))
                        quantity = int(input("Enter the Quantity:"))
                        cursor = conn.execute(f"SELECT quantity from PLANTINFO where id={plant_id}")
                        price = conn.execute(f"SELECT PRICE FROM PLANTINFO WHERE ID = {plant_id}")
                        for row in price:
                            ip=row[0]
                            Total_bill+=ip*float(quantity)
                        for row in cursor:
                            a = row[0]
                            remaining_quant = a-quantity
                            conn.execute(f"UPDATE PLANTINFO set QUANTITY = {remaining_quant} where id = {plant_id}")
                            conn.commit()
                    print(f"Total bill is ₹{Total_bill}")
                    result = pyfiglet.figlet_format("Thankyou For Shopping", font = "digital" )
                    print(result)

class In:
    Quote=("A beautiful plant is like having a friend around the house.\n-Beth Ditto","Always do your best. What you plant now, you will harvest later.\n-Og Mandino","Don't judge each day by the harvest you reap but by the seeds that you plant.\n-Robert Louis Stevenson")
    quote=random.choice(Quote)
    a=Controls()
    a.Display(quote)
    a.Con()
    
c=In()