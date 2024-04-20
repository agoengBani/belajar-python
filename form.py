import tkinter as tk

# membuat form
form  = tk.Tk()
form.title('Aplikasi belajar') # memberi judul pada form

# membuat proses ketika tombol ditekan
def ambil_bilangan():
   a = entry_bilangan_a.get()
   b = entry_bilangan_b.get()
   result = int(a) * int(b)
   # Menampilkan hasil di label dalam form utama
   hasil_label.config(text=f'Hasil: {result}')

# membuat label
lbl_bilangan_a = tk.Label(form, text=("Input bilangan A : "))
lbl_bilangan_a.pack() # menampilkan label di form

# membuat text box
entry_bilangan_a = tk.Entry(form)
entry_bilangan_a.pack() # menampilkan text box di form

# membuat label
lbl_bilangan_b = tk.Label(form, text=("Input bilangan B : "))
lbl_bilangan_b.pack() # menampilkan label di form

# membuat text box
entry_bilangan_b = tk.Entry(form)
entry_bilangan_b.pack() # menampilkan text box di form

# membuat tombol
btn_proses = tk.Button(form, text=("Proses"), command=ambil_bilangan)
btn_proses.pack() # menampilkan tombol

# menampilkan hasil dari inputan ke form
hasil_label = tk.Label(form, text="")
hasil_label.pack()

# mainloop() -> berfungsi untuk menampilkan form
form.mainloop()