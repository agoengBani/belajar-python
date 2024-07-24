from tkinter import *
from tkinter import messagebox
import subprocess
import mysql.connector

# Koneksi ke database
db = mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="uas_2255201039"
)

root = Tk()
root.title("DATA PAJAK HOTEL")

# Fungsi untuk membuka form insert data
def create():
    subprocess.run(["python3", "insert.py"])

# Fungsi untuk membaca data dari database
def read_data():
    cursor = db.cursor()
    sql = "SELECT * FROM data_pajak_hotel"
    cursor.execute(sql)
    return cursor.fetchall()

# Fungsi untuk memperbarui data di database
def update(id, no_reg_objek, npwdp, rekening, nama_hotel, alamat, kelurahan, kecamatan, pembukuan, username, status):
    def save():
        new_no_reg_objek = entry_no_reg_objek.get()
        new_npwdp = entry_npwdp.get()
        new_rekening = entry_rekening.get()
        new_nama_hotel = entry_nama_hotel.get()
        new_alamat = entry_alamat.get()
        new_kelurahan = entry_kelurahan.get()
        new_kecamatan = entry_kecamatan.get()
        new_pembukuan = entry_pembukuan.get()
        new_username = entry_username.get()
        new_status = status_var.get()

        cursor = db.cursor()
        sql = "UPDATE data_pajak_hotel SET no_reg_objek=%s, npwdp=%s, rekening=%s, nama_hotel=%s, alamat=%s, kelurahan=%s, kecamatan=%s, pembukuan=%s, username=%s, status=%s WHERE id=%s"
        val = (new_no_reg_objek, new_npwdp, new_rekening, new_nama_hotel, new_alamat, new_kelurahan, new_kecamatan, new_pembukuan, new_username, new_status, id)
        cursor.execute(sql, val)
        db.commit()

        messagebox.showinfo("Success", "Data updated successfully")
        edit_window.destroy()
        refresh()

    edit_window = Toplevel(root)
    edit_window.title("Edit Data")

    Label(edit_window, text="NO REG OBJEK").grid(row=0, column=0)
    entry_no_reg_objek = Entry(edit_window)
    entry_no_reg_objek.grid(row=0, column=1)
    entry_no_reg_objek.insert(0, no_reg_objek)

    Label(edit_window, text="NPWDP").grid(row=1, column=0)
    entry_npwdp = Entry(edit_window)
    entry_npwdp.grid(row=1, column=1)
    entry_npwdp.insert(0, npwdp)

    Label(edit_window, text="REKENING").grid(row=2, column=0)
    entry_rekening = Entry(edit_window)
    entry_rekening.grid(row=2, column=1)
    entry_rekening.insert(0, rekening)

    Label(edit_window, text="NAMA HOTEL").grid(row=3, column=0)
    entry_nama_hotel = Entry(edit_window)
    entry_nama_hotel.grid(row=3, column=1)
    entry_nama_hotel.insert(0, nama_hotel)

    Label(edit_window, text="ALAMAT").grid(row=4, column=0)
    entry_alamat = Entry(edit_window)
    entry_alamat.grid(row=4, column=1)
    entry_alamat.insert(0, alamat)

    Label(edit_window, text="KELURAHAN").grid(row=5, column=0)
    entry_kelurahan = Entry(edit_window)
    entry_kelurahan.grid(row=5, column=1)
    entry_kelurahan.insert(0, kelurahan)

    Label(edit_window, text="KECAMATAN").grid(row=6, column=0)
    entry_kecamatan = Entry(edit_window)
    entry_kecamatan.grid(row=6, column=1)
    entry_kecamatan.insert(0, kecamatan)

    Label(edit_window, text="PEMBUKUAN").grid(row=7, column=0)
    entry_pembukuan = Entry(edit_window)
    entry_pembukuan.grid(row=7, column=1)
    entry_pembukuan.insert(0, pembukuan)

    Label(edit_window, text="USERNAME").grid(row=8, column=0)
    entry_username = Entry(edit_window)
    entry_username.grid(row=8, column=1)
    entry_username.insert(0, username)

    Label(edit_window, text="STATUS").grid(row=9, column=0)
    status_var = StringVar(value=status)
    status_aktif = Radiobutton(edit_window, text="Y", variable=status_var, value="Y")
    status_tidak_aktif = Radiobutton(edit_window, text="T", variable=status_var, value="T")
    status_aktif.grid(row=9, column=1)
    status_tidak_aktif.grid(row=9, column=2)

    Button(edit_window, text="Save", command=save).grid(row=10, columnspan=3)

# Fungsi untuk menghapus data di database
def delete(id):
    cursor = db.cursor()
    sql = "DELETE FROM data_pajak_hotel WHERE id=%s"
    val = (id, )
    cursor.execute(sql, val)
    db.commit()
    messagebox.showinfo("Success", "Data deleted successfully")
    refresh()

# Fungsi untuk merefresh tampilan data
def refresh():
    for widget in root.winfo_children():
        widget.destroy()
    main()

# Fungsi utama untuk menampilkan data
def main():
    Button(root, text="Insert", command=create).grid(row=0, column=16)

    Label(root, text="NO", borderwidth=1, relief=SUNKEN, width=5).grid(row=0)
    Label(root, text="Id", borderwidth=1, relief=SUNKEN, width=5).grid(row=0, column=1)
    Label(root, text="NO REG OBJEK", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=2)
    Label(root, text="NPWDP", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=3)
    Label(root, text="REKENING", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=4)
    Label(root, text="NAMA HOTEL", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=5)
    Label(root, text="ALAMAT", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=6)
    Label(root, text="KELURAHAN", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=7)
    Label(root, text="KECAMATAN", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=8)
    Label(root, text="PEMBUKUAN", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=9)
    Label(root, text="USERNAME", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=10)
    Label(root, text="CREATED AT", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=11)
    Label(root, text="UPDATED AT", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=12)
    Label(root, text="STATUS", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=13)
    Label(root, text="AKSI", borderwidth=1, relief=SUNKEN, width=12).grid(row=0, column=14, columnspan=2)

    results = read_data()
    no = 0

    for data in results:
        no += 1
        Label(root, text=no, borderwidth=1, relief=SUNKEN, width=5).grid(row=no)
        Label(root, text=data[0], borderwidth=1, relief=SUNKEN, width=5).grid(row=no, column=1)
        Label(root, text=data[1], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=2)
        Label(root, text=data[2], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=3)
        Label(root, text=data[3], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=4)
        Label(root, text=data[4], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=5)
        Label(root, text=data[5], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=6)
        Label(root, text=data[6], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=7)
        Label(root, text=data[7], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=8)
        Label(root, text=data[8], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=9)
        Label(root, text=data[9], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=10)
        Label(root, text=data[10], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=11)
        Label(root, text=data[11], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=12)
        Label(root, text=data[12], borderwidth=1, relief=SUNKEN, width=12).grid(row=no, column=13)
        Button(root, text="Edit",  command=lambda id=data[0], no_reg_objek=data[1], npwdp=data[2], rekening=data[3], nama_hotel=data[4], alamat=data[5], kelurahan=data[6], kecamatan=data[7], pembukuan=data[8], username=data[9], status=data[12] :update(id, no_reg_objek, npwdp, rekening, nama_hotel, alamat, kelurahan, kecamatan, pembukuan, username, status)).grid(row=no, column=14)
        Button(root, text="Delete", command=lambda id=data[0] :delete(id)).grid(row=no, column=15)

main()
root.mainloop()
