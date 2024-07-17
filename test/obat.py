from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '',
    database = 'klinik'
)

c = db.cursor()

if db.is_connected():
    messagebox.showinfo("INFO","BERHASIL TERKONEKSI DENGAN DATABASE")
else:
    messagebox.showinfo("INFO","GAGAL TERKONEKSI DENGAN DATABASE")

from tkinter import *
import tkinter.font

root = Tk()
root.geometry("300x600")

changefont = tkinter.font.Font(size=10)
judl = Label(root,text = "PEMBUATAN OBAT",font =changefont)
judl.place(x =40,y = 10)

labelfr = LabelFrame(root,text = "result",padx=20,pady=20)
labelfr.place(x = 60,y = 380)

namaObat = Label(root,text = "Nama Obat")
klasifikasiObat = Label(root,text = "Klasifikasi Obat")
jenisObat = Label(root,text = "Jenis Obat")
harga = Label(root,text = "Harga")
dosis = Label(root,text = "Dosis")
resep = Label(root,text = "Resep" )

e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root,width=40)
e4 = Entry(root,width=40)
e5 = Entry(root,width=40)
e6 = Entry(root,width=40)
# e7 = Entry(root)

namaObat.place(x = 20, y =50)
klasifikasiObat.place(x = 20, y =90)
jenisObat.place(x = 20, y =130)
harga.place(x = 20, y =170)
dosis.place(x = 20, y =210)
resep.place(x = 20, y =250)

e1.place(x = 20, y = 70)
e2.place(x = 20, y = 110)
e3.place(x = 20, y = 150)
e4.place(x = 20, y = 190)
e5.place(x = 20, y = 230)
e6.place(x = 20, y = 270)
# e7.place(x = 20, y = 30)

r = StringVar()
r.set(None)

# rb = Radiobutton(root,text = "male",variable=r,value="male").place(x = 20,y =310 )
# rb2 = Radiobutton(root,text = "female",variable=r,value="female").place(x = 80,y =310 )

def masuk():
    namaObat = e1.get()
    klasifikasiObat = e2.get()
    jenisObat = e3.get()
    harga = e4.get()
    dosis = e5.get()
    resep = e6.get()
    # id = e7.get()

    insert_query = "INSERT INTO obat (nama_obat, klasifikasi_obat, jenis_obat, harga, dosis, resep) VALUES (%s, %s, %s, %s, %s, %s)"
    vals = (namaObat,klasifikasiObat,jenisObat,harga,dosis,resep)
    c.execute(insert_query,vals)
    db.commit()

# def deleteData():
#     user_id = e6.get()

#     delete_query = "DELETE FROM anggota WHERE resep =" + user_id
#     c.execute(delete_query)
#     db.commit()

# def updateData():
#     namaObat = e1.get()
#     klasifikasiObat = e2.get()
#     jenisObat = e3.get()
#     harga = e4.get()
#     dosis = e5.get()
#     resep = e6.get()
#     gender =r.get()

#     update_query = "UPDATE anggota SET nama=%s,nick=%s,jenisObat=%s,harga=%s,dosis=%s,gender=%s WHERE resep=%s"
#     vals = (namaObat,klasifikasiObat,jenisObat,harga,dosis,gender,resep)
#     c.execute(update_query,vals)
#     db.commit()
    
# def clear():
#     for widget in root.winfo_children():
#         if isinstance(widget,Entry):
#             widget.delete(0,'end')
#         if isinstance(widget,Radiobutton):
#             r.set(None)

# def searchData():
#     # clear fields
#     e1.delete(0,END)
#     e2.delete(0,END)
#     e3.delete(0,END)
#     e4.delete(0,END)
#     e5.delete(0,END)
#     e6.delete(0,END)
#     r.set(0)

#     # search
#     user_id = e6.get()
#     search_query = "SELECT * FROM anggota WHERE resep =" + user_id
#     c.execute(search_query)
#     userdata = c.fetchone()
#     e1.insert(0,userdata[0])
#     e2.insert(0,userdata[1])
#     e3.insert(0,userdata[2])
#     e4.insert(0,userdata[3])
#     e5.insert(0,userdata[4])
#     e6.insert(0,userdata[5])
#     r.set(0,userdata[6])


btn = Button(root,text = "submit",command=masuk).place(x = 10,y = 350)
# btn = Button(root,text = "delete",command=deleteData).place(x = 70,y = 350)
# btn = Button(root,text = "update",command=updateData).place(x = 125,y = 350)
# btn = Button(root,text = "clear",command=clear).place(x = 185,y = 350)
# btn = Button(root,text = "search",command=searchData).place(x = 10,y = 390)


root.mainloop()


