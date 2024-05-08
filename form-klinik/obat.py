from tkinter import *
root = Tk()

root.title("Form Obat")

root.geometry("400x400")

# frame
# frame = Frame(root, bg="black", padx=10, pady=10)
# frame.pack()

Label(root, text="Nama Obat").grid(row=0)
Label(root, text="Dosis").grid(row=1)
Label(root, text="Resep").grid(row=2)
Label(root, text="Klasifikasi obat").grid(row=3)
Label(root, text="Jenis Obat").grid(row=4)

Entry(root, width=50).grid(row=0, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=1, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=2, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=3, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=4, column=1, padx=10, pady=5, ipady=5) 

Button(root, text="Simpan").grid(row=10, columnspan=2, pady=10)


root.mainloop()