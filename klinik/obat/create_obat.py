from tkinter import messagebox
import mysql.connector
from tkinter import *

root = Tk()
root.title("INSERT OBAT")

db = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '',
    database = 'klinik'
)

cursor = db.cursor()

# if db.is_connected():
#     messagebox.showinfo("INFO","BERHASIL TERKONEKSI DENGAN DATABASE")
# else:
#     messagebox.showinfo("INFO","GAGAL TERKONEKSI DENGAN DATABASE")


def insert():
    insert_query = "INSERT INTO obat (nama_obat, klasifikasi_obat, jenis_obat, harga, dosis, resep) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (nama_obat.get(), klasifikasi_obat.get(), jenis_obat.get(), harga.get(), dosis.get(), resep.get())
    cursor.execute(insert_query, data)
    db.commit()

    messagebox.showinfo("Success", "Insert Data Successfully")
    root.destroy()


label2 = Label(root, text="Nama Obat:")
label2.grid(column=0, row=1, padx=5, pady=5)
nama_obat = Entry(root, width=30)
nama_obat.grid(column=1, row=1, padx=5, pady=5)

label3 = Label(root, text="Klasifikasi Obat:")
label3.grid(column=0, row=2, padx=5, pady=5)
klasifikasi_obat = Entry(root, width=30)
klasifikasi_obat.grid(column=1, row=2, padx=5, pady=5)

label4 = Label(root, text="Jenis Obat:")
label4.grid(column=0, row=3, padx=5, pady=5)
jenis_obat = Entry(root, width=30)
jenis_obat.grid(column=1, row=3, padx=5, pady=5)

label5 = Label(root, text="Harga:")
label5.grid(column=0, row=4, padx=5, pady=5)
harga = Entry(root, width=30)
harga.grid(column=1, row=4, padx=5, pady=5)

label6 = Label(root, text="Dosis:")
label6.grid(column=0, row=5, padx=5, pady=5)
dosis = Entry(root, width=30)
dosis.grid(column=1, row=5, padx=5, pady=5)

label7 = Label(root, text="Resep:")
label7.grid(column=0, row=6, padx=5, pady=5)
resep = Entry(root, width=30)
resep.grid(column=1, row=6, padx=5, pady=5)

loan_button = Button(root, text="Simpan", command=insert)
loan_button.grid(column=0, row=7, columnspan=2, padx=5, pady=5)

root.mainloop()