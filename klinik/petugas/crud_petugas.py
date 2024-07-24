from tkinter import *
from tkinter import messagebox
import subprocess
import mysql.connector

root = Tk()
root.title("Form Petugas")

db = mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="klinik"
)

# Create data
def create():
    subprocess.run(["python3", "create_petugas.py"])

# Read data
cursor = db.cursor()
sql = "SELECT * FROM petugas"
cursor.execute(sql)
results = cursor.fetchall()

# Update data
def update(id, nama, umur, berat_badan, tinggi_badan, jenis_kelamin, petugas):
    def save():
        new_nama = entry_nama.get()
        new_umur = entry_umur.get()
        new_berat_badan = entry_berat.get()
        new_tinggi_badan = entry_tinggi_badan.get()
        new_jenis_kelamin = entry_jenis_kelamin.get()
        new_petugas = entry_petugas.get()

        cursor = db.cursor()
        sql = "UPDATE petugas SET nama=%s, umur=%s, berat_badan=%s, tinggi_badan=%s, jenis_kelamin=%s, petugas=%s WHERE id_petugas=%s"
        val = (new_nama, new_umur, new_berat_badan, new_tinggi_badan, new_jenis_kelamin, new_petugas, id)
        cursor.execute(sql, val)
        db.commit()
        
      #   edit_window.destroy()
        messagebox.showinfo("Success", "Data updated successfully")
      #   root.destroy()
        main()

    edit_window = Toplevel(root)
    edit_window.title("Edit Data")

    Label(edit_window, text="Nama petugas").grid(row=0, column=0)
    entry_nama = Entry(edit_window)
    entry_nama.grid(row=0, column=1)
    entry_nama.insert(0, nama)

    Label(edit_window, text="Umur").grid(row=1, column=0)
    entry_umur = Entry(edit_window)
    entry_umur.grid(row=1, column=1)
    entry_umur.insert(0, umur)

    Label(edit_window, text="Berat badan").grid(row=2, column=0)
    entry_berat = Entry(edit_window)
    entry_berat.grid(row=2, column=1)
    entry_berat.insert(0, berat_badan)

    Label(edit_window, text="Tinggi badan").grid(row=3, column=0)
    entry_tinggi_badan = Entry(edit_window)
    entry_tinggi_badan.grid(row=3, column=1)
    entry_tinggi_badan.insert(0, tinggi_badan)

    Label(edit_window, text="Jenis kelamin").grid(row=4, column=0)
    entry_jenis_kelamin = Entry(edit_window)
    entry_jenis_kelamin.grid(row=4, column=1)
    entry_jenis_kelamin.insert(0, jenis_kelamin)

    Label(edit_window, text="Petugas").grid(row=5, column=0)
    entry_petugas = Entry(edit_window)
    entry_petugas.grid(row=5, column=1)
    entry_petugas.insert(0, petugas)

    Button(edit_window, text="Save", command=save).grid(row=6, columnspan=2)

# Delete data
def delete(id):
    cursor = db.cursor()
    sql = "DELETE FROM petugas WHERE id_petugas=%s"
    val = (id, )
    cursor.execute(sql, val)
    db.commit()
    messagebox.showinfo("Success", "Data deleted successfully")
   #  root.destroy()
    main()

# Main window
def main():
    Button(root, text="Create", command=create).grid(row=0, column=10)

    Label(root, text="NO", borderwidth=1, relief=SUNKEN, width=10).grid(row=0)
    Label(root, text="Id Petugas", borderwidth=1, relief=SUNKEN, width=10).grid(row=0, column=1)
    Label(root, text="Nama Petugas", borderwidth=1, relief=SUNKEN, width=15).grid(row=0, column=2)
    Label(root, text="Umur", borderwidth=1, relief=SUNKEN, width=15).grid(row=0, column=3)
    Label(root, text="Berat Badan", borderwidth=1, relief=SUNKEN, width=15).grid(row=0, column=4)
    Label(root, text="Tinggi Badan", borderwidth=1, relief=SUNKEN, width=15).grid(row=0, column=5)
    Label(root, text="Jenis Kelamin", borderwidth=1, relief=SUNKEN, width=15).grid(row=0, column=6)
    Label(root, text="Petugas", borderwidth=1, relief=SUNKEN, width=15).grid(row=0, column=7)
    Label(root, text="Aksi", borderwidth=1, relief=SUNKEN, width=15).grid(row=0, column=8, columnspan=2)

    no = 0

    for data in results:
        no += 1
        Label(root, text=no, borderwidth=1, relief=SUNKEN, width=10).grid(row=no)
        Label(root, text=data[0], borderwidth=1, relief=SUNKEN, width=10).grid(row=no, column=1)
        Label(root, text=data[1], borderwidth=1, relief=SUNKEN, width=15).grid(row=no, column=2)
        Label(root, text=data[2], borderwidth=1, relief=SUNKEN, width=15).grid(row=no, column=3)
        Label(root, text=data[3], borderwidth=1, relief=SUNKEN, width=15).grid(row=no, column=4)
        Label(root, text=data[4], borderwidth=1, relief=SUNKEN, width=15).grid(row=no, column=5)
        Label(root, text=data[5], borderwidth=1, relief=SUNKEN, width=15).grid(row=no, column=6)
        Label(root, text=data[6], borderwidth=1, relief=SUNKEN, width=15).grid(row=no, column=7)
        Button(root, text="Edit",  command=lambda id=data[0], nama=data[1], umur=data[2], berat_badan=data[3], tinggi_badan=data[4], jenis_kelamin=data[5], petugas=data[6] :update(id, nama, umur, berat_badan, tinggi_badan, jenis_kelamin, petugas)).grid(row=no, column=8)
        Button(root, text="Delete", command=lambda id=data[0] :delete(id)).grid(row=no, column=9)

    root.mainloop()

main()
