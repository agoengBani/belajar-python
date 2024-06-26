import mysql.connector

db = mysql.connector.connect(
   host = "localhost",
   user = "admin",
   password = ""
)

if db.is_conencted():
   print("Berhasil terhubung ke database")

cursor = db.cursor()
sql = "INSERT INTO obat (id_obat, nama_obat, klasifikasi_obat, jenis_obat, harga, dosis, resep) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = ("01", "Paracetamol", "Obat Demam", "Racun Baik", "10000", "5mg", "Dari dokter")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))