import psycopg2

class Employee:
    def __init__(self):
        self.connection = psycopg2.connect(user="postgres", database="industry", password="#######", host="localhost")
        self.connection.commit()
        print("Connection established!")
        self.cursor = self.connection.cursor()

    def create_table_employee(self):
        query = "DROP TABLE IF EXISTS employee CASCADE"
        self.cursor.execute(query)
        self.connection.commit()
        print("Table is dropped!")

        query1 = "CREATE TABLE employee(emp_id INT PRIMARY KEY, emp_name VARCHAR(40), emp_city VARCHAR(20), emp_salary INT)"
        self.cursor.execute(query1)
        self.connection.commit()
        print("Table is created!")

    def insert_employee(self):
        values = [
            (101, 'mansi', 'nasik', 100000),
            (102, 'sharon', 'mumbai', 90000),
            (103, 'rajat', 'bikaner', 90500),
            (104, 'sayali', 'orisha', 95000),
            (105, 'nikita', 'kolhapur', 80000)
        ]
        args = ','.join(self.cursor.mogrify("(%s,%s,%s,%s)", i).decode('utf-8') for i in values)
        self.cursor.execute("INSERT INTO employee VALUES" + (args))
        print("Records inserted")
        self.connection.commit()

    def create_table_dept(self):
        query2 = "DROP TABLE IF EXISTS department CASCADE"
        self.cursor.execute(query2)
        self.connection.commit()
        print("Table is dropped!")

        query3 = "CREATE TABLE department(dept_id INT PRIMARY KEY, dept_name VARCHAR(40), emp_id INT REFERENCES employee(emp_id))"
        self.cursor.execute(query3)
        self.connection.commit()
        print("Table is created!")

    def insert_department(self):
        values = [
            (1, 'it', 103),
            (2, 'computer', 102),
            (3, 'dbms', 101),
            (4, 'it', 104),
            (5, 'dbms', 105)
        ]
        args = ','.join(self.cursor.mogrify("(%s,%s,%s)", i).decode('utf-8') for i in values)
        self.cursor.execute("INSERT INTO department VALUES" + (args))
        print("Records inserted")
        self.connection.commit()

    def show_result(self):
        query4 = "SELECT * FROM employee"
        self.cursor.execute(query4)
        res = self.cursor.fetchall()
        print("Employees:")
        for row in res:
            print(row)

        query5 = "SELECT * FROM department"
        self.cursor.execute(query5)
        rel = self.cursor.fetchall()
        print("Departments:")
        for row in rel:
            print(row)

    def close(self):
        self.cursor.close()
        self.connection.close()
        print('Connection closed!')

e1 = Employee()
e1.create_table_employee()
e1.insert_employee()
e1.create_table_dept()
e1.insert_department()
e1.show_result()
e1.close()
