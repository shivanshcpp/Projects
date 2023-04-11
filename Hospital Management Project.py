while (True):
    flag=0
    print("""
                ================================
                   Welcome To CityHospital
                ================================
    """)
    from tabulate import tabulate
    import mysql.connector as mysq
    from datetime import date
    database = mysq.connect(host="localhost", user="root",
                        password="Shivansh@123", database="HOSPITAL")
    if (database == 0):
        print("Error in Database Connection...")
    cursorobject = database.cursor()
    cursorobject.execute("create database if not exists hospital")
    cursorobject.execute("use hospital")
    patient = "CREATE TABLE IF NOT EXISTS PATIENT(patient_id INT unsigned AUTO_INCREMENT,name VARCHAR(100),gender CHAR ,age INT unsigned,contact_no VARCHAR(10),address VARCHAR(100) ,disease VARCHAR(100),checkin DATE ,blood_group VARCHAR(2) ,doctor_assigned VARCHAR(100) ,PRIMARY KEY(patient_id))"
    cursorobject.execute(patient)
    database.commit()

    patient_admit = "CREATE TABLE IF NOT EXISTS ADMIT(name VARCHAR(100),days_no INT,room_no INT ,room_type VARCHAR(50),price INT)"
    cursorobject.execute(patient_admit)
    database.commit()

    staff="CREATE TABLE IF NOT EXISTS STAFF(name VARCHAR(100),occupation VARCHAR(100),specialization VARCHAR(100),salary INT(10),fees INT(10),phone_no VARCHAR(10),address VARCHAR(50))"
    cursorobject.execute(staff)
    database.commit()

    patient_appointment = "CREATE TABLE IF NOT EXISTS APPOINTMENT(app_id INT unsigned AUTO_INCREMENT primary key,name VARCHAR(100),symptom VARCHAR(100),date DATE,time VARCHAR(7),doctor_assigned VARCHAR(100),fee INT(5))"
    cursorobject.execute(patient_appointment)
    database.commit()

    def print_staff():
        cursorobject=database.cursor()
        query = "SELECT * FROM staff"
        cursorobject.execute(query)
        myresult = cursorobject.fetchall()
        data=["Name","Occupation","Specialization","Salary","Fees","Phone No","Address"]
        print(tabulate(myresult,headers=data,tablefmt="psql"))
        cursorobject.close()

    def print_staff_by_name(pname):
        cursorobject=database.cursor()
        query = "SELECT * FROM Staff WHERE occupation=%s"
        val = (pname,)
        cursorobject.execute(query, val)
        myresult = cursorobject.fetchall()
        data=["Name","Occupation","Specialization","Salary","Fees","Phone No","Address"]
        print(tabulate(myresult,headers=data,tablefmt="psql"))
        cursorobject.close()

    def add_staff():
        cursorobject = database.cursor()
        specl=""
        name = input("Enter Name:")
        occ=input("Enter Occupation:")
        if(occ=="Doctor" or occ=="doctor"):
            specl = input("Enter Doctor's Specialization:")
            fees = input("Enter Doctor's Fees:")
        address = input("Enter Address:")
        contact = input("Enter Contact No:")
        salary = int(input("Enter Salary:"))
        sql1 = """INSERT INTO STAFF(name,occupation,specialization,address,phone_no,salary,fees) VALUES('{}','{}','{}','{}','{}','{}','{}');""".format(
            name, occ, specl, address, contact,salary,fees)
        cursorobject.execute(sql1)
        database.commit()
        cursorobject.close()
        print("SUCCESSFULLY ADDED!!")

    def delete_staff(pname,occ):
        cursorobject=database.cursor()
        query = "DELETE FROM staff WHERE name=%s and occupation=%s"
        val=(pname,occ)
        cursorobject.execute(query,val)
        print("SUCCESSFULLY DELETED!!")
        cursorobject.close()

    def delete_staff_name(pname):
        cursorobject=database.cursor()
        query = "DELETE FROM staff WHERE name=%s"
        val=(pname,)
        cursorobject.execute(query,val)
        print("SUCCESSFULLY DELETED!!")
        cursorobject.close()

    def print_patient():
        cursorobject=database.cursor()
        query = "SELECT * FROM Patient"
        cursorobject.execute(query)
        myresult = cursorobject.fetchall()
        data=["Patient Id","Name","Gender","Age","Phone No","Address","Symptom","Checkin Date","Blood Group","Doctor Assigned"]
        print(tabulate(myresult,headers=data,tablefmt="psql"))
        cursorobject.close()

    def add_patient():
        cursorobject = database.cursor()
        name = input("Enter Patient's Name:")
        gender = input("Enter Patient's Gender(M/F):")
        age = int(input("Enter age:"))
        contact = input("Enter Contact No:")
        address = input("Enter Address:")
        disease = input("Enter Disease:")
        blood_group = input("Enter Blood Group:")
        doctor = input("Enter Doctor:")
        today = date.today()
        sql1 = """INSERT INTO PATIENT(name,gender,age,contact_no,address,disease,checkin,blood_group,doctor_assigned) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}');""".format(
            name, gender, age, contact, address, disease, today, blood_group, doctor)
        cursorobject.execute(sql1)
        database.commit()
        cursorobject.close()
        print("""
                                        ====================================
                                           !!!!Registered Successfully!!!!
                                        ====================================
                                                                                            """)
                          
    def discharge(pname):
        cursorobject=database.cursor()
        query = "DELETE FROM patient WHERE name=%s"
        val=(pname,)
        cursorobject.execute(query,val)
        cursorobject.close()
        print("""
                    ===================================
                            PATIENT DISCHARGED
                    ===================================
                                                        """)

    def print_patient_by_name(pname):
        cursorobject=database.cursor()
        query = "SELECT * FROM Patient WHERE name=%s"
        val = (pname,)
        cursorobject.execute(query, val)
        myresult = cursorobject.fetchall()
        data=["Patient Id","Name","Gender","Age","Phone No","Address","Symptom","Checkin Date","Blood Group","Doctor Assigned"]
        print(tabulate(myresult,headers=data,tablefmt="psql"))
        cursorobject.close()

    def final_fee(pname):
        cursorobject=database.cursor()
        query = "SELECT fee FROM appointment where name=%s"
        val=(pname,)
        cursorobject.execute(query,val)
        myresult = cursorobject.fetchone()
        fee=myresult[0]
        print("TOTAL BILL :- ",fee)
        cursorobject.close()

    def appointment(pname):
        cursorobject = database.cursor()
        symptom = input("Enter Symptom:")
        time = input("Enter Time of Appointment:")
        doctor = input("Enter Doctor's Name:")
        today = date.today()
        query1 = "SELECT fees FROM Staff where name=%s and occupation=%s"
        t="Doctor"
        val=(doctor,t)
        cursorobject.execute(query1,val)
        myresult = cursorobject.fetchall()
        for x in myresult:
            a=list(x)
            fee=a[0]
        sql1 = """INSERT INTO APPOINTMENT(name,symptom,date,time,doctor_assigned,fee) VALUES('{}','{}','{}','{}','{}','{}');""".format(
                pname, symptom, today, time,doctor,fee)
        cursorobject.execute(sql1)
        database.commit()
        cursorobject.close()
        print("""
                                        ====================================
                                          !!!!!!!Appointment Booked!!!!!!!
                                        ====================================
                                                                                            """)

    def cancel_appointment(pname):
        cursorobject=database.cursor()
        query = "DELETE FROM appointment WHERE name=%s"
        val=(pname,)
        cursorobject.execute(query,val)
        print("SUCCESSFULLY CANCELLED!!")
        cursorobject.close()

    def search_appointment(today):
        c=0
        cursorobject=database.cursor()
        query = "SELECT * FROM appointment WHERE date=%s"
        val = (today,)
        cursorobject.execute(query, val)
        myresult = cursorobject.fetchall()
        for x in myresult:
            c=c+1
        data=["Appointment Id","Name","Symptom","Date of Appointment","Appointment's Time","Doctor Assigned","Fees"]
        print(tabulate(myresult,headers=data,tablefmt="psql"))
        cursorobject.close()
        print("Total Appointments for Today:",c)

    cursorobject.execute("CREATE TABLE IF NOT EXISTS user_login(username varchar(30) primary key,password varchar(30) default'000')")
    while (True):
        print("""
                        1. Sign In
                        2. Registration
                        3. Forgot Password?(Wanna Change It??)
                        4. Exit Application
                                                            """)
        r = int(input("enter your choice:"))
        if(r == 2):
            print("""

                =======================================
                  !!!!!!!!!!Register Yourself!!!!!!!!
                =======================================
                                                    """)
            u = input("Enter Username:")
            p = input("Enter Password (Password should be strong):")
            cursorobject.execute("INSERT INTO user_login VALUES('" + u + "','" + p + "')")
            database.commit()
            print("""
                =========================================
                      Registration Done Successfully
                =========================================
                                                        """)
        elif(r==4):
            flag=1
            break
        elif(r==3):
            ad=input("Enter Username:")
            new=input("Enter New Password:")
            query="UPDATE user_login SET password=%s where username=%s"
            val=(new,ad)
            cursorobject.execute(query,val)
            print("PASSWORD SUCCESSFULLY CHANGED!!")
        elif(r == 1):
            print("""
                    ==================================
                      -------   Sign In   -------
                    ==================================
                                                        """)
            user = input("Enter Username:")
            passw = input("Enter Password:")
            cursorobject.execute("SELECT password FROM user_login WHERE username='" + user + "'")
            myresult = cursorobject.fetchall()
            for x in myresult:
                a = list(x)
                if a[0] == str(passw):
                    while (True):
                        print("""
                                1.Administration
                                2.Patient(Details)
                                3.Appiontment
                                4.Sign Out

                                                   """)
                        a = int(input("ENTER YOUR CHOICE:"))
                        if(a == 1):
                            print("""
                                    1. Display the Details
                                    2. Add a New Member
                                    3. Delete a Member
                                    4. Return to Menu
                                                             """)
                            b = int(input("Enter your Choice:")) 
                            if(b == 1):
                                print("""
                                        1. Display All Details
                                        2. Display All Doctors Details
                                        3. Display All Nurse Details
                                        4. Return to Menu
                                                         """)
                                c=int(input("Enter your Choice:"))
                                if(c==1):
                                    print_staff()
                                elif(c==2):
                                    pname="Doctor"
                                    print_staff_by_name(pname)
                                elif(c==3):
                                    pname="Nurse"
                                    print_staff_by_name(pname)
                                elif(c==4):
                                    continue
                                else:
                                    print("OOPS WRONG CHOICE!!")
                            elif(b==2):
                                add_staff()
                            elif(b==3):
                                print("""
                                        1. Remove Doctor(Delete Doctor Record)
                                        2. Remove Nurse(Delete Nurse Record)
                                        3. Delete Others Record
                                        4. Return to Menu
                                                                """)
                                c=int(input("ENTER YOUR CHOICE:"))
                                p = input("Do You really want to delete this data?(y/n):")
                                if p == "y":
                                    if(c==1):
                                        print_staff_by_name("Doctor")
                                        occ="Doctor"
                                        pname=input("Enter Doctor's Name:")
                                        delete_staff(pname,occ)
                                    elif(c==2):
                                        print_staff_by_name("Nurse")
                                        occ="Nurse"
                                        pname=input("Enter Nurse's Name:")
                                        delete_staff(pname,occ)
                                    elif(c==3):
                                        print_staff()
                                        pname=input("Enter Staff's Name:")
                                        delete_staff(pname)
                                    elif(c==4):
                                        continue
                                    else:
                                        print("OOPS WRONG CHOICE!!")
                                else:
                                    print("NOT DELETED!!")
                            elif(b==4):
                                continue
                            else:
                                print("OOPS WRONG CHOICE!!")
                        elif(a==2):
                            print("""
                                        1. Show Patients Information
                                        2. Add a New Patient
                                        3. Discharge Summary
                                        4. Return to Menu 
                                                                 """)
                            b = int(input("Enter your Choice:"))
                            if(b==1):
                                print_patient()
                            elif(b==2):
                                add_patient()
                            elif(b==3):
                                pname=input("ENTER PAYIENT'S NAME:")
                                print_patient_by_name(pname)
                                final_fee(pname)
                                bill_amt = input("Bill Paid?? (y/n):")
                                if bill_amt == "y":
                                    discharge(pname)
                                else:
                                    print("""
                                                         W A R N I N G
                                                ===================================
                                                 !!!!!!!BILLS NOT PAID!!!!!!!
                                                ===================================
                                                                                    """)
                            elif(b==4):
                                continue
                            else:
                                print("WRONG CHOICE!!")
                        elif(a==3):
                            print("""
                                        1. Book an Appointment
                                        2. Search Today's Appointments
                                        3. Cancel Appointment
                                        4. Return to Menu
                                                                """)
                            b=int(input("Enter your Choice:"))
                            if(b==1):
                                pname=input("Enter Name of patient:")
                                query = "SELECT name FROM Patient"
                                cursorobject.execute(query)
                                myresult = cursorobject.fetchall()
                                for x in myresult:
                                    a=list(x)
                                if(a[0]==str(pname)):
                                    appointment(pname)
                                else:
                                    print("""
                                            ===================================
                                                Please Register Patient First
                                            ===================================
                                                                                """)
                                    continue
                            elif(b==2):
                                today = date.today()
                                search_appointment(today)
                            elif(b==3):
                                pname=input("Enter Patient's Name whose Appointment to be Cancelled:")
                                cancel_appointment(pname)
                            elif(b==4):
                                continue
                            else:
                                print("OOPS WRONG CHOICE!!")
                            
                        elif(a==4):
                            break
                        else:
                            print("OOPS WRONG CHOICE!!")
                else:
                    print("""
                    ===================================
                     !!!!!!!OOPS WRONG PASSWORD!!!!!!!
                    ===================================
                                                        """)
                    break;  
    if(flag==1):
        break        


