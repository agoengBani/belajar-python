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

r = StringVar()
r.set(None)

def masuk():
    namaObat = e1.get()
    klasifikasiObat = e2.get()
    jenisObat = e3.get()
    harga = e4.get()
    dosis = e5.get()
    resep = e6.get()

    insert_query = "INSERT INTO obat (nama_obat, klasifikasi_obat, jenis_obat, harga, dosis, resep) VALUES (%s, %s, %s, %s, %s, %s)"
    vals = (namaObat,klasifikasiObat,jenisObat,harga,dosis,resep)
    c.execute(insert_query,vals)
    db.commit()

btn = Button(root,text = "submit",command=masuk).place(x = 10,y = 350)

root.mainloop()