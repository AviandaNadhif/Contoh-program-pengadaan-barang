import datetime
import json
import os
# Pengadaan Barang perusahaan Geprek Millenial
# Memuat data user dan password
user = []
password = []
# List barang yang tersedia
barang_list = []
Duit_Perusahaan = 1000000
exit_program = False
# Untuk menampilkan menu dan memproses pilihan
def tampilkan_menu(barang_list):

    global exit_program
    while not exit_program:
        global Duit_Perusahaan
        print("="*40)
        print("Menu Pengadaan Barang perusahaan Geprek Millenial")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Lihat Barang")
        print("4. Lihat Uang Perusahaan")
        print("5. Beli Barang")
        print("6. Simpan Data")
        print("7. Kembali ke Menu Login")
        print("8. Keluar")
        print("="*40)
        pilihan = input("Pilih menu (1/2/3/4/5/6/7/8): ")
        if pilihan == "1":
            # Tambah Barang
            nama_barang = input("Masukkan nama barang: ")
            # Cek apakah barang sudah ada di daftar
            if any(nama_barang in barang for barang in barang_list):
                print("Barang sudah ada dalam daftar.")
                continue
            jumlah_barang = int(input("Masukkan jumlah barang(unit/kg): "))
            harga_per_unit = int(input("Masukkan harga per unit/kg barang: Rp."))
            harga_barang = jumlah_barang * harga_per_unit
            tanggal_pengadaan = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Buat Pastiin semua input valid
            if nama_barang:
                if jumlah_barang > 0:
                    if harga_per_unit > 0:
                        # Buat string dan tuple untuk barang baru
                        barang = (
                            f"Nama: {nama_barang}\n"
                            f"Jumlah: {jumlah_barang}\n"
                            f"Harga per unit: Rp.{harga_per_unit:,}\n"
                            f"Total Harga: Rp.{harga_barang:,}\n"
                            f"Tanggal: {tanggal_pengadaan}"
                        )
                        # Menambahkan barang ke daftar barang
                        barang_list.append(barang)
                        print("Barang berhasil ditambahkan!")
                    else:
                        print("Harga per unit barang harus lebih dari 0.")
                else:
                    print("Jumlah barang harus lebih dari 0.")
            else:
                print("Nama barang tidak boleh kosong.")
        elif pilihan == "2":
            # Hapus Barang
            if not barang_list:
                print("Tidak ada barang yang dapat dihapus.")
            else:
                print("Daftar Barang:")
                barang_ke = 1
                for barang in barang_list:
                    print(f"{barang_ke}. \n{barang}")
                    barang_ke += 1
                barang_yang_dihapus = int(input("Masukkan nomor barang yang ingin dihapus: "))
                if barang_yang_dihapus > 0 and barang_yang_dihapus <= len(barang_list):
                    barang_list.pop(barang_yang_dihapus - 1)
                    print("Barang berhasil dihapus.")
                else:
                    print("Nomor barang yang dimasukkan tidak valid.")

        elif pilihan == "3":
            # Lihat Barang
            if not barang_list:
                print("Tidak ada barang yang tersedia.")
            else:
                barang_ke = 1
                for barang in barang_list:
                    print(f"{barang_ke}. \n{barang}")
                    barang_ke += 1

        elif pilihan == "4":
            # Lihat Uang Perusahaan
            print(f"Uang Perusahaan: Rp.{Duit_Perusahaan:,}")
            pilihan_tambah_uang = input("Apakah Anda ingin menambahkan uang perusahaan? (Y/N): ")
            if pilihan_tambah_uang.upper() == "Y":
                tambahan_uang = int(input("Masukkan jumlah uang yang ingin ditambahkan: Rp."))
                if tambahan_uang > 0:
                    Duit_Perusahaan += tambahan_uang
                    print(f"Uang perusahaan berhasil ditambahkan. Uang perusahaan sekarang: Rp.{Duit_Perusahaan:,}")
                else:
                    print("Jumlah uang yang dimasukkan harus lebih dari Rp.0.")
            elif pilihan_tambah_uang.upper() == "N":
                print("Uang perusahaan tidak ditambahkan.")
            else:
                print("Pilihan tidak valid.")
        elif pilihan == "5":
            # Beli Barang
            if not barang_list:
                print("Tidak ada barang yang tersedia.")
            else:
                barang_ke = 1
                for barang in barang_list:
                    print(f"{barang_ke}. \n{barang}")
                    barang_ke += 1
                barang_yang_dibeli = int(input("Masukkan nomor barang yang ingin dibeli: "))
                if barang_yang_dibeli > 0 and barang_yang_dibeli <= len(barang_list):
                    barang_yang_dibeli -= 1
                    barang = barang_list[barang_yang_dibeli]
                    # Memisahkan string berdasarkan baris baru (\n)
                    baris_barang = barang.split("\n")
                    # Mengambil baris yang berisi total harga (baris ke-4)
                    baris_harga = baris_barang[3]
                    # Memisahkan string berdasarkan ": " dan mengambil bagian kedua
                    harga_str = baris_harga.split(": ")[1]
                    # Menghapus "Rp." dan tanda koma, lalu mengubahnya menjadi integer
                    harga_barang = int(harga_str.replace("Rp.", "").replace(",", ""))
                    if Duit_Perusahaan >= harga_barang:
                        Duit_Perusahaan -= harga_barang
                        print("Barang berhasil dibeli!")
                    else:
                        print("Uang perusahaan tidak cukup untuk membeli barang tersebut.")
                else:
                    print("Nomor barang yang dimasukkan tidak valid.")
        elif pilihan == "6":
            # Simpan Data
            simpan_data(barang_list, Duit_Perusahaan)
        elif pilihan == "7":
            # Kembali ke Menu Login
            login()
        elif pilihan == "8":
            # Keluar
            print("="*40)
            print("Terima kasih telah menggunakan program pengadaan barang, Semoga Harimu menyenangkan.")
            exit_program = True
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
def daftar_userdanpassword():
            print("=== Pendaftaraan user dan password ===")
            print("Masukkan User dan Password")
            user.append(input("Masukkan username: ").lower())
            password.append(input("Masukkan password: ").lower())
            simpan_userdanpassword_data()
            print("User dan Password berhasil ditambahkan.")
# Memuat data user dan password
def login():
    global exit_program
    while not exit_program:
        print("\n=== Login Pengguna ===")
        print("1. Login")
        print("2. Daftar")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        if pilihan == "1":
            username = input("Masukkan username: ").lower()
            if username in user:
                passwords = input("Masukkan password: ").lower()
                if passwords in password:
                    print("Selamat datang")
                    tampilkan_menu(barang_list)
                    
                else:
                    print("Password salah")
            else:
                print("Username dan password tidak ditemukan. Kembali ke menu Login")
                
        elif pilihan == "2":
            daftar_userdanpassword()
        elif pilihan == "3":
            print("="*40)
            print("Terima kasih telah menggunakan program pengadaan barang, Semoga Harimu menyenangkan.")
            exit_program = True
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            break
# Untuk menyimpan data ke file JSON
def simpan_data(barang_list, Duit_Perusahaan):
    # Mendapatkan path direktori Downloads
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "data_barang dan uang.json")
    with open(downloads_path, 'w') as file:
        json.dump({"List Barang": barang_list, "Duit Perusahaan": Duit_Perusahaan}, file, indent=4)
    print(f"Data barang berhasil disimpan ke {downloads_path}")
# Untuk memuat data dari file JSON
def muat_data():
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "data_barang dan uang.json")
    try:
        with open(downloads_path, 'r') as file:
            data = json.load(file)
            return data["List Barang"], data["Duit Perusahaan"]
    except FileNotFoundError:
        return [], Duit_Perusahaan # Mengembalikan list kosong jika file tidak ditemukan
# Untuk menyimpan data user dan password ke file JSON
def simpan_userdanpassword_data():
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "user.json")
    with open(downloads_path, 'w') as file:
        json.dump({"List User": user, "List Password": password}, file, indent=4)
    print(f"Data user berhasil disimpan ke {downloads_path}")
# Untuk memuat data user dan password dari file JSON
def muat_userdanpassword_data():
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "user.json")
    try:
        with open(downloads_path, 'r') as file:
            data = json.load(file)
            return data["List User"], data["List Password"]
    except FileNotFoundError:
        return [], [] # Mengembalikan list kosong jika file tidak ditemukan

# Memuat data  
barang_list, Duit_Perusahaan = muat_data()
user, password = muat_userdanpassword_data()

# Menjalankan program
login()
