from tkinter import *
import mysql.connector

root = Tk()
root.title("Form Obat")

db = mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="klinik"
)

# read
cursor = db.cursor()
sql = "SELECT * FROM obat"
cursor.execute(sql)
results = cursor.fetchall()

def update(id):
   cursor = db.cursor()
   sql = "UPDATE obat SET nama_obat=%s, klasifikasi_obat=%s, jenis_obat=%s, harga=%s, dosis=%s, resep=%s WHERE id_obat=%s"
   val = (id, )
   cursor.execute(sql, val)
   db.commit()

# delete
def delete(id):
   cursor = db.cursor()
   sql = "DELETE FROM obat WHERE id_obat=%s"
   val = (id, )
   cursor.execute(sql, val)
   db.commit()

Label(root, text="NO", borderwidth=1, relief=SUNKEN, width=20).grid(row=0)
Label(root, text="Id Obat", borderwidth=1, relief=SUNKEN, width=20).grid(row=0, column=1)
Label(root, text="Nama Obat", borderwidth=1, relief=SUNKEN, width=20).grid(row=0, column=2)
Label(root, text="Klasifikasi", borderwidth=1, relief=SUNKEN, width=20).grid(row=0, column=3)
Label(root, text="Jenis Obat", borderwidth=1, relief=SUNKEN, width=20).grid(row=0, column=4)
Label(root, text="Harga Obat", borderwidth=1, relief=SUNKEN, width=20).grid(row=0, column=5)
Label(root, text="Dosis", borderwidth=1, relief=SUNKEN, width=20).grid(row=0, column=6)
Label(root, text="Resep", borderwidth=1, relief=SUNKEN, width=20).grid(row=0, column=7)
Label(root, text="Aksi", borderwidth=1, relief=SUNKEN, width=20).grid(row=0, column=8)

no=0

for data in results:
   no+=1
   Label(root, text=no, borderwidth=1, relief=SUNKEN, width=20).grid(row=no)
   Label(root, text=data[0], borderwidth=1, relief=SUNKEN, width=20).grid(row=no, column=1)
   Label(root, text=data[1], borderwidth=1, relief=SUNKEN, width=20).grid(row=no, column=2)
   Label(root, text=data[2], borderwidth=1, relief=SUNKEN, width=20).grid(row=no, column=3)
   Label(root, text=data[3], borderwidth=1, relief=SUNKEN, width=20).grid(row=no, column=4)
   Label(root, text=data[4], borderwidth=1, relief=SUNKEN, width=20).grid(row=no, column=5)
   Label(root, text=data[5], borderwidth=1, relief=SUNKEN, width=20).grid(row=no, column=6)
   Label(root, text=data[6], borderwidth=1, relief=SUNKEN, width=20).grid(row=no, column=7)
   Button(root, text="Delete", command=lambda id=data[0] :delete(id)).grid(row=no, column=8)


root.mainloop()