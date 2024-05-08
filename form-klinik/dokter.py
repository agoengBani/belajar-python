from tkinter import *
root = Tk()

root.title("Form Dokter")

root.geometry("400x400")

# frame
# frame = Frame(root, bg="black", padx=10, pady=10)
# frame.pack()

Label(root, text="Nama").grid(row=0)
Label(root, text="Alamat").grid(row=1)
Label(root, text="Jenis Kelamin").grid(row=2)
Label(root, text="Umur").grid(row=3)
Label(root, text="Berat Badan").grid(row=4)
Label(root, text="No HP").grid(row=5)
Label(root, text="Antrian").grid(row=6)
Label(root, text="Poly").grid(row=7)
Label(root, text="Jenis perawatan").grid(row=8)
Label(root, text="Jenis Penanganan").grid(row=9)
Label(root, text="Jadwal Control").grid(row=10)

Entry(root, width=50).grid(row=0, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=1, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=2, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=3, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=4, column=1, padx=10, pady=5, ipady=5)  
Entry(root, width=50).grid(row=5, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=6, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=7, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=8, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=9, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=10, column=1, padx=10, pady=5, ipady=5)

Button(root, text="Simpan").grid(row=10, columnspan=2, pady=10)

root.mainloop()