from tkinter import *
root = Tk()

root.title("Form Jual")

root.geometry("400x400")

# frame
# frame = Frame(root, bg="black", padx=10, pady=10)
# frame.pack()

Label(root, text="Obat").grid(row=0)
Label(root, text="Transaksi").grid(row=1)

Entry(root, width=50).grid(row=0, column=1, padx=10, pady=5, ipady=5)
Entry(root, width=50).grid(row=1, column=1, padx=10, pady=5, ipady=5)

Button(root, text="Simpan").grid(row=10, columnspan=2, pady=10)

root.mainloop()