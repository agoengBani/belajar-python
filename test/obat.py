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
create_label(main_frame, "tgl exp", 0, 1)
create_label(main_frame, "Jenis obat", 0, 2)

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
    
    # Membuat frame untuk tombol aksi
    frame_aksi = Frame(main_frame, bd=0, relief="solid", highlightthickness=1, highlightbackground="black")
    frame_aksi.grid(row=row, column=6, sticky="nsew")
    
    # Tombol Edit dan Delete di dalam frame
    Button(frame_aksi, text="sirup", bd=0).pack(side=LEFT)
    Button(frame_aksi, text="tablet", bd=0).pack(side=LEFT)
    
    entries.append((entry_no, entry_nama))

# Tombol untuk menambah baris
Button(main_frame, text="Tambah Baris", command=add_row, relief="solid", borderwidth=1).grid(row=10, columnspan=7, pady=10)

# Tombol Simpan
Button(main_frame, text="Simpan", relief="solid", borderwidth=1).grid(row=11, columnspan=7, pady=10)

# Menambahkan satu baris awal
add_row()

# Membuat kolom memiliki ukuran yang sama
for col in range(7):
    main_frame.grid_columnconfigure(col, weight=1)

root.mainloop()
