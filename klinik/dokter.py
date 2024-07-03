from tkinter import *
import mysql.connector
db = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="klinik"
)
cursor = db.cursor()
def insert():
       insert_query ="INSERT INTO dokter (id_dokter,nama,jenis_kelamin,umur,poly,jadwal) VALUES (%s, %s, %s, %s, %s, %s)"
       data = (id_dokter.get(),nama.get(),jenis_kelamin.get(),umur.get(),poly.get(),jadwal.get())
       cursor.execute(insert_query, data)
       db.commit()

root = Tk()
root.title("FORM DOKTER")

label1 = Label(root, text="ID Dokter:")
label1.grid(column=0, row=0, padx=5, pady=5)
id_dokter = Entry(root, width=30)
id_dokter.grid(column=1, row=0, padx=5, pady=5)

label2 = Label(root, text="Nama Dokter:")
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

label5 = Label(root, text="Poly:")
label5.grid(column=0, row=4, padx=5, pady=5)
poly = Entry(root, width=30)
poly.grid(column=1, row=4, padx=5, pady=5)

label6 = Label(root, text="Jadwal:")
label6.grid(column=0, row=5, padx=5, pady=5)
jadwal = Entry(root, width=30)
jadwal.grid(column=1, row=5, padx=5, pady=5)

loan_button = Button(root, text="Simpan", command=insert)
loan_button.grid(column=0, row=7, columnspan=2, padx=5, pady=5)
root.mainloop()