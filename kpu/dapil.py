from tkinter import *
root = Tk()

root.title("Form Dapil")

root.geometry("400x400")

Label(root, text="Id Dapil").grid(row=0)
Label(root, text="Nama Dapil").grid(row=1)
Label(root, text="Wilayah").grid(row=2)
Label(root, text="Jumlah Kursi").grid(row=3)
Label(root, text="Id Pemilu").grid(row=4)

Entry(root, width=50).grid(row=0, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=1, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=2, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=3, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=4, column=1, padx=10, pady=5, ipady=5)  

Button(root, text="Simpan").grid(row=5, columnspan=2, pady=10)

root.mainloop()