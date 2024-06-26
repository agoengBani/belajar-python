from tkinter import *
root = Tk()

root.title("Form Pencalon")

root.geometry("400x400")

Label(root, text="Id Calon").grid(row=0)
Label(root, text="Nama").grid(row=1)
Label(root, text="Tanggal Lahir").grid(row=2)
Label(root, text="Tempat Lahir").grid(row=3)
Label(root, text="Alamat").grid(row=4)

Label(root, text="Jenis Kelamin").grid(row=5)
Label(root, text="Pendidikan").grid(row=6)
Label(root, text="Nama Partai").grid(row=7)
Label(root, text="Email").grid(row=8)
Label(root, text="Telepon").grid(row=9)
Label(root, text="Id Pemilu").grid(row=10)

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

Button(root, text="Simpan").grid(row=11, columnspan=2, pady=10)

root.mainloop()