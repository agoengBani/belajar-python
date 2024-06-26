# a = input("Masukkan nilai jarak: ")
# b = input("Masukkan nilai waktu: ")
# c = int(a) * int(b)
# print("kecepatan = ", c, "km/jam")

# a = 5
# print(a)

# for i in range(10):
#    print(f"Looping ke- {i}")

a = input("input awal : ")
b = input("input akhir: ")

for i in range(int(a), int(b)):
   if i == a:
      i = i + 1
      continue
   print(i)