import mysql.connector

print ("--------School Management--------")

#connector
mydb=mysql.connector.connect( host="localhost", user="root",password="(enter your password)")#enter your mysql password 
mycursor=mydb.cursor()

#creating database 
mycursor.execute("create database if not exists pyschool")
mycursor.execute("use pyschool")

#creating required tables
mycursor.execute("create table if not exists pystudent(name varchar(50) not null,class varchar(25) not null,roll_no varchar(25),gender char(1))")
mycursor.execute("create table if not exists pystaff (sname varchar(50) not null,sgender char(1),subject varchar(25) not null,salary varchar(25))")
mydb.commit()

while True:
    print("1--> enter data for new student")
    print("2--> enter data for new staff data")
    print("3--> search student data")
    print("4--> search staff data")
    print("5--> edit student record")
    print("6--> edit staff record ")
    print("7--> delete student record ")
    print("8--> delete staff record")
    print("9--> exit ")

    ch=int(input("what would you like to do??"))
    #procedure for entering a NEW STUDENT RECORD
    if ch==1:
        print("All information prompted are mandatory to be filled")
        name=input("enter name ( limit 35 characters) :")
        std=str(input("enter class :"))
        roll_no=str(input("enter roll number:"))
        gender=str(input("enter Gender(M/F):"))
        mycursor.execute("insert into pystudent values('"+name+"','"+std+"','"+roll_no+"','"+gender+"')")
        mydb.commit()
        print("student record has been saved successfully!")
        
         
        #procedure for entering a NEW STAFF RECORD
    elif ch==2:
        sname=str(input("Enter staff member name:"))
        sgender=str(input("Enter Gender(M/F):"))
        dep=str(input("Enter department or subject:"))
        sal=int(input("Enter Salary:"))
        mycursor.execute("insert into pystaff values('"+sname+"','"+sgender+"','"+dep+"','"+str(sal)+"')")
        mydb.commit()
        print("staff record has been saved successfully ")
        


        #procedure for displaying student record
    elif ch==3:
        roll_no=str(input("enter student roll no:"))
        mycursor.execute("select * from pystudent where roll_no='"+roll_no+"'")
        for i in mycursor:
            name,std,roll_no,gender=i
            print(f'name:- {name}')
            print(f' std:- {std}')
            print(f' Roll number :- {roll_no}')
            print(f' gender :- {gender}')



    #procedure for displaying staff record 
    elif ch==4:
        name=str(input("Enter name :"))
        mycursor.execute("select * from pystaff where sname ='"+name+"'")
        for i in mycursor:
            sname,sgender,dep,sal=i
            print(f"name :- {sname}")
            print(f"gender:- {sgender}")
            print(f"department :- {dep}")
            print(f" salary :- {sal}")


    #procedure for editing student record
    elif ch==5:
        
        print("1--> edit student name ")
        print("2--> edit student class ")
        print("3--> edit student roll no ")
        ch1=int(input("select the category you would like to edit :"))

        #to edit the name of the student 
        if ch1==1:
            roll=input("enter the roll number of the student to change the name :")
            mycursor.execute("select * from pystudent ")
            flag =0
            for i in mycursor:
                t_id=i[2]
                if (t_id==roll):
                    flag=1
            if flag==1:
                print( "ID FOUND IN THE DATABASE ")
                uname=input("ENTER THE NEW NAME :")
                mycursor.execute("update pystudent set name='"+uname+"' where roll_no='"+roll+"'")
                mycursor.execute("select * from pystudent where roll_no='"+roll+"'")
                for i in mycursor:
                    name,std,roll_no,gender=i
                    print(f'name:- {name}')
                    print(f' std:- {std}')
                    print(f' Roll number :- {roll_no}')
                    print(f' gender :- {gender}')
                    mydb.commit()
            else:
                print("ID NOT FOUND IN THE DATABASE")

                
        #to edit the class  of the student
        elif ch1==2:
            nameid=input("enter the name of the student to change the class :")
            mycursor.execute("select * from pystudent ")
            flag =0
            for i in mycursor:
                t_id=i[0]
                if (t_id==nameid):
                    flag=1
            if flag==1:
                print( "ID FOUND IN THE DATABASE ")
                uclass=input("ENTER THE NEW CLASS :")
                mycursor.execute("update pystudent set clkass='"+uclass+"' where name='"+nameid+"'")
                mycursor.execute("select * from pystudent where name='"+nameid+"'")
                for i in mycursor:
                    name,std,roll_no,gender=i
                    print(f'name:- {name}')
                    print(f' std:- {std}')
                    print(f' Roll number :- {roll_no}')
                    print(f' gender :- {gender}')
                    mydb.commit()
            else:
                print("ID NOT FOUND IN THE DATABASE")



        #to edit the roll no of the student
        elif ch1==3:
            nameid=input("enter the name  of the student to change the rollno :")
            mycursor.execute("select * from pystudent ")
            flag =0
            for i in mycursor:
                t_id=i[0]
                if (t_id==nameid):
                    flag=1
            if flag==1:
                print( "ID FOUND IN THE DATABASE ")
                urollno=input("ENTER THE NEW ROLLNO :")
                mycursor.execute("update pystudent set roll_no='"+urollno+"' where name='"+nameid+"'")
                mycursor.execute("select * from pystudent where name='"+nameid+"'")
                for i in mycursor:
                    name,std,roll_no,gender=i
                    print(f'name:- {name}')
                    print(f' std:- {std}')
                    print(f' Roll number :- {roll_no}')
                    print(f' gender :- {gender}')
                    mydb.commit()
            else:
                print("ID NOT FOUND IN THE DATABASE")


#procedure for editing staff record
    elif ch==6:
      
        print("1--> edit staff member name ")
        print("2--> edit staff member department")
        print("3--> edit staff member salary ")
        ch2=int(input("select the category you would like to edit :"))
        
        
        #to edit the staff member name 
        if ch2==1:
            nameid=input("enter the current staff member to change the name :")
            mycursor.execute("select * from pystaff ")
            flag =0
            for i in mycursor:
                t_id=i[0]
                if (t_id==nameid):
                    flag=1
            if flag==1:
                print( "ID FOUND IN THE DATABASE ")
                uname=input("ENTER THE NEW NAME :")
                mycursor.execute("update pystaff set sname='"+uname+"' where sname='"+nameid+"'")
                mycursor.execute("select * from pystaff where sname ='"+nameid+"'")
                for i in mycursor:
                    sname,sgender,dep,sal=i
                    print(f"name :- {sname}")
                    print(f"gender:- {sgender}")
                    print(f"department :- {dep}")
                    print(f" salary :- {sal}")
                    mydb.commit()
            else:
                print("ID NOT FOUND IN THE DATABASE")


         #to change the department or subject of the staff member
        elif ch2==2:
            nameid=input("enter the current staff member to change the department or subject   :")
            mycursor.execute("select * from pystaff ")
            flag =0
            for i in mycursor:
                t_id=i[0]
                if (t_id==nameid):
                    flag=1
            if flag==1:
                print( "ID FOUND IN THE DATABASE  ")
                udep=input("ENTER THE NEW DEPARTMENT OR SUBJECT  :")
                mycursor.execute("update pystaff set subject='"+udep+"' where sname='"+nameid+"'")
                mycursor.execute("select * from pystaff where sname ='"+nameid+"'")
                for i in mycursor:
                    sname,sgender,dep,sal=i
                    print(f"name :- {sname}")
                    print(f"gender:- {sgender}")
                    print(f"department :- {dep}")
                    print(f" salary :- {sal}")
                    mydb.commit()
            else:
                print("ID NOT FOUND IN THE DATABASE")

         #to change the salary of a staff member
        elif ch2==3:
            nameid=input("enter the current staff member to change the salary   :")
            mycursor.execute("select * from pystaff ")
            flag =0
            for i in mycursor:
                t_id=i[0]
                if (t_id==nameid):
                    flag=1
            if flag==1:
                print( "ID FOUND IN THE DATABASE  ")
                usal=input("ENTER THE NEW SALARY   :")
                mycursor.execute("update pystaff set salary='"+str(usal)+"' where sname='"+nameid+"'")
                mycursor.execute("select * from pystaff where sname ='"+nameid+"'")
                for i in mycursor:
                    sname,sgender,dep,sal=i
                    print(f"name :- {sname}")
                    print(f"gender:- {sgender}")
                    print(f"department :- {dep}")
                    print(f" salary :- {sal}")
                    mydb.commit()
           
            else:
                print("ID NOT FOUND IN THE DATABASE")
            
                
            
        #procedure for deleting student record

    elif ch==7:
        r_no=str(input("Enter Roll no:"))
        mycursor.execute("delete from pystudent where name ='"+r_no+"'")
        mydb.commit()
        print("Student record is successfully deleted")
        mydb.commit()


    #procedure for deleting staff record

    elif ch==8:
        sname=str(input("enter Name : "))
        mycursor.execute("delete from pystaff where sname ='"+sname+"'")
        mydb.commit()
        print("Staff record is succesfully deleted")
        mydb.commit()


    elif ch==9:
        break 
