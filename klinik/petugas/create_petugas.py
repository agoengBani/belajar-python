from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
root.title("FORM PETUGAS")

db = mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="klinik"
)

cursor = db.cursor()

def insert():
       insert_query ="INSERT INTO petugas (nama,jenis_kelamin,umur,berat_badan,tinggi_badan,petugas) VALUES (%s, %s, %s, %s, %s, %s)"
       data = (nama.get(),jenis_kelamin.get(),umur.get(),berat_badan.get(),tinggi_badan.get(),petugas.get())
       cursor.execute(insert_query, data)
       db.commit()

       messagebox.showinfo("Success", "Data updated successfully")
       root.destroy()



# label1 = Label(root, text="ID Petugas:")
# label1.grid(column=0, row=0, padx=5, pady=5)
# id_petugas = Entry(root, width=30)
# id_petugas.grid(column=1, row=0, padx=5, pady=5)

label2 = Label(root, text="Nama Petugas:")
label2.grid(column=0, row=1, padx=5, pady=5)
nama = Entry(root, width=30)
nama.grid(column=1, row=1, padx=5, pady=5)

label3 = Label(root, text="Jenis Kelamin:")
label3.grid(column=0, row=2, padx=5, pady=5)
jenis_kelamin = Entry(root, width=30)
jenis_kelamin.grid(column=1, row=2, padx=5, pady=5)

label4 = Label(root, text="Umur:")
label4.grid(column=0, row=3, padx=5, pady=5)
umur = Entry(root, width=30)
umur.grid(column=1, row=3, padx=5, pady=5)

label5 = Label(root, text="Berat Badan:")
label5.grid(column=0, row=4, padx=5, pady=5)
berat_badan = Entry(root, width=30)
berat_badan.grid(column=1, row=4, padx=5, pady=5)

label6 = Label(root, text="Tinggi Badan:")
label6.grid(column=0, row=5, padx=5, pady=5)
tinggi_badan = Entry(root, width=30)
tinggi_badan.grid(column=1, row=5, padx=5, pady=5)

label7 = Label(root, text="Jenis Petugas:")
label7.grid(column=0, row=6, padx=5, pady=5)
petugas = Entry(root, width=30)
petugas.grid(column=1, row=6, padx=5, pady=5)

loan_button = Button(root, text="Simpan", command=insert)
loan_button.grid(column=0, row=7, columnspan=2, padx=5, pady=5)
root.mainloop()