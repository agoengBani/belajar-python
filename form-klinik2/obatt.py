from tkinter import *

root = Tk()
root.title("Form Obat")

# Membuat frame utama
main_frame = Frame(root, padx=10, pady=10)
main_frame.pack(padx=10, pady=10)

# Fungsi untuk membuat label dengan border yang menyatu
def create_label(frame, text, row, column):
    label = Label(frame, text=text, relief="solid", borderwidth=1)
    label.grid(row=row, column=column, sticky="nsew", ipadx=5, ipady=5)
    return label

# Membuat Label untuk setiap kolom di dalam frame
create_label(main_frame, "No", 0, 0)
create_label(main_frame, "Nama Obat", 0, 1)
create_label(main_frame, "Dosis", 0, 2)
create_label(main_frame, "Resep", 0, 3)
create_label(main_frame, "Klasifikasi Obat", 0, 4)
create_label(main_frame, "Jenis Obat", 0, 5)
create_label(main_frame, "Aksi", 0, 6)

entries = []

def add_row():
    row = len(entries) + 1
    
    frame_no = Frame(main_frame, bd=1, relief="solid", highlightthickness=1, highlightbackground="black")
    frame_no.grid(row=row, column=0, sticky="nsew")
    entry_no = Entry(frame_no, width=30, bd=0)
    entry_no.pack()
    
    frame_nama = Frame(main_frame, bd=1, relief="solid", highlightthickness=1, highlightbackground="black")
    frame_nama.grid(row=row, column=1, sticky="nsew")
    entry_nama = Entry(frame_nama, width=30, bd=0)
    entry_nama.pack()
    
    frame_dosis = Frame(main_frame, bd=1, relief="solid", highlightthickness=1, highlightbackground="black")
    frame_dosis.grid(row=row, column=2, sticky="nsew")
    entry_dosis = Entry(frame_dosis, width=30, bd=0)
    entry_dosis.pack()
    
    frame_resep = Frame(main_frame, bd=1, relief="solid", highlightthickness=1, highlightbackground="black")
    frame_resep.grid(row=row, column=3, sticky="nsew")
    entry_resep = Entry(frame_resep, width=30, bd=0)
    entry_resep.pack()
    
    frame_klasifikasi = Frame(main_frame, bd=1, relief="solid", highlightthickness=1, highlightbackground="black")
    frame_klasifikasi.grid(row=row, column=4, sticky="nsew")
    entry_klasifikasi = Entry(frame_klasifikasi, width=30, bd=0)
    entry_klasifikasi.pack()
    
    frame_jenis = Frame(main_frame, bd=1, relief="solid", highlightthickness=1, highlightbackground="black")
    frame_jenis.grid(row=row, column=5, sticky="nsew")
    entry_jenis = Entry(frame_jenis, width=30, bd=0)
    entry_jenis.pack()
    
    # Membuat frame untuk tombol aksi
    frame_aksi = Frame(main_frame, bd=1, relief="solid", highlightthickness=1, highlightbackground="black")
    frame_aksi.grid(row=row, column=6, sticky="nsew")
    
    # Tombol Edit dan Delete di dalam frame
    Button(frame_aksi, text="Edit", bd=0).pack(side=LEFT, padx=2, pady=2)
    Button(frame_aksi, text="Delete", bd=0).pack(side=LEFT, padx=2, pady=2)
    
    entries.append((entry_no, entry_nama, entry_dosis, entry_resep, entry_klasifikasi, entry_jenis))

def save_data():
    data = []
    for entry_set in entries:
        row_data = [entry.get() for entry in entry_set]
        data.append(row_data)
    # Cetak data ke konsol (atau Anda bisa menyimpannya ke file atau database)
    print("Data Tersimpan:")
    for row in data:
        print(row)

# Tombol untuk menambah baris
Button(main_frame, text="Tambah Baris", command=add_row, relief="solid", borderwidth=1).grid(row=10, columnspan=7, pady=10)

# Tombol Simpan
Button(main_frame, text="Simpan", command=save_data, relief="solid", borderwidth=1).grid(row=11, columnspan=7, pady=10)

# Menambahkan satu baris awal
add_row()

# Membuat kolom memiliki ukuran yang sama
for col in range(7):
    main_frame.grid_columnconfigure(col, weight=1)

root.mainloop()
