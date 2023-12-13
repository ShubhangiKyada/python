#Hello Create one CSV file named “employee.csv”.
#Take minimum 10 records in this CSV file according to following EMP table.



#Write a python program to import CSV file data into table EMP(e_id, e_name, salary, date_of_birth).


#Q-5 Write a python program to create database named “company.db” in sqlite.
#Ans=create that database in sqlite3


#Also create table sales_product (order_no (primary key), p_id, p_name, p_unit_price, sales_quantity, sales_unit_price).
import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales_product (
        order_no INTEGER PRIMARY KEY,
        p_id INTEGER,
        p_name TEXT,
        p_unit_price REAL,
        sales_quantity INTEGER,
        sales_unit_price REAL
    )
''')


#Take values from user and insert minimum 5 records. Access sales_product table data and display all data with ‘total_sales_price’ and
#‘total_profit’. 


import sqlite3

def insert():

    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()


    order_no = int(input('Enter Order No: '))
    p_id = int(input('Enter Product ID: '))
    p_name = input('Enter Product Name: ')
    p_unit_price = float(input('Enter Product Unit Price: '))
    sales_quantity = int(input('Enter Sales Quantity: '))
    sales_unit_price = float(input('Enter Sales Unit Price: '))

    
    cursor.execute('''
        INSERT INTO sales_product (order_no, p_id, p_name, p_unit_price, sales_quantity, sales_unit_price)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (order_no, p_id, p_name, p_unit_price, sales_quantity, sales_unit_price))

    conn.commit()
    conn.close()

def main():
    while True:
        print('1. Insert')
        print('2. Exit')

        choice = input("Enter choice: ")

        if choice == '1':
            insert()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    
#After insert all the values convert data into dataFrame:
    import pandas as pd
    import sqlite3

    conn = sqlite3.connect('company.db')
    
    data=pad.read_sql_query("Select * from sales_product")



#(total_sales_price = sales_quantity * sales_unit_price).
#(total_unit_price = p_unit_price * sales_quantity)
#(total_profit = total_sales_price – total_unit_price)


data['total_sales_price']=data['sales_quantity'] *data[' sales_unit_price']
data['total_unit_price']=data['p_unit_price'] * data['sales_quantity']
data['total_profit']=data['total_sales_price'] - data['stotal_unit_price']


print(data)


'''Q-6 Write a phython script to do following on student (Rollno, Name, Sub 1, Sub 2, Sub 3, total) table:'''

import sqlite3
def create_table():
 conn=sqlite3.connect('student.db')
 cur=conn.cursor()
 cur.execute('''create table student
 (Rollno number primary key,
 Name text,
 sub1 number,
 sub2 number,
 sub3 number,
 total number)''')
 print("table created\n\n")
 conn.commit()
 conn.close()

create_table()


'''1.Insert atleast 5 to 10 records.'''
import sqlite3
def insert_records():
 conn=sqlite3.connect('student.db')
 cur=conn.cursor()
 cur.execute('insert into student values(1,"Shubhangi",90,90,80,260)')
 cur.execute('insert into student values(2,"Krushal",90,80,70,240)')
 cur.execute('insert into student values(3,"Rutika",70,90,80,240)')
 cur.execute('insert into student values(4,"Radhika",60,70,50,180)')
 cur.execute('insert into student values(5,"Rensi",70,80,80,230)')
 cur.execute('insert into student values(6,"Visha",90,60,70,220)')
 cur.execute('insert into student values(7,"Ram",90,50,80,220)')
 cur.execute('insert into student values(8,"Sujal",90,90,70,250)')
 cur.execute("select * from student")
 record=cur.fetchall()
 for i in record:
 print(i)


 conn.commit()
 conn.close()

insert_records()

#2. Update the specific record value.

import sqlite3
def update_record():
 conn=sqlite3.connect('student.db')
 cur=conn.cursor()
  cur.execute('update student set Name="Rohan" where Rollno=7')
 cur.execute("select * from student")
 record=cur.fetchall()
 for i in record:
 print(i)


 conn.commit()
 conn.close()
 
update_record()

#3. Delete the record specific record.

import sqlite3
def delete_record():
 conn=sqlite3.connect('student.db')
 cur=conn.cursor()
 cur.execute('delete from student where Rollno=8')
 cur.execute("select * from student")
 record=cur.fetchall()
 for i in record:
 print(i)


 conn.commit()
 conn.close()


delete_record()


#4. Display student detail who got highest total marks.

import sqlite3
def high_marks():
 conn=sqlite3.connect('student.db')
 cur=conn.cursor()
 cur.execute("select * from student order by total desc limit 1")
 record=cur.fetchone()
 print(record)

 conn.commit()
 conn.close()

high_marks() 













'''5. Write Python Script to do followings on item.csv (Item_no, Item_name, Price,
Qty, total)'''


#1) Write item's detail in the item.csv file. Calculate total = price * Qty

import pandas as pd
csvFile=pd.read_csv('item.csv')
print(csvFile)
addItems={
 'Item_no':8,
 'Item_name':'Mouse',
 'Price':2500,
 'Qty':6
 }
addtoDataFrame=pd.DataFrame(addItems, index=['7'])
csvFile=pd.concat([csvFile,addtoDataFrame])
print("\nAdd Items into Items Details:\n",csvFile)


#2) Using data frame display item name and price whose price is between 1000 to 5000.

import pandas as pd
csvFile=pd.read_csv('item.csv')
itemsPrice=csvFile[(csvFile['Price']>1000)&(csvFile['Price']<5000)][['Item_name','Price']]
print("\nItem name and price whose price is between 1000 to 5000:\n\n",itemsPrice)

      
#3) Display alternate records from item.csv file.


import pandas as pd
csvFile=pd.read_csv('item.csv')
altRecord=csvFile.iloc[::2]
print("\n Alternate Records:\n\n",altRecord)


#4) Display items whose price is minimum, maximum.
import pandas as pd
csvFile=pd.read_csv('item.csv')
minPrice=csvFile[csvFile['Price'] == csvFile['Price'].min()]
maxPrice=csvFile[csvFile['Price'] == csvFile['Price'].max()]
print("\n\n Minimum Price:\n",minPrice)
print("\n\n Maximum Price:\n",maxPrice)


#5) Sort the data according to item name wise.

import pandas as pd

csvFile=pd.read_csv('item.csv')
sortByName=csvFile.sort_values(by='Item_name')
print("\n\nSort By Item Name:\n",sortByName)

#6) Display items rows between 3th to 7th row.

import pandas as pd
csvFile=pd.read_csv('item.csv')
rowsofFile=csvFile.iloc[2:7]
print("\n\nRows between 3th to 7th row:\n",rowsofFile)

#7) Display last 6 rows.

import pandas as pd
csvFile=pd.read_csv('item.csv')
lastSix=csvFile.tail(6)
print("\n\nLast 6 rows:\n",lastSix)


#6. Sales (sid, year, totalsales) Create above table into a SQLite database with appropriate constraints.
#1) Insert at least 5-10 records into the sales table
#Ans : write in sqlite3
.open sale.db
sqlite> .table
sqlite> create table Sales(
(x1...> sid number primary key,
(x1...> year number not null,
(x1...> totalsales number);
sqlite> insert into Sales values
 ...> (101,2004,50000),
 ...> (102,2005,60000),
 ...> (103,2006,45000),
  ...> (104,2007,55000),
 ...> (105,2008,65000),
 ...> (106,2009,60000);

 
#2) Export sales table data into sales.csv file.
 
mode csv
sqlite> .header on
sqlite> .output sales.csv
 

'''Q-9 Create CSV File for Product Selling for 6 Months and 40 add at-least 5 Records for 5 different products.
Prod_name JAN FAB MAR APR MAY JUN'''
#Create Python script to perform following task.
#A. Read data in Dataframe.

import csv
import pandas as pd
data=pd.read_csv('empdata.csv')
print(data)
 
#B. Add columns and calculate total_sell, average_sell.

import csv
import pandas as pd
data['total_sale']=data['JAN']+data['FAB']+data['MAR']+data['APR']+dat
a['MAY']+data['JUN']
data['average_sale']=(data['JAN']+data['FAB']+data['MAR']+data['APR']+
data['MAY']+data['JUN'])/6
print(data)
 
#D. Explain final dataframe to csv named sell_analysis.csv

import csv
import pandas as pd
data.to_csv('sell_analysis.csv')



 '''Create COLLEGE database and perform following tasks. Create following table using SQLite and then close the connection.
Student(roll_no INTEGER Primary key, name text(20), city text(20), age INTEGER)
Insert ten student records for Student table.'''
#Display all records of the Student table using cursor.

import sqlite3
conn=sqlite3.connect('college.db')
cur=conn.cursor()
cur.execute("select * from student")
row=cur.fetchall()

for i in row:
    print(i)

conn.commi()
conn.close()
 
#Export the Student table to CSV file.

with open("student.csv", "w", newline='') as csvfile:
 csv_writer = csv.writer(csvfile)
 csv_writer.writerow(['roll_no', 'name', 'city', 'age'])
 csv_writer.writerows(row)
conn.close()


#3 Write a python code to write the data frame in the csv file. Name csv file as "studentinfo.csv".and also create pychart for the same.


#first create dictionary

data = {
 'StudentID': [1, 2, 3, 4, 5],
 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
 'Age': [20, 22, 21, 23, 20]
}


#then covert it into datafream

df = pd.DataFrame(data)

#then import it into csv

df.to_csv("studentinfo.csv", index=False)

