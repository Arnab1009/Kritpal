import datetime
import logging
import tkinter as tk
from tkinter import *
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='Xm41ucfb@10#',database='bank')
curs=conn.cursor()
conn.autocommit=True

bank=tk.Tk()
bank.title("Indian Service Bank")
label=tk.Label(bank,text="INDIAN SERVICE BANK")
label.pack(side="top")
'''
def insert1():
    a=custid.get()
    b=first_name.get()
    c=last_name.get()
    d=city.get()
    e=occupation.get()
    f=mobile_no.get()
    g=dob.get()
    h=bid.get()
    i=bname.get()
    j=accnumber.get()
    C_Insert="INSERT INTO customer(custid,first_name,last_name,city,occupation,mobile_no,dob) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f,g)
    A_Insert="INSERT INTO acc(accnumber,custid,bid,opening_balance,accdate,acctype,accstatus) VALUES('{}','{}','{}',{},'{}','{}','{}')".format(j,a,h,10000,datetime.date.today(),"Savings","Active")
    curs.execute("SET foreign_key_checks = 0;")
    curs.execute(C_Insert)
    curs.execute(A_Insert)
    curs.execute("SET foreign_key_checks = 1;")
    conn.commit()

def func1():
    global custid,first_name,last_name,city,occupation,mobile_no,dob,bid,bname,accnumber
    def but1():
        but1_lab=tk.Label(web1,text="Account successfully created!")
        but1_lab.grid(row=4,column=3)
    custid=tk.StringVar()
    first_name=tk.StringVar()
    last_name=tk.StringVar()
    city=tk.StringVar()
    occupation=tk.StringVar()
    mobile_no=tk.StringVar()
    dob=tk.StringVar()
    bid=tk.StringVar()
    bname=tk.StringVar()
    accnumber=tk.StringVar()
    web1=tk.Tk()
    web1.title("Create account")
    label1=tk.Label(web1,text="CREATE ACCOUNT")
    label1.grid(row=1,column=1)
    lab1=tk.Label(web1,text="Customer id : ")
    lab1.grid(row=2,column=1,pady=(0,20))
    ent1=tk.Entry(web1,width=15,textvariable=custid)
    custid.get()
    ent1.grid(row=2,column=2,pady=(0,20))
    lab2=tk.Label(web1,text="First name : ")
    lab2.grid(row=3,column=1,pady=(0,20))
    ent2=tk.Entry(web1,width=15,textvariable=first_name)
    first_name.get()
    ent2.grid(row=3,column=2,pady=(0,20))
    lab3=tk.Label(web1,text="Last name : ")
    lab3.grid(row=4,column=1,pady=(0,20))
    ent3=tk.Entry(web1,width=15,textvariable=last_name)
    last_name.get()
    ent3.grid(row=4,column=2,pady=(0,20))
    lab4=tk.Label(web1,text="City : ")
    lab4.grid(row=5,column=1,pady=(0,20))
    ent4=tk.Entry(web1,width=15,textvariable=city)
    city.get()
    ent4.grid(row=5,column=2,pady=(0,20))
    lab5=tk.Label(web1,text="Occupation : ")
    lab5.grid(row=6,column=1,pady=(0,20))
    ent5=tk.Entry(web1,width=15,textvariable=occupation)
    occupation.get()
    ent5.grid(row=6,column=2,pady=(0,20))
    lab6=tk.Label(web1,text="Mobile number : ")
    lab6.grid(row=7,column=1,pady=(0,20))
    ent6=tk.Entry(web1,width=15,textvariable=mobile_no)
    mobile_no.get()
    ent6.grid(row=7,column=2,pady=(0,20))
    lab7=tk.Label(web1,text="Date of Birth : ")
    lab7.grid(row=8,column=1,pady=(0,20))
    ent7=tk.Entry(web1,width=15,textvariable=dob)
    dob.get()
    ent7.grid(row=8,column=2,pady=(0,20))

    lab8=tk.Label(web1,text="Branch id : ")
    lab8.grid(row=9,column=1,pady=(0,20))
    ent8=tk.Entry(web1,width=15,textvariable=bid)
    bid.get()
    ent8.grid(row=9,column=2,pady=(0,20))
    lab9=tk.Label(web1,text="Branch name : ")
    lab9.grid(row=10,column=1,pady=(0,20))
    ent9=tk.Entry(web1,width=15,textvariable=bname)
    bname.get()
    ent9.grid(row=10,column=2,pady=(0,20))
    lab10=tk.Label(web1,text="Account number : ")
    lab10.grid(row=11,column=1,pady=(0,20))
    ent10=tk.Entry(web1,width=15,textvariable=accnumber)
    accnumber.get()
    ent10.grid(row=11,column=2,pady=(0,20))
    
    butt1=tk.Button(web1,text="Enter",command=lambda: [but1(),insert1()])
    butt1.grid(row=12,column=1,pady=(0,50))
    

button1=tk.Button(bank,text="CREATE ACCOUNT",command=func1)
button1.pack()
'''

def func2():
    acc_id=tk.StringVar()
    transnumber=tk.StringVar()
    transmed=tk.StringVar()
    withamt=tk.IntVar()
    depamt=tk.IntVar()
    web2=tk.Tk()
    web2.title("Transaction")
    label2=tk.Label(web2,text="TRANSACTION")
    label2.grid(row=1,column=1)
    lab11=tk.Label(web2,text="Account id : ")
    lab11.grid(row=2,column=1,pady=(0,20))
    ent11=tk.Entry(web2,width=15,textvariable=acc_id)
    acc_id.get()
    ent11.grid(row=2,column=2,pady=(0,20))
    
    def func4():
        curs.execute("SELECT accnumber FROM acc WHERE EXISTS(SELECT * FROM acc WHERE accnumber=%s);",(acc_id.get(),))
        data=curs.fetchall()
        l=len(data)        
        if len==0:
            label3=tk.Label(web2,text="Invalid User!")
            label3.grid(row=4,column=1)        
        else:
            web3=tk.Tk()
            web3.title("Transacation")
            label4=tk.Label(web2,text="TRANSACTION DETAILS")
            label4.grid(row=1,column=1)
            lab12=tk.Label(web3,text="Transaction number : ")
            lab12.grid(row=2,column=1)
            ent12=tk.Entry(web3,width=15,textvariable=transnumber)
            transnumber.get()
            ent12.grid(row=2,column=2)
            lab13=tk.Label(web3,text="Transaction medium : ")
            lab13.grid(row=3,column=1)
            ent13=tk.Entry(web3,width=15,textvariable=transmed)
            transmed.get()
            ent13.grid(row=3,column=2)
                
            def withdrawal():
                web4=tk.Tk()
                web4.title("Withdrawal")
                label5=tk.Label(web4,text="WITHDRAWAL")
                label5.grid(row=1,column=1)
                lab14=tk.Label(web4,text="Enter amount (maximum 5000) : ")
                lab14.grid(row=2,column=1)
                ent14=tk.Entry(web4,width=15,textvariable=withamt)
                withamt.get()
                ent14.grid(row=2,column=2)

                def msg1():
                    l1=tk.Label(web4,text="Amount successfully withdrawn!")
                    l1.grid(row=3,column=2)
                    k=acc_id.get()
                    l=transnumber.get()
                    m=transmed.get()
                    n=withamt.get()
                    W_Insert="INSERT INTO transdetails(transnumber,accnumber,transdate,transmed,transtype,transamt) VALUES('{}','{}','{}','{}','{}',{})".format(l,k,datetime.datetime.today(),m,"Withdrawal",n)
                    curs.execute(W_Insert)
                    conn.commit()
                msg_but1=tk.Button(web4,text="Enter",command=msg1)
                msg_but1.grid(row=3,column=2)
                    
            def deposit():
                logging.warning("deposit has been reached")
                web5=tk.Tk()
                web5.title("Deposit")
                label7=tk.Label(web5,text="DEPOSIT")
                label7.grid(row=1,column=1)
                lab15=tk.Label(web5,text="Enter amount : ")
                lab15.grid(row=2,column=1)
                ent15=tk.Entry(web5,width=15,textvariable=depamt)
                depamt.get()
                ent15.grid(row=2,column=2)

                def msg2():
                    l2=tk.Label(web5,text="Amount successfully deposited!")
                    l2.grid(row=3,colun=2)                           
                    k=acc_id.get()
                    l=transnumber.get()
                    m=transmed.get()
                    o=depamt.get()                   
                    D_Insert="INSERT INTO transdetails(transnumber,accnumber,transdate,transmed,transtype,transamt) VALUES('{}','{}','{}','{}','{}',{})".format(l,k,datetime.datetime.today(),m,"Withdrawal",o)
                    curs.execute(D_Insert)
                    conn.commit()
                msg_but2=tk.Button(web5,text="Enter",command=msg2)
                msg_but2.grid(row=3,column=2)  
                        
            butt2=tk.Button(web3,text="WITHDRAWAL",command=withdrawal)
            butt2.grid(row=4,column=2)
            butt3=tk.Button(web3,text="DEPOSIT",command=deposit)
            butt3.grid(row=5,column=2)
        
        
    butt4=tk.Button(web2,text="Enter",command=func4)
    butt4.grid(row=5,column=1)
    
    
    
button2=tk.Button(bank,text="TRANSACTION",command=func2)
button2.pack()
bank.mainloop()
'''
elif choice==2:
    acc_id=input("Enter your account id : ")
    curs.execute("SELECT * FROM acc WHERE accnumber=%s;",(acc_id,))
    data=curs.fetchall()
    count=curs.rowcount
    if count==0:
        print("Invalid user")
    else:
        print("1. Withdrawal")
        print()
        print("2. Deposit")
        print()
        transnumber=input("Enter transaction id : ")
        transmed=input("Enter transaction medium : ")
        n=int(input("Enter your choice : "))
        if n==1:
            withamt=int(input("Enter amount to be withdrawn(maximum is 5000) : "))
            W_Insert="INSERT INTO transdetails(transnumber,accnumber,transdate,transmed,transtype,transamt) VALUES('{}','{}','{}','{}','{}',{})".format(transnumber,acc_id,datetime.datetime.today(),transmed,"Withdrawal",withamt)
            curs.execute(W_Insert)
            print("Withdrawal of Rs. ",withamt," has been completed successfully!")
        elif n==2:
            depamt=int(input("Enter amount to be deposited"))
            D_Insert="INSERT INTO transdetails(transnumber,accnumber,transdate,transmed,transtype,transamt) VALUES (%s,%s,%s,%s,%s,%s)"
            val3=(transnumber,acc_id,datetime.date.today(),transmed,"Deposit",depamt)
            curs.execute(D_Insert,val3)
            print("Deposit of Rs. ",depamt," has been completed successfully!")
        else:
            print("Invalid choice")

elif choice==3:
    custid1=input("Enter your customer id : ")
    curs.execute("SELECT * FROM customer WHERE custid=%s;",(custid1,))
    if curs.fetchone() is None:
        print("Invalid account")
    else:
        curs.execute("SELECT * FROM customer WHERE custid=%s;",(custid1,))
        data1=curs.fetchall()
        for row in data1:
            print("Customer id = ",row[0])
            print("First name = ",row[1])
            print("Last name = ",row[2])
            print("City = ",row[3])
            print("Occupation = ",row[4])
            print("Mobile number = ",row[5])
            print("Date of birth = ",row[6])


elif choice==4:
    acc_id1=input("Enter your account number : ")
    curs.execute("SELECT * FROM transdetails WHERE accnumber=%s;",(acc_id1,))
    if curs.fetchone() is None:
        print("No transaction history")
    else:
        curs.execute("SELECT * FROM transdetails WHERE accnumber=%s;",(acc_id1,))
        data2=curs.fetchall()
        for i in data2:
                print("Transaction number = ",i[0])
                print("Account number = ",i[1])
                print("Transaction date = ",i[2])
                print("Transaction medium = ",i[3])
                print("Transaction type = ",i[4])
                print("Transaction amount = ",i[5])

elif choice==5:
    custid2=input("Enter your customer id : ")
    bid1=input("Enter your branch id : ")
    loanamt=int(input("Enter the loan amount : "))
    L_Insert="INSERT INTO loan(custid,bid,loanamt) VALUES (%s,%s,%s)"
    val4=(custid2,bid1,loanamt)
    curs.execute(L_Insert,val4)
    print("Loan has been successfully approved!")

elif choice==6:
    acc_id2=input("Enter your account id : ")
    custid3=input("Enter your customer id : ")
    curs.execute("SET foreign_key_checks = 0;")
    curs.execute("DELETE FROM acc WHERE accnumber=%s;",(acc_id2,))
    curs.execute("DELETE FROM customer WHERE custid=%s;",(custid3,))    
    print("Account successfully deleted!")
    curs.execute("SET foreign_key_checks = 1;")

elif choice==7:
    print("Quitting....")
    print("Thank you! Visit Again")

else:
    print("Invalid choice")
'''
