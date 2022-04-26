from ast import Pass
from select import select
from tkinter import *
from tkinter import ttk
from Basededatos import empleados 




class ventana(Frame):
    
    employee = empleados()

    def __init__(self, master=None):
     super().__init__(master,width=780, height=550)
     self.master = master
     self.pack()
     self.create_widgets()
     self.textbox1()
 
     def cleanbox(self):
        self.txtID.delete(0, END)
        self.txtname.delete(0, END)
        self.txtemail.delete(0, END)
        self.txttime.delete(0, END)
        self.txtentry.delete(0, END)
        self.txtmanage.delete(0, END)



    def textbox1(self):
     datos = self.employee.consult_employee()
     for row in datos:
        self.grid.insert("",END,text=row[0], values=(row[1], row[2],row[3], row[4], row[5]))

    def fnew(self):
      self.cleanbox("normal")
      self.cleanbox()
      self.txtID.focus()

    def fadd(self):
       pass
   
    def fdelete(self):
       select = self.grid .focus()
       print(select)

       cl = select.grid.item(select, 'text')
       print(cl)

       values = select.grid.item(select, 'values')
       print(values)
      
       if cl == '':
          print('Please select an item') 
       else:
           values = self.grid.item (select, 'values')
           data = str(cl) + ", " + values[0]  + "," + values[1]
           print(values)
           r = massegebox.askquestion("Delete", 'Do you want to delete the selected record?' + data)

           if r == massegebox.YES:
              Pass
           else:
            n = self.employee.delete_employee(cl)
            if n == 1:
               massegebox.showinfo("Delete", 'Item deleted successfully')
           
            else: massegebox.showwarning("Delete", 'Unable to remove item, pleace try again')
               
           
           
            pass
       

    def fsave(self):
        self.employee.insert_pais(self.txtID.get(),self.txtName.get(), self.txtEmail.get(), self.txtentry.get(), self.txtmanage.get())
        self.textbox1()

    def fcancel(self):
       pass

    def create_widgets(self):
     frame1 = Frame(self, bg="#bfdaff")
     frame1.place(x=0, y=0, width=90, height=550)

     self.btnnew=Button(frame1, text="New", command= self.fnew, bg="blue", fg="white")
     self.btnnew.place(x=5,y=50, width=80, height=30)

     self.btnnew=Button(frame1, text="Add", command= self.fadd, bg="blue", fg="white")
     self.btnnew.place(x=5,y=90, width=80, height=30)

     self.btnnew=Button(frame1, text="Delete", command= self.fdelete, bg="blue", fg="white")
     self.btnnew.place(x=5,y=130, width=80, height=30)



     frame2 = Frame (self, bg="#d3dde3")
     frame2.place(x=95, y=0, width=150, height=550)

     label1 = Label(frame2, text="ID: ")
     label1.place(x=3, y=5)
     self.txtID=Entry(frame2)
     self.txtID.place(x=2, y=25, width=50, height=20)

     label2 = Label(frame2, text="Name: ")
     label2.place(x=3, y=55)
     self.txtname=Entry(frame2)
     self.txtname.place(x=2, y=75, width=50, height=20)

     label3 = Label(frame2, text="Email: ")
     label3.place(x=3, y=105)
     self.txtemail=Entry(frame2)
     self.txtemail.place(x=2, y=125, width=100, height=20)

     label4 = Label(frame2, text="Time worked: ")
     label4.place(x=3, y=155)
     self.txttime=Entry(frame2)
     self.txttime.place(x=2, y=175, width=100, height=20)

     label5 = Label(frame2, text="Entry date: ")
     label5.place(x=3, y=205)
     self.txtentry=Entry(frame2)
     self.txtentry.place(x=2, y=225, width=50, height=20)

     label5= Label(frame2, text="Entry date: ")
     label5.place(x=3, y=205)
     self.txtmanage=Entry(frame2)
     self.txtmanage.place(x=2, y=275, width=50, height=20)

   
     self.bsave=Button(frame2, text="Save", command= self.fsave, bg="blue", fg="white")
     self.bsave.place(x=10, y=270, width=60, height=30)

     self.bcancel=Button(frame2, text="Cancel", command= self.fcancel, bg="blue", fg="white")
     self.bcancel.place(x=80, y=270, width=60, height=30)

     self.grid = ttk.Treeview(self, columns=("Name", "Email", "Time worked", "Entry date","Manager ID"))

     self.grid.column("#0" ,width=50)
     self.grid.column("Name" ,width=90, anchor=CENTER)
     self.grid.column("Email" ,width=90, anchor=CENTER)
     self.grid.column("Time worked" ,width=90, anchor=CENTER)
     self.grid.column("Entry date" ,width=90, anchor=CENTER)
     self.grid.column("Manager ID" ,width=90, anchor=CENTER)

     self.grid.heading("#0", text="ID", anchor=CENTER)
     self.grid.heading("Name", text="Name", anchor=CENTER)
     self.grid.heading("Email", text="Email", anchor=CENTER)
     self.grid.heading("Time worked", text="Time worked", anchor=CENTER)
     self.grid.heading("Manager ID", text="Manager ID", anchor=CENTER)
     self.grid.place(x=247, y=0, width=520, height=559)
     










