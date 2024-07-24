from tkinter import *
from tkinter import messagebox
import subprocess
import mysql.connector

root = Tk()
root.title("Form Obat")

db = mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="klinik"
)

# Create data
def create():
    subprocess.run(["python3", "create_obat.py"])

# Read data
cursor = db.cursor()
sql = "SELECT * FROM obat"
cursor.execute(sql)
results = cursor.fetchall()

# Update data
def update(id, nama, klasifikasi, jenis, harga, dosis, resep):
    def save():
        new_nama = entry_nama.get()
        new_klasifikasi = entry_klasifikasi.get()
        new_jenis = entry_jenis.get()
        new_harga = entry_harga.get()
        new_dosis = entry_dosis.get()
        new_resep = entry_resep.get()

        cursor = db.cursor()
        sql = "UPDATE obat SET nama_obat=%s, klasifikasi_obat=%s, jenis_obat=%s, harga=%s, dosis=%s, resep=%s WHERE id_obat=%s"
        val = (new_nama, new_klasifikasi, new_jenis, new_harga, new_dosis, new_resep, id)
        cursor.execute(sql, val)
        db.commit()
        
        # edit_window.destroy()
        messagebox.showinfo("Success", "Data updated successfully")
        root.destroy()
        # main()

    edit_window = Toplevel(root)
    edit_window.title("Edit Data")

    Label(edit_window, text="Nama Obat").grid(row=0, column=0)
    entry_nama = Entry(edit_window)
    entry_nama.grid(row=0, column=1)
    entry_nama.insert(0, nama)

    Label(edit_window, text="Klasifikasi").grid(row=1, column=0)
    entry_klasifikasi = Entry(edit_window)
    entry_klasifikasi.grid(row=1, column=1)
    entry_klasifikasi.insert(0, klasifikasi)

    Label(edit_window, text="Jenis Obat").grid(row=2, column=0)
    entry_jenis = Entry(edit_window)
    entry_jenis.grid(row=2, column=1)
    entry_jenis.insert(0, jenis)

    Label(edit_window, text="Harga Obat").grid(row=3, column=0)
    entry_harga = Entry(edit_window)
    entry_harga.grid(row=3, column=1)
    entry_harga.insert(0, harga)

    Label(edit_window, text="Dosis").grid(row=4, column=0)
    entry_dosis = Entry(edit_window)
    entry_dosis.grid(row=4, column=1)
    entry_dosis.insert(0, dosis)

    Label(edit_window, text="Resep").grid(row=5, column=0)
    entry_resep = Entry(edit_window)
    entry_resep.grid(row=5, column=1)
    entry_resep.insert(0, resep)

    Button(edit_window, text="Save", command=save).grid(row=6, columnspan=2)

# Delete data
def delete(id):
    cursor = db.cursor()
    sql = "DELETE FROM obat WHERE id_obat=%s"
    val = (id, )
    cursor.execute(sql, val)
    db.commit()
    messagebox.showinfo("Success", "Data deleted successfully")
    root.destroy()
    # main()

# Main window
def main():
    Button(root, text="Create", command=create).grid(row=0, column=10)

    Label(root, text="NO", borderwidth=1, relief=SUNKEN, width=10).grid(row=0)
    Label(root, text="Id Obat", borderwidth=1, relief=SUNKEN, width=10).grid(row=0, column=1)
    Label(root, text="Nama Obat", borderwidth=1, relief=SUNKEN, width=10).grid(row=0, column=2)
    Label(root, text="Klasifikasi", borderwidth=1, relief=SUNKEN, width=10).grid(row=0, column=3)
    Label(root, text="Jenis Obat", borderwidth=1, relief=SUNKEN, width=10).grid(row=0, column=4)
    Label(root, text="Harga Obat", borderwidth=1, relief=SUNKEN, width=10).grid(row=0, column=5)
    Label(root, text="Dosis", borderwidth=1, relief=SUNKEN, width=10).grid(row=0, column=6)
    Label(root, text="Resep", borderwidth=1, relief=SUNKEN, width=10).grid(row=0, column=7)
    Label(root, text="Aksi", borderwidth=1, relief=SUNKEN, width=10).grid(row=0, column=8, columnspan=2)

    no = 0

    for data in results:
        no += 1
        Label(root, text=no, borderwidth=1, relief=SUNKEN, width=10).grid(row=no)
        Label(root, text=data[0], borderwidth=1, relief=SUNKEN, width=10).grid(row=no, column=1)
        Label(root, text=data[1], borderwidth=1, relief=SUNKEN, width=10).grid(row=no, column=2)
        Label(root, text=data[2], borderwidth=1, relief=SUNKEN, width=10).grid(row=no, column=3)
        Label(root, text=data[3], borderwidth=1, relief=SUNKEN, width=10).grid(row=no, column=4)
        Label(root, text=data[4], borderwidth=1, relief=SUNKEN, width=10).grid(row=no, column=5)
        Label(root, text=data[5], borderwidth=1, relief=SUNKEN, width=10).grid(row=no, column=6)
        Label(root, text=data[6], borderwidth=1, relief=SUNKEN, width=10).grid(row=no, column=7)
        Button(root, text="Edit",  command=lambda id=data[0], nama=data[1], klasifikasi=data[2], jenis=data[3], harga=data[4], dosis=data[5], resep=data[6] :update(id, nama, klasifikasi, jenis, harga, dosis, resep)).grid(row=no, column=8)
        Button(root, text="Delete", command=lambda id=data[0] :delete(id)).grid(row=no, column=9)

    root.mainloop()

main()
