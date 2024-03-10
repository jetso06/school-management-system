import mysql.connector as sqltr
mycon=sqltr.connect(host='localhost',user='root',passwd='jetso',use_pure=True,database="comp_activity")
c=mycon.cursor()

def displayrecords():
    global mycon
    global c
    try:
        c.execute("select * from teacher")
        d=c.fetchall()
        for i in d:
            print(i)
    except:
        print("Error")

def countrecords():
    global mycon
    global c
    c.execute("select * from teacher")
    d=c.fetchall()    
    count=c.rowcount
    print("The number of records present is:",count)


def searchrecord():
    global mycon
    global c
    i=(input("enter the Teacher's Name':"))
    c.execute("select * from teacher where Name= '{}'".format(i))
    d=c.fetchall()
    for i in d:
        print(i)
    if i not in d:
        print("invalid entry")

def addrecord():
    global mycon
    global c
    while True:
        i=int(input("enter the teacher id:"))
        b=input("enter the Teacher Name:")        
        h=input("enter the Department of the Teacher:")        
        k=input("enter the Hire date(yy-mm-dd):")
        j=input("enter the category:")
        l=input("enter the gender(M/F)")
        o=int(input("enter the salary of the teacher"))
        st="insert into teacher (ID,Name,Department,HireDate,Category,Gender,Salary)values({},'{}','{}','{}','{}','{}',{})".format(i,b,h,k,j,l,o)
        c.execute(st)
        mycon.commit()
        ch=input("Do you want to continue?Y/N")
        if ch=="N" or ch=="n":
            break

def deleterecord():    
    global mycon
    global c
    while True:
        p=int(input("enter the Id of the teacher:"))
        d="delete from teacher where ID= {}".format(p,)
        c.execute(d)
        mycon.commit()
        ch=input("Do you want to continue?Y/N")
        if ch=="N" or ch=="n":
            break

def updaterecords():
    global mycon
    global c
    while True:
        n=int(input("enter the Teacher Id:"))
        print("1.UPDATE TEACHER ID")
        print("2.UPDATE TEACHER NAME")
        print("3.UPDATE TEACHER DEPARTMENT")
        print("4.UPDATE HIRE DATE")
        print("5.UPDATE CATEGORY")
        print("6.UPDATE GENDER")
        print("7.UPDATE SALARY")
        ch=int(input("enter the choice="))
        if ch==1:
            m=int(input("enter the new teacher id:"))
            c.execute("update teacher set ID={} where ID={}".format(m,n))
            mycon.commit()
        elif ch==2:
            k=input("enter the new teacher name:")
            c.execute("update teacher set Name='{}' where ID={}".format(k,n))
            mycon.commit()
        elif ch==3:
            o=input("enter the new teacher department:")
            c.execute("update teacher set Department='{}' where ID={}".format(o,n))
            mycon.commit()
        elif ch==4:
            w=input("enter the new hire date(yy-mm-dd):")
            c.execute("update teacher set HireDate='{}' where ID={}".format(w,n))
            mycon.commit()
        elif ch==5:
            q=input("enter the new category:")
            c.execute("update teacher set Category='{}' where ID={}".format(q,n))
            mycon.commit()
        elif ch==6:
            e=input("enter the new gender:")
            c.execute("update teacher set Gender='{}' where ID={}".format(e,n))
            mycon.commit()
        elif ch==7:
            r=input("enter the new Salary:")
            c.execute("update teacher set Salary={} where ID={}".format(r,n))
            mycon.commit()
        else:
            print("invalid choice")
        ch1=input("Do you want to continue?Y/N")
        if ch1=="N" or ch1=="n":
            break
