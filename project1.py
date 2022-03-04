import tkinter as tk
from tkinter.ttk import *
from tkinter.constants import BOTTOM, END, LEFT, RIGHT, TOP
from typing import Text
import mysql.connector
import datetime
conn=mysql.connector.connect(host="localhost",user="root",password="jayanth1589",database="databasesql")
cursor=conn.cursor(buffered=True)
def submitt():
    a=e1.get()
    b=e2.get()
    f=0
    sql="select * from authentication"
    cursor.execute(sql)
    
    conn.commit()
    c=cursor.fetchall()
    for i in c:
        i=list(i)
        if(i[0]==str(a) and i[1]==str(b)):
            f=1
            break
    if(f==1):
        home()
    else:
        l=tk.Label(text="Incorrect Credintals")
        pass
def home():
    
    
    try:
        window.destroy()
        
    except:
        pass
    try:
        a.destroy()
        
    except:
        pass
    try:
        aw.destroy()
        
    except:
        pass
    try:
        awi.destroy()
    except:
        pass
    global win
    win=tk.Tk()
    win.title("home")
    flabel=tk.Label(text="              MEDICAL MANAGEMENT SYSTEM",font=("Arial Bold",50))
    flabel.pack()
    stock=tk.Button(text="stock",background="pink",activeforeground="red",font=("Arial Bold",20),width=30,command=stck)
    customer=tk.Button(text="customer",background="pink",activeforeground="red",font=("Arial Bold",20),width=30,command=customersupport)
    user=tk.Button(text="User",background="pink",activeforeground="red",font=("Arial Bold",20),width=30,command=userr)
    stock.pack()
    customer.pack()
    user.pack()
    win.geometry("1600x1600")
    win.mainloop()
def stck():
    try:
        window.destroy()
        
    except:
        pass
    try:
        a.destroy()
        
    except:
        pass
    try:
        aw.destroy()
        
    except:
        pass
    try:
        
        win.destroy()
    except:
        pass
    global awi,pi,ui,ari,uij,pij,arij
    awi=tk.Tk()
    awi.title("Stock")
    m=tk.Menu(awi)
    m.add_command(label="Custm",command=customersupport)
    m.add_command(label="Adduser",command=userr)
    m.add_command(label="Home",command=home)
    awi.config(menu=m)
    uni=tk.Label(text="MEDICINE",font=("Arial Bold",20))
    ui=tk.Entry()
    pni=tk.Label(text="QUANTITY",font=("Arial Bold",20))
    pi=tk.Entry()
    ar=tk.Label(text="COST",font=("Arial Bold",20))
    ari=tk.Entry()
    bi=tk.Button(text="Add",background="pink",font=("Arial Bold",20),activebackground="red",width=10,command=stckaddi)
    unij=tk.Label(text="NEW MEDICINE",font=("Arial Bold",20))
    uij=tk.Entry()
    pnij=tk.Label(text="NEW QUANTITY",font=("Arial Bold",20))
    pij=tk.Entry()
    bij=tk.Button(text="NEW Add",background="pink",font=("Arial Bold",20),activebackground="red",width=10,command=stckadd)
    arj=tk.Label(text="NEW COST",font=("Arial Bold",20))
    arij=tk.Entry()
    uni.grid(row=0,column=0)
    ui.grid(row=0,column=1)
    pni.grid(row=1,column=0)
    pi.grid(row=1,column=1)
    bi.grid(row=3,column=1)
    ar.grid(row=2,column=0)
    ari.grid(row=2,column=1)
    unij.grid(row=0,column=2)
    uij.grid(row=0,column=3)
    pnij.grid(row=1,column=2)
    pij.grid(row=1,column=3)
    bij.grid(row=3,column=3)
    arj.grid(row=2,column=2)
    arij.grid(row=2,column=3)
    b=tk.Button(text="show records",background="pink",font=("Arial Bold",20),activebackground="red",width=15,command=stockavailable)
    b.grid(row=5,column=2)
    bl=tk.Button(text="show stock",background="pink",font=("Arial Bold",20),activebackground="red",width=15,command=stockrecords)
    bl.grid(row=6,column=2)
    l=tk.Label(text="",height=1)
    l.grid(row=4,column=0)
    awi.geometry("1600x1600")
    awi.mainloop()
def stockavailable():
    ar=tk.Toplevel(awi)
    conn=mysql.connector.connect(host="localhost",user="root",password="jayanth1589",database="databasesql")
    cursor=conn.cursor(buffered=True)
    dbs="select * from stockrecords"
    cursor.execute(dbs)
    r=cursor.fetchall()
    i=10
    e = Label(ar,width=12, text="MEDICINE",font=("Arial Bold",15)) 
    e.grid(row=0, column=0)
    e = Label(ar,width=12, text="QUANTITY",font=("Arial Bold",15)) 
    e.grid(row=0, column=1) 
    e = Label(ar,width=12, text="COST",font=("Arial Bold",15)) 
    e.grid(row=0, column=2) 
    for student in r: 
        for j in range(len(student)):
            e = Label(ar,width=12, text=student[j],font=("Arial Bold",10)) 
            e.grid(row=i, column=j) 
            #e.insert(END, student[j])
        i=i+1
    ar.mainloop()
def stockrecords():
    ar=tk.Toplevel(awi)
    conn=mysql.connector.connect(host="localhost",user="root",password="jayanth1589",database="databasesql")
    cursor=conn.cursor(buffered=True)
    dbs="select * from medicine"
    cursor.execute(dbs)
    r=cursor.fetchall()
    i=10
    
    e = Label(ar,width=12, text="MEDICINE",font=("Arial Bold",15)) 
    e.grid(row=0, column=0) 
    e = Label(ar,width=12, text="QUANTITY",font=("Arial Bold",15)) 
    e.grid(row=0, column=1)
    e = Label(ar,width=12, text="COST",font=("Arial Bold",15)) 
    e.grid(row=0, column=2) 
    for student in r: 
        for j in range(len(student)):
            e = Label(ar,width=12, text=student[j],font=("Arial Bold",10)) 
            e.grid(row=i, column=j) 
            #e.insert(END, student[j])
        i=i+1
    ar.mainloop()
def stckadd():
    conn=mysql.connector.connect(host="localhost",user="root",password="jayanth1589",database="databasesql")
    cursor=conn.cursor(buffered=True)
    l=uij.get()
    lp=pij.get()
    lpq=arij.get()
    sql="insert into medicine values('{}',{},{})".format(l,lp,lpq)
    sqlite="insert into stockrecords values('{}',{},{})".format(l,lp,lpq)
    cursor.execute(sql)
    cursor.execute(sqlite)
    conn.commit()
    uij.delete(0,"end")
    pij.delete(0,"end")
    arij.delete(0,"end")
    awi.mainloop()
def stckaddi():
    conn=mysql.connector.connect(host="localhost",user="root",password="jayanth1589",database="databasesql")
    cursor=conn.cursor(buffered=True)
    l=ui.get()
    lp=pi.get()
    lpq=ari.get()
    ais="update medicine set quantity={},cost={} where name = '{}'".format(lp,lpq,l)
    sqlite="insert into stockrecords values('{}',{},{})".format(l,lp,lpq)
    cursor.execute(ais)
    cursor.execute(sqlite) 
    conn.commit()
    ui.delete(0,"end")
    pi.delete(0,"end")
    ari.delete(0,"end")
    
def userr():
    try:
        
        awi.destroy()
    except:
        pass
    try:
        window.destroy()
        
    except:
        pass
    try:
        a.destroy()
        
    except:
        pass
    try:
        
        win.destroy()
    except:
        pass
    global un,u,pn,p,aw
    aw=tk.Tk()
    aw.title("User")
    m=tk.Menu(aw)
    m.add_command(label="Custm",command=customersupport)
    m.add_command(label="Stock",command=stck)
    m.add_command(label="Home",command=home)
    aw.config(menu=m)
    
    un=tk.Label(aw,text="USERNAME",font=("Arial Bold",20))
    u=tk.Entry()
    pn=tk.Label(aw,text="PASSWORD",font=("Arial Bold",20))
    p=tk.Entry()
    b=tk.Button(text="Add",background="pink",font=("Arial Bold",20),activebackground="red",width=10,command=userradd)
    un.grid(row=0,column=0)
    u.grid(row=0,column=1)
    pn.grid(row=1,column=0)
    p.grid(row=1,column=1)
    b.grid(row=2,column=1)
    aw.geometry("1600x1600")
def customersupport():
    try:
        
        awi.destroy()
    except:
        pass
    try:
        window.destroy()
        
    except:
        pass
    try:
        aw.destroy()
        
    except:
        pass
    try:
        win.destroy()
    except:
        pass
    global a,phno1,name1,medicine1,quantity1,total
    a=tk.Tk()
    a.title("Customersupport")
    m=tk.Menu(a)
    m.add_command(label="Adduser",command=userr)
    m.add_command(label="Stock",command=stck)
    m.add_command(label="Home",command=home)
    a.config(menu=m)
    name=tk.Label(a,text="name",font=("Arial Bold",20))
    phno=tk.Label(a,text="phno",font=("Arial Bold",20))
    medicine=tk.Label(a,text="medicine",font=("Arial Bold",20))
    quantity=tk.Label(a,text="quantity",font=("Arial Bold",20))
    name1=tk.Entry()
    phno1=tk.Entry()
    medicine1=tk.Entry()
    quantity1=tk.Entry()
    l=tk.Label(text="",height=1)
    l.grid(row=8,column=0)
    b=tk.Button(text="show records",background="pink",font=("Arial Bold",20),activebackground="red",width=15,command=records)
    b.grid(row=9,column=1)
    name.grid(row=1,column=0)
    name1.grid(row=1,column=1)
    phno.grid(row=2,column=0)
    phno1.grid(row=2,column=1)
    medicine.grid(row=3,column=0)
    medicine1.grid(row=3,column=1)
    quantity.grid(row=4,column=0)
    quantity1.grid(row=4,column=1)
    bill=tk.Button(text="bill",background="pink",font=("Arial Bold",20),activebackground="red",width=10,command=billl)
    bill.grid(row=5,column=0)
    clearr=tk.Button(text="clear",background="pink",font=("Arial Bold",20),activebackground="red",width=10,command=clear)
    clearr.grid(row=5,column=1)
    p2=tk.Label(text="Amount",font=("Arial Bold",20))
    p2.grid(row=6,column=0)
    total=tk.Entry()
    total.grid(row=6,column=1)
    s=tk.Button(text="SUBMIT",background="violet",font=("Arial Bold",20),activebackground="red",command=sub)
    s.grid(row=7,column=1)
    a.geometry("1600x1600")
    a.mainloop()
def userradd():
    conn=mysql.connector.connect(host="localhost",user="root",password="jayanth1589",database="databasesql")
    cursor=conn.cursor(buffered=True)
    l=u.get()
    lp=p.get()
    sql="insert into authentication values(%s,%s)"
    aqr=(str(l),str(lp))
    try:
        cursor.execute(sql,aqr)
        j=tk.Label(text="SUCCESSFULLY ADDED")
    except:
        j=tk.Label(text="ERROR")
    u.delete(0,"end")
    p.delete(0,"end")
    j.grid(row=3,column=0)
    aw.mainloop()
    conn.commit()
def clear():
    name1.delete(0,"end")
    medicine1.delete(0,"end")
    quantity1.delete(0,"end")
    phno1.delete(0,"end")
    total.delete(0,"end")
def records():
    ar=tk.Toplevel(a)
    ar.title("Records")
    conn=mysql.connector.connect(host="localhost",user="root",password="jayanth1589",database="databasesql")
    cursor=conn.cursor(buffered=True)
    dbs="select * from records"
    cursor.execute(dbs)
    r=cursor.fetchall()
    i=10
    e = Label(ar,width=12, text="NAME",font=("Arial Bold",15)) 
    e.grid(row=0, column=0)
    e = Label(ar,width=12, text="PHNO",font=("Arial Bold",15)) 
    e.grid(row=0, column=1) 
    e = Label(ar,width=12, text="MEDICINE",font=("Arial Bold",15)) 
    e.grid(row=0, column=2) 
    e = Label(ar,width=12, text="QUANTITY",font=("Arial Bold",15)) 
    e.grid(row=0, column=3)
    e = Label(ar,width=12, text="DATE",font=("Arial Bold",15)) 
    e.grid(row=0, column=4)
    for student in r: 
        for j in range(len(student)):
            e = Label(ar,width=12, text=student[j],font=("Arial Bold",10)) 
            e.grid(row=i, column=j) 
            #e.insert(END, student[j])
        i=i+1
    ar.mainloop()
def sub():
    conn=mysql.connector.connect(host="localhost",user="root",password="jayanth1589",database="databasesql")
    cursor=conn.cursor(buffered=True)
    aq="insert into records values(%s,%s,%s,%s,%s)"
    
    n=name1.get()
    p=phno1.get()
    m=medicine1.get()
    q=quantity1.get()
    a=datetime.datetime.now()
    e = Label(width=12, text="NAME",font=("Arial Bold",15)) 
    e.grid(row=10, column=0)
    e = Label(width=12, text="PHNO",font=("Arial Bold",15)) 
    e.grid(row=10, column=1) 
    e = Label(width=12, text="MEDICINE",font=("Arial Bold",15)) 
    e.grid(row=10, column=2) 
    e = Label(width=12, text="QUANTITY",font=("Arial Bold",15)) 
    e.grid(row=10, column=3)
    
    e = Label(width=12, text=n,font=("Arial Bold",15)) 
    e.grid(row=11, column=0)
    e = Label(width=12, text=p,font=("Arial Bold",15)) 
    e.grid(row=11, column=1)
    e = Label(width=12, text=m,font=("Arial Bold",15)) 
    e.grid(row=11, column=2)
    e = Label(width=12, text=q,font=("Arial Bold",15)) 
    e.grid(row=11, column=3) 
    sql="update medicine set quantity=quantity-{} where name='{}'".format(q,m)
    aqr=(str(n),str(p),str(m),str(q),str(a))
    cursor.execute(aq,aqr)
    cursor.execute(sql)
    conn.commit()
def billl():
    c=medicine1.get()
    c=str(c)
    
    conn=mysql.connector.connect(host="localhost",user="root",password="jayanth1589",database="databasesql")
    cursor=conn.cursor(buffered=True)
    sql="select cost from medicine where name = '{}'".format(c)
    l=sql
    cursor.execute(l)
    conn.commit()
    al=cursor.fetchall()
    b=al[0][0]
    n=quantity1.get()
    
    m=(int(b))*(int(n))
    
    total.insert(0,str(m))

window=tk.Tk()
window.title("login")
f=Frame(window,width=900,height=800)
f.pack(side=TOP)
p1=tk.Label(f,text="Authentication required",font=("Arial Bold",10))
p1.grid(row=0,column=1)
l1=tk.Label(f,text="Username",font=("Arial Bold",20))
e1=tk.Entry(f)
l1.grid(row=1,column=0)
e1.grid(row=1,column=1)
l2=tk.Label(f,text="Password",font=("Arial Bold",20))
e2=tk.Entry(f)
l2.grid(row=2,column=0)
e2.grid(row=2,column=1)
exit=tk.Button(f,text="Exit",background="pink",activeforeground="red",font=("Arial Bold",20),command=window.destroy)
exit.grid(row=3,column=0)
submit=tk.Button(f,text="Submit",background="pink",activeforeground="red",font=("Arial Bold",20),command=submitt)
submit.grid(row=3,column=1)
window.geometry("1600x1600")
window.mainloop()








