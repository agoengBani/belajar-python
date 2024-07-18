from tkinter import *
root = Tk()

root.title("Form Obat")

frame_no_tgl_exp = Frame(root, relief="solid", borderwidth=1)
frame_no_tgl_exp.grid(row=0, column=0, sticky='nsew', rowspan=2)
Label(frame_no_tgl_exp, text="No", width=30).pack()

frame_nama_obat = Frame(root, relief="solid", borderwidth=1)
frame_nama_obat.grid(row=0, column=1, sticky='nsew', rowspan=2)
Label(frame_nama_obat, text="tgl exp", width=30).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=0, column=2, columnspan=2, sticky='nsew')
Label(frame_jenis_obat, text="Jenis obat", width=30).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=2, sticky='nsew')
Label(frame_jenis_obat, text="sirup", width=15).pack()

frame_jenis_obat = Frame(root, relief="solid", borderwidth=1)
frame_jenis_obat.grid(row=1, column=3, sticky='nsew')
Label(frame_jenis_obat, text="tablet", width=15).pack()

Entry(root, width=36, relief="solid", borderwidth=1).grid(row=2, column=0, sticky='nsew')
Entry(root, width=36, relief="solid", borderwidth=1).grid(row=2, column=1, sticky='nsew')
Entry(root, width=18, relief="solid", borderwidth=1).grid(row=2, column=2, sticky='nsew', columnspan=2, padx=(0, 2))
Entry(root, width=18, relief="solid", borderwidth=1).grid(row=2, column=3, sticky='nsew')

Entry(root, width=36, relief="solid", borderwidth=1).grid(row=3, column=0, sticky='nsew')
Entry(root, width=36, relief="solid", borderwidth=1).grid(row=3, column=1, sticky='nsew')
Entry(root, width=18, relief="solid", borderwidth=1).grid(row=3, column=2, sticky='nsew', columnspan=2, padx=(0, 2))
Entry(root, width=18, relief="solid", borderwidth=1).grid(row=3, column=3, sticky='nsew')

Button(root, text="Simpan").grid(row=10, columnspan=2, pady=10)

frame_aksi = Frame(root)
frame_aksi.grid(row=1, column=2)

root.mainloop()