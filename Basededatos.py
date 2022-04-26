import mysql.connector

class empleados:
    def __int__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", passwd="", database="employee_management")

    def __str__(self):
        datos=self.consult_employee()
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
    
    def consult_employee(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM employee")
        datos = cur.fechall()
        cur.close()
        return datos

    def new_method(self):
        cur = self.cnn.cursor()
        return cur

    def search_employee(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT, FROM employee WHERE Id = {}". format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def enter_employee(self,Id,Name, Email, Time_Worked, Entry_Date, Manager_ID):
        cur = self.cnn.cursor()
        sql='''INSERT INTO employee(Id, Name, Email, Time_Worked, Entry_Date, Manager_ID) VALUES
        ('{}', '{}', '{}', '{}', '{}', '{}')'''.format(Id, Name, Email, Time_Worked, Entry_Date, Manager_ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n 

    def delete_employee(self, Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM employee WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n 

    def modify_employee(self, Id, Name, Email, Time_Worked, Entry_Date, Manager_ID):
        cur = self.cnn.cursor()
        sql='''UPDATE employee SET Id='{}', Name='{}', Email='{}', Time_Worked= '{}', Entry_Date= '{}', 
        Manager_ID= '{}' WHERE Id={}'''.format(Id, Name, Email, Time_Worked, Entry_Date, Manager_ID)  
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()

    