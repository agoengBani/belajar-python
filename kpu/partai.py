from tkinter import *
root = Tk()

root.title("Form Partai")

root.geometry("400x400")

Label(root, text="Id Partai").grid(row=0)
Label(root, text="Nama Partai").grid(row=1)
Label(root, text="Ketua Partai").grid(row=2)
Label(root, text="Alamat").grid(row=3)
Label(root, text="Telepon").grid(row=4)

Label(root, text="Email").grid(row=5)
Label(root, text="Website").grid(row=6)

Entry(root, width=50).grid(row=0, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=1, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=2, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=3, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=4, column=1, padx=10, pady=5, ipady=5)  

Entry(root, width=50).grid(row=5, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=6, column=1, padx=10, pady=5, ipady=5)

Button(root, text="Simpan").grid(row=7, columnspan=2, pady=10)

root.mainloop()