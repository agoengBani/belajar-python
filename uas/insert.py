from tkinter import messagebox
import mysql.connector
from tkinter import *
from datetime import datetime

root = Tk()
root.title("INSERT OBAT")

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='uas_2255201039'
)

cursor = db.cursor()

def insert():
    insert_query = "INSERT INTO data_pajak_hotel (no_reg_objek, npwdp, rekening, nama_hotel, alamat, kelurahan, kecamatan, pembukuan, username, created_at, updated_at, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = (no_reg_objek.get(), npwdp.get(), rekening.get(), nama_hotel.get(), alamat.get(), kelurahan.get(), kecamatan.get(), pembukuan.get(), username.get(), current_time, current_time, status.get())
    cursor.execute(insert_query, data)
    db.commit()

    messagebox.showinfo("Success", "Insert Data Successfully")
    root.destroy()

label2 = Label(root, text="No Reg Objek:")
label2.grid(column=0, row=1, padx=5, pady=5)
no_reg_objek = Entry(root, width=30)
no_reg_objek.grid(column=1, row=1, padx=5, pady=5)

label3 = Label(root, text="NPWDP:")
label3.grid(column=0, row=2, padx=5, pady=5)
npwdp = Entry(root, width=30)
npwdp.grid(column=1, row=2, padx=5, pady=5)

label4 = Label(root, text="REKENING:")
label4.grid(column=0, row=3, padx=5, pady=5)
rekening = Entry(root, width=30)
rekening.grid(column=1, row=3, padx=5, pady=5)

label5 = Label(root, text="NAMA HOTEL:")
label5.grid(column=0, row=4, padx=5, pady=5)
nama_hotel = Entry(root, width=30)
nama_hotel.grid(column=1, row=4, padx=5, pady=5)

label6 = Label(root, text="ALAMAT:")
label6.grid(column=0, row=5, padx=5, pady=5)
alamat = Entry(root, width=30)
alamat.grid(column=1, row=5, padx=5, pady=5)

label7 = Label(root, text="KELURAHAN:")
label7.grid(column=0, row=6, padx=5, pady=5)
kelurahan = Entry(root, width=30)
kelurahan.grid(column=1, row=6, padx=5, pady=5)

label8 = Label(root, text="KECAMATAN:")
label8.grid(column=0, row=7, padx=5, pady=5)
kecamatan = Entry(root, width=30)
kecamatan.grid(column=1, row=7, padx=5, pady=5)

label9 = Label(root, text="PEMBUKUAN:")
label9.grid(column=0, row=8, padx=5, pady=5)
pembukuan = Entry(root, width=30)
pembukuan.grid(column=1, row=8, padx=5, pady=5)

label10 = Label(root, text="USERNAME:")
label10.grid(column=0, row=9, padx=5, pady=5)
username = Entry(root, width=30)
username.grid(column=1, row=9, padx=5, pady=5)

label11 = Label(root, text="STATUS:")
label11.grid(column=0, row=10, padx=5, pady=5)
status = StringVar()
status.set("Y")

status_aktif = Radiobutton(root, text="Y", variable=status, value="Y")
status_aktif.grid(column=1, row=10, padx=5, pady=5)

status_tidak_aktif = Radiobutton(root, text="N", variable=status, value="N")
status_tidak_aktif.grid(column=1, row=11, padx=5, pady=5)


loan_button = Button(root, text="Simpan", command=insert)
loan_button.grid(column=0, row=12, columnspan=2, padx=5, pady=5)

root.mainloop()
