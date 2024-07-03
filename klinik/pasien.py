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
judl = Label(root,text = "PASIEN",font =changefont)
judl.place(x =40,y = 10)

labelfr = LabelFrame(root,text = "result",padx=20,pady=20)
labelfr.place(x = 60,y = 380)

nama_pasien = Label(root,text = "Nama Pasien")
jenis_kelamin = Label(root,text = "Jenis Kelamin")
umur = Label(root,text = "Umur")
berat_badan = Label(root,text = "Berat Badan")
tinggi_badan = Label(root,text = "Tinggi Badan")

e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root,width=40)
e4 = Entry(root,width=40)
e5 = Entry(root,width=40)

nama_pasien.place(x = 20, y =50)
jenis_kelamin.place(x = 20, y =90)
umur.place(x = 20, y =130)
berat_badan.place(x = 20, y =170)
tinggi_badan.place(x = 20, y =210)

e1.place(x = 20, y = 70)
e2.place(x = 20, y = 110)
e3.place(x = 20, y = 150)
e4.place(x = 20, y = 190)
e5.place(x = 20, y = 230)

r = StringVar()
r.set(None)

def masuk():
    nama_pasien = e1.get()
    jenis_kelamin = e2.get()
    umur = e3.get()
    berat_badan = e4.get()
    tinggi_badan = e5.get()

    insert_query = "INSERT INTO pasien (nama, jenis_kelamin, umur, berat_badan, tinggi_badan) VALUES (%s, %s, %s, %s, %s)"
    vals = (nama_pasien,jenis_kelamin,umur,berat_badan,tinggi_badan)
    c.execute(insert_query,vals)
    db.commit()

btn = Button(root,text = "submit",command=masuk).place(x = 10,y = 350)

root.mainloop()