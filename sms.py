import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="shubham",
    password="9406882656",
    database="student"
)

TABLE_NAME = 'student_info'


def addn():
    name = input("Enter name: ")
    roll = input("Enter roll no.: ")
    address = input("Enter address: ")
    phn = input("Enter Phone Number: ")
    mycursor = mydb.cursor()
    mycursor.execute(f'''
  CREATE TABLE IF NOT EXISTS 
    {TABLE_NAME}(
    name varchar(50), 
    roll_no varchar(10) primary key, 
    address varchar(50), 
    phn varchar(10)
    )'''
                     )
    st = f'''INSERT INTO
          {TABLE_NAME}(name, roll_no, address, phn)
          values('{name}','{roll}','{address}','{phn}')'''
    mycursor.execute(st)
    mydb.commit()
    print("Added Successfully")

def display():
	mycursor = mydb.cursor(dictionary=True)
	mycursor.execute(f"SELECT * FROM  {TABLE_NAME}")
	for row in mycursor:
		print(row)

def search():
    roll = input("Enter roll no: ")
    mycursor = mydb.cursor(dictionary=True)
    sql = f'''SELECT * FROM {TABLE_NAME} WHERE roll_no = '{roll}' '''
    mycursor.execute(sql)
    for row in mycursor:
        print(row)

def upd():
    rolln = input("Enter roll no: ")
    mycursor = mydb.cursor(dictionary=True)
    nam = input("Enter name: ")
    roll = input("Enter roll no.: ")
    addr = input("Enter address: ")
    ph = input("Enter Phone Number: ")
    st = f'''update {TABLE_NAME}
            set name = '{nam}', roll_no ='{roll}', address = '{addr}', phn = '{ph}'
            where roll_no = '{rolln}' '''
    mycursor.execute(st)
    mydb.commit()
    print("Updated Successfully")

def delt():
    rolln = input("Enter roll no: ")
    mycursor = mydb.cursor(dictionary=True)
    st = f'''delete from {TABLE_NAME}
            where roll_no = '{rolln}' '''
    mycursor.execute(st)
    mydb.commit()
    print("Deleted Successfully")


def main():

    choice = 0
    while(choice < 6):
        choice = int(
            input("1.Add 2.Display 3.Search 4.Update 5.Delete 6.Exit \nEnter your choice : "))
        if(choice == 1):
            addn()
        elif(choice == 2):
            display() 
        elif(choice == 3):
           search()
        elif(choice == 4):
            upd()
        elif(choice == 5):
            delt()

        mydb.close()


main()
