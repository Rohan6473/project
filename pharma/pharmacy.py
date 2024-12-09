
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1250x800+0+0") 

        self.addmed_var=StringVar()
        self.refmed_var=StringVar()

        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()

        lbltitle=Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM ",bd=15,relief=RIDGE,
                       bg='white',fg='darkgreen',font=('times new roman',50,'bold'),padx=2,pady=4) 
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open('C:\\Users\\rohan\\Desktop\\pharma\\pharm.png')
        img1=img1.resize((70,70),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=15,y=20)

        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",
                                font=('arial',12,'bold'))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1355,height=65)
        
        btnAddData=Button(ButtonFrame,text="Medicine Add",font=('arial',11,'bold'),bg="darkgreen",fg="white",command=self.Add_data)
        btnAddData.grid(row=0,column=0)

        btnUpdateMed=Button(ButtonFrame,text="UPDATE",font=('arial',11,'bold'),width=13,bg="darkgreen",fg="white",command=self.UpdateMed)
        btnUpdateMed.grid(row=0,column=1)

        btnDeleteMed=Button(ButtonFrame,text="DELETE",font=('arial',11,'bold'),width=13,bg="red",fg="white",command=self.delete)
        btnDeleteMed.grid(row=0,column=2)

        btnresetMed=Button(ButtonFrame,text="RESET",font=('arial',11,'bold'),width=13,bg="darkgreen",fg="white",command=self.reset)
        btnresetMed.grid(row=0,column=3)

        btnExitMed=Button(ButtonFrame,text="EXIT",font=('arial',11,'bold'),width=13,bg="darkgreen",fg="white")
        btnExitMed.grid(row=0,column=4)

        lblSearch=Label(ButtonFrame,font=('arial',17,'bold'),text="Search BY",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=11,font=('arial',16,'bold'),state="readonly")
        search_combo['values']=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        self.searchTxt=StringVar()
        txtsearch=Entry(ButtonFrame,textvariable=self.searchTxt,bd=3,relief=RIDGE,width=11,font=('arial',16,'bold'))
        txtsearch.grid(row=0,column=7)

        searchbtn=Button(ButtonFrame,text="SEARCH",font=('arial',11,'bold'),width=13,bg="darkgreen",fg="white",command=self.search_data)
        searchbtn.grid(row=0,column=8)

        showAll=Button(ButtonFrame,text="SHOW ALL",font=('arial',11,'bold'),width=13,bg="darkgreen",fg="white",command=self.fetch_data)
        showAll.grid(row=0,column=9)

        lblrefno=Label(DataFrameLeft,font=('arial',11,'bold'),text="Reference No",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="12345@Rs",database="rohandb")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row=my_cursor.fetchall()

        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=27,font=('arial',12,'bold'),state="readonly")
        ref_combo['values']=("Ref","Medname","Lot")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

        lblrefno=Label(DataFrameLeft,font=('arial',11,'bold'),text="Company Name",padx=2)
        lblrefno.grid(row=1,column=0,sticky=W)

        txtcompanyname=Entry(DataFrameLeft,textvariable=self.cmpName_var,bd=3,relief=RIDGE,width=30,font=('arial',12,'bold'))
        txtcompanyname.grid(row=1,column=1)

        lblTypeMedicine=Label(DataFrameLeft,font=('arial',11,'bold'),text="Type Of Medicine",padx=2)
        lblTypeMedicine.grid(row=2,column=0,sticky=W)

        comTypeMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,width=27,font=('arial',12,'bold'),state="readonly")
        comTypeMedicine['values']=("Tablet","Liquid","Capsules","Topical Medicines"," Drops","Inhales","Injection")
        comTypeMedicine.grid(row=2,column=1)
        comTypeMedicine.current(0)

        conn=mysql.connector.connect(host="localhost",username="root",password="12345@Rs",database="rohandb")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med=my_cursor.fetchall()

        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,width=27,font=('arial',12,'bold'),state="readonly")
        comMedicineName['values']=("Ref","Mesname","colour")
        comMedicineName.grid(row=3,column=1)
        comMedicineName.current(0)

        lbllotno=Label(DataFrameLeft,font=('arial',11,'bold'),text="Lot no",padx=2,pady=6)
        lbllotno.grid(row=5,column=0,sticky=W)
        txtLotno=Entry(DataFrameLeft,textvariable=self.lot_var,bd=2,relief=RIDGE,width=29,font=('arial',12,'bold'),bg="white",)
        txtLotno.grid(row=5,column=1)

        lblIssueDate=Label(DataFrameLeft,font=('arial',11,'bold'),text="Issue Date",padx=2,pady=6)
        lblIssueDate.grid(row=6,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,bd=2,relief=RIDGE,width=29,font=('arial',12,'bold'),bg="white",)
        txtIssueDate.grid(row=6,column=1)

        lblExpDate=Label(DataFrameLeft,font=('arial',11,'bold'),text="Exp Date",padx=2,pady=6)
        lblExpDate.grid(row=7,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,bd=2,textvariable=self.expdate_var,relief=RIDGE,width=29,font=('arial',12,'bold'),bg="white",)
        txtExpDate.grid(row=7,column=1)
    
        lblSideEffect=Label(DataFrameLeft,font=('arial',11,'bold'),text="Side Effect",padx=2,pady=6)
        lblSideEffect.grid(row=9,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,bd=2,relief=RIDGE,width=29,font=('arial',12,'bold'),bg="white",)
        txtSideEffect.grid(row=9,column=1)

        lblPrecWarning=Label(DataFrameLeft,font=('arial',11,'bold'),text="Prec&Warning",padx=2,pady=6)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPreWarning=Entry(DataFrameLeft,textvariable=self.warning_var,bd=2,relief=RIDGE,width=29,font=('arial',12,'bold'),bg="white",)
        txtPreWarning.grid(row=0,column=3)
    
        lblDosage=Label(DataFrameLeft,font=('arial',11,'bold'),text="Dosage",padx=2,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,bd=2,textvariable=self.dosage_var,relief=RIDGE,width=29,font=('arial',12,'bold'),bg="white",)
        txtDosage.grid(row=1,column=3)

        lblPrice=Label(DataFrameLeft,font=('arial',11,'bold'),text="Price",padx=2,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,bd=2,textvariable=self.price_var,relief=RIDGE,width=29,font=('arial',12,'bold'),bg="white",)
        txtPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFrameLeft,font=('arial',11,'bold'),text="Product QT",padx=2,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQT=Entry(DataFrameLeft,textvariable=self.product_var,bd=2,relief=RIDGE,width=29,font=('arial',12,'bold'),bg="white",)
        txtProductQT.grid(row=3,column=3,sticky=W)

        lblUses=Label(DataFrameLeft,font=('arial',11,'bold'),text="Uses",padx=2,pady=6)
        lblUses.grid(row=8,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,bd=2,textvariable=self.uses_var,relief=RIDGE,width=29,font=('arial',12,'bold'),bg="white",)
        txtUses.grid(row=8,column=1)

        lblMedicineName=Label(DataFrameLeft,font=('arial',11,'bold'),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        img2=Image.open('C:\\Users\\rohan\\Desktop\\pharma\\bott.jpeg')
        img2=img2.resize((150,135),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=485,y=330)

        img3=Image.open('C:\\Users\\rohan\\Desktop\\pharma\\ecg.jpeg')
        img3=img3.resize((150,135),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=630,y=330)

        img4=Image.open('C:\\Users\\rohan\\Desktop\\pharma\\tab.jpeg')
        img4=img4.resize((150,135),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=730,y=330)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine And Department",fg="darkgreen",
                                font=('arial',12,'bold'))
        DataFrameRight.place(x=910,y=5,width=400,height=350)

        img5=Image.open('C:\\Users\\rohan\\Desktop\\pharma\\tabb.jpeg')
        img5=img5.resize((200,75),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=960,y=160)

        img6=Image.open('C:\\Users\\rohan\\Desktop\\pharma\\bott.jpeg')
        img6=img6.resize((150,75),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(self.root,image=self.photoimg6,borderwidth=0)
        b1.place(x=1160,y=160)

        lblrefno=Label(DataFrameRight,font=('arial',11,'bold'),text="Reference no")
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataFrameRight,textvariable=self.refmed_var,bd=2,relief=RIDGE,width=14,font=('arial',12,'bold'),bg="white")
        txtrefno.place(x=135,y=80)

        lblmedName=Label(DataFrameRight,font=('arial',11,'bold'),text="Medicine Name")
        lblmedName.place(x=0,y=110)
        txtmedName=Entry(DataFrameRight,textvariable=self.addmed_var,bd=2,relief=RIDGE,width=14,font=('arial',12,'bold'),bg="white")
        txtmedName.place(x=135,y=110)

        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=210,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,columns=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=80)
        self.medicine_table.column("medname",width=80)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=220,y=150,width=140,height=160)

        btnAddmed=Button(down_frame,text="ADD",font=('arial',11,'bold'),bg="lime",fg="white",width=14,pady=2,command=self.AddMed)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="UPDATE",font=('arial',11,'bold'),bg="purple",fg="white",width=14,pady=2,command=self.UpdateMed)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="DELETE",font=('arial',11,'bold'),bg="red",fg="white",width=14,pady=2,command=self.DeleteMed)
        btnDeletemed.grid(row=2,column=0)
    
        btnClearmed=Button(down_frame,text="CLEAR",font=('arial',11,'bold'),bg="orange",fg="white",width=14,pady=2,command=self.ClearMed)
        btnClearmed.grid(row=3,column=0)

        Framedetails=Frame(self.root,bd=7,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1400,height=115)

        Table_frame=Frame(self.root,bd=4,relief=RIDGE)
        Table_frame.place(x=0,y=580,width=1355,height=110)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("ref","companyName","type","tabletName","lot no","issuedate",
                                        "expdate","uses","sideeffect","warning","dosage","price","productqt"),
                                        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)        
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table['show']="headings"

        self.pharmacy_table.heading("ref",text="Reference no")
        self.pharmacy_table.heading("companyName",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("lot no",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp date")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.heading("uses",text="uses")
        self.pharmacy_table.heading("tabletName",text="Tablet Name")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("ref",width=80)
        self.pharmacy_table.column("companyName",width=80)
        self.pharmacy_table.column("type",width=80)
        self.pharmacy_table.column("lot no",width=80)
        self.pharmacy_table.column("issuedate",width=80)
        self.pharmacy_table.column("expdate",width=80)
        self.pharmacy_table.column("sideeffect",width=80)
        self.pharmacy_table.column("warning",width=80)
        self.pharmacy_table.column("dosage",width=80)
        self.pharmacy_table.column("price",width=80)
        self.pharmacy_table.column("productqt",width=80)
        self.pharmacy_table.column("uses",width=80)
        self.pharmacy_table.column("tabletName",width=80)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345@Rs",database="rohandb")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                         self.refmed_var.get(),
                         self.addmed_var.get(),
                         ))
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success","Medicine added")

    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345@Rs",database="rohandb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refmed_var.set(row[0])
        self.addmed_var.set(row[1])
    
    def UpdateMed(self):
        if self.refmed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345@Rs",database="rohandb")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                                                          self.addmed_var.get(),
                                                          self.refmed_var.get(),        
            ))   
            conn.commit()
            self.fetch_dataMed()
            conn.close() 
            messagebox.showinfo("Success","Medicine has been updated")
    
    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345@Rs",database="rohandb")
        my_cursor=conn.cursor()
        sql="delete from pharma where Ref=%s"
        val=(self.refmed_var.get(),)
        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_dataMed()
        conn.close()

    def ClearMed(self):
        self.refmed_var.set("")
        self.addmed_var.set("")
    
    def Add_data(self):
        if self.ref_var.get=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345@Rs",database="rohandb")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            self.ref_var.get(),
                            self.cmpName_var.get(),
                            self.typeMed_var.get(),
                            self.medName_var.get(),
                            self.lot_var.get(),
                            self.issuedate_var.get(),
                            self.expdate_var.get(),
                            self.uses_var.get(),
                            self.sideEffect_var.get(),
                            self.warning_var.get(),
                            self.dosage_var.get(),
                            self.price_var.get(),
                            self.product_var.get(),
                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Data has been inserted")

    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="12345@Rs",database="rohandb")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from pharmacy")
            row=my_cursor.fetchall()
            if len(row)!=0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in row:
                    self.pharmacy_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]
        self.ref_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row[3])
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.product_var.set(row[12]),

    def UpdateMed(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345@Rs",database="rohandb")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set cmpName=%s,typeMed=%s,medName=%s,LotNo=%s,Issuedate=%s,Expdate=%s,uses=%s,sideeffect=%s,warning=%s,dosage=%s,price=%s,product=%s where Ref_no=%s",(
                            self.cmpName_var.get(),
                            self.typeMed_var.get(),
                            self.medName_var.get(),
                            self.lot_var.get(),
                            self.issuedate_var.get(),
                            self.expdate_var.get(),
                            self.uses_var.get(),
                            self.sideEffect_var.get(),
                            self.warning_var.get(),
                            self.dosage_var.get(),
                            self.price_var.get(),
                            self.product_var.get(),
                            self.ref_var.get(),       
            ))   
            conn.commit()
            self.fetch_data()
            conn.close() 
            messagebox.showinfo("Success","Medicine has been updated")

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345@Rs",database="rohandb")
        my_cursor=conn.cursor()
        sql="delete from pharmacy where Ref_no=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Deleted succesfully")

    def reset(self):
        #self.ref_var.set(""),
        self.ref_var.set(""),
        #self.cmpName_var.set(""),
        #self.typeMed_var.set("")
        self.medName_var.set("")
        self.lot_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.uses_var.set("")
        self.sideEffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.product_var.set("")

    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345@Rs",database="rohandb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy where "+str(self.search_var.get())+"LIKE"+str(self.searchTxt.get())+"%")

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()  
