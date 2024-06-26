import mysql.connector

db = mysql.connector.connect(
   host = "localhost",
   user = "root",
   password = "",
   database = "klinik"
)

if db.is_connected():
   print("Connected to MySQL database")

cursor = db.cursor()
sql = "INSERT INTO obat (id_obat, nama_obat, klasifikasi_obat, jenis_obat, harga, dosis, resep) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
val = ("01", "paracetamol", "obat demam", "racun baik", "10000", "5mg", "dari dokter")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))
