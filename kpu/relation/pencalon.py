from tkinter import *
root = Tk()

root.title("Grid Relasi Dapil dan Pencalon")

frame_no_tgl_exp = Frame(root, relief="solid", borderwidth=1)
frame_no_tgl_exp.grid(row=0, column=0, sticky='nsew', rowspan=2)
Label(frame_no_tgl_exp, text="No", width=10).pack()

frame_nama_obat = Frame(root, relief="solid", borderwidth=1)
frame_nama_obat.grid(row=0, column=5, sticky='nsew', rowspan=10)
Label(frame_nama_obat, text="Pencalon", width=10).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=5, sticky='nsew')
Label(frame_jenis_obat, text="Id Calon", width=30).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=6, sticky='nsew')
Label(frame_jenis_obat, text="Nama", width=30).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=7, sticky='nsew')
Label(frame_jenis_obat, text="Tanggal Lahir", width=15).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=8, sticky='nsew')
Label(frame_jenis_obat, text="Tempat Lahir", width=15).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=9, sticky='nsew')
Label(frame_jenis_obat, text="Alamat", width=15).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=10, sticky='nsew')
Label(frame_jenis_obat, text="Pendidikan", width=15).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=11, sticky='nsew')
Label(frame_jenis_obat, text="Nama Partai", width=15).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=12, sticky='nsew')
Label(frame_jenis_obat, text="Email", width=15).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=13, sticky='nsew')
Label(frame_jenis_obat, text="Telepon", width=15).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=14, sticky='nsew')
Label(frame_jenis_obat, text="Id Pemilu", width=15).pack()

Entry(root, width=36, relief="solid", borderwidth=1).grid(row=2, column=5, sticky='nsew')
Entry(root, width=36, relief="solid", borderwidth=1).grid(row=2, column=6, sticky='nsew')
Entry(root, width=18, relief="solid", borderwidth=1).grid(row=2, column=7, sticky='nsew')
Entry(root, width=18, relief="solid", borderwidth=1).grid(row=2, column=8, sticky='nsew')
Entry(root, width=18, relief="solid", borderwidth=1).grid(row=2, column=9, sticky='nsew')

Entry(root, width=36, relief="solid", borderwidth=1).grid(row=3, column=10, sticky='nsew')
Entry(root, width=36, relief="solid", borderwidth=1).grid(row=3, column=11, sticky='nsew')
Entry(root, width=18, relief="solid", borderwidth=1).grid(row=3, column=12, sticky='nsew')
Entry(root, width=18, relief="solid", borderwidth=1).grid(row=3, column=13, sticky='nsew')
Entry(root, width=18, relief="solid", borderwidth=1).grid(row=3, column=14, sticky='nsew')

Button(root, text="Simpan").grid(row=10, columnspan=2, pady=10)

frame_aksi = Frame(root)
frame_aksi.grid(row=1, column=2)

root.mainloop()