import os 
import csv
import hashlib
from tabulate import tabulate 

# Database sederhana untuk menyimpan akun (username dan Password)
akun_db = {}

# Fungsi untuk mengenkripsi password
def enkripsi_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hitung_imt(berat_badan, tinggi_badan):
    return berat_badan / (tinggi_badan / 100) ** 2

def hitung_nilai_tes_tulis(jml_benar_tiu, jml_benar_twk, jml_benar_tkp, bobot_tiu, bobot_twk, bobot_tkp):
    return (jml_benar_tiu * bobot_tiu) + (jml_benar_twk * bobot_twk) + (jml_benar_tkp * bobot_tkp)

def simpan_akun_csv():
    with open('akun.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'Password'])
        writer.writeheader()
        for username, password in akun_db.items():
            writer.writerow({'username': username, 'Password': password})

def baca_akun_csv():
    try:
        with open('akun.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                akun_db[row['username']] = row['Password']  # Muat data ke akun_db
    except FileNotFoundError:
        print("File akun.csv tidak ditemukan. Membuat file baru.")
    except Exception as e:
        print(f"Kesalahan saat membaca akun: {e}")

def simpan_pendaftar_csv(pendaftar):
    """Fungsi untuk menyimpan data peserta ke file CSV dengan format yang lebih rapi."""
    # Periksa apakah file sudah ada
    file_exists = os.path.isfile('peserta.csv')

    with open('peserta.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        # Jika file belum ada, tulis header
        if not file_exists:
            header = ['Nama', 'Jenis Kelamin', 'Tinggi Badan (cm)', 'Berat Badan (kg)', 'IMT', 'Nilai Tes', 'Status']
            writer.writerow(header)
        
        # Data peserta
        for peserta in pendaftar:
            writer.writerow([
                peserta['nama'],
                peserta['jenis_kelamin'],
                f"{peserta['tinggi_badan']:.1f}",  
                f"{peserta['berat_badan']:.1f}",  
                f"{peserta['imt']:.2f}",          
                int(peserta['nilai_tes']),       
                peserta['status']
            ])
    print("Data peserta berhasil disimpan")

def baca_pendaftar_csv():
    pendaftar = []
    try:
        with open('peserta.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    pendaftar.append({
                        'nama': row['Nama'],
                        'jenis_kelamin': row['Jenis Kelamin'],
                        'tinggi_badan': float(row['Tinggi Badan (cm)']) if row['Tinggi Badan (cm)'] else 0,
                        'berat_badan': float(row['Berat Badan (kg)']) if row['Berat Badan (kg)'] else 0,
                        'imt': float(row['IMT']) if row['IMT'] else 0,
                        'nilai_tes': float(row['Nilai Tes']) if row['Nilai Tes'] else 0,
                        'status': row['Status']
                    })
                except ValueError as e:
                    print(f"Skipping row due to error: {e}")
                    continue  # Skip the row if there is an error
    except FileNotFoundError:
        print("File peserta.csv tidak ditemukan. Membuat file baru.")
    return pendaftar

def tampilkan_tabel_csv():
    try:
        with open('peserta.csv', mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
            
            # Pisahkan header dan data
            if data:
                header, rows = data[0], data[1:]
                print(tabulate(rows, headers=header, tablefmt="grid"))
            else:
                print("Tidak ada data untuk ditampilkan.")
    except FileNotFoundError:
        print("File peserta.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def signup():
    print("=========== Signup ===========")
    username = input("Masukkan username: ")
    
    # Cek jika username sudah terdaftar
    if username in akun_db:
       print("Username sudah terdaftar, silahkan melanjutkan program")
       print("Tekan Enter untuk melanjutkan ke menu utama.")
       input() 
       return False
    
    password = input("Masukkan password: ")
    konfirmasi_password = input("Konfirmasi password: ")
    
    if password != konfirmasi_password:
        print("Password tidak cocok. Silakan coba lagi.")
        return False
    
    akun_db[username] = enkripsi_password(password)
    print("Akun berhasil dibuat! Silahkan melanjutkan program.")
    print("Tekan Enter untuk melanjutkan ke menu utama.")
    input()  # Tunggu pengguna menekan Enter
    return True

def login():
    print("=========== Login ===========")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in akun_db and akun_db[username] == enkripsi_password(password):
        print("Login berhasil!")
        print("Tekan Enter untuk melanjutkan ke menu utama.")
        input()
        return True
    else:
        print("username atau password salah. Coba lagi.")
        return False

def seleksi(pendaftar, batas_tinggi_laki, batas_tinggi_perempuan, nilai_minimum, bobot_tiu, bobot_twk, bobot_tkp):
    for peserta in pendaftar:
        imt = hitung_imt(peserta['berat_badan'], peserta['tinggi_badan'])
        nilai_tes = hitung_nilai_tes_tulis(peserta['jml_benar_tiu'], peserta['jml_benar_twk'], peserta['jml_benar_tkp'], bobot_tiu, bobot_twk, bobot_tkp)
        
        peserta['imt'] = imt
        peserta['nilai_tes'] = nilai_tes

        if peserta['jenis_kelamin'] == 'L':
            if peserta['tinggi_badan'] >= batas_tinggi_laki and 18.5 <= imt <= 24.9 and nilai_tes >= nilai_minimum:
                peserta['status'] = 'Lolos Seleksi'
            else:
                peserta['status'] = 'Tidak Lolos'
        elif peserta['jenis_kelamin'] == 'P':
            if peserta['tinggi_badan'] >= batas_tinggi_perempuan and 18.5 <= imt <= 24.9 and nilai_tes >= nilai_minimum:
                peserta['status'] = 'Lolos Seleksi'
            else:
                peserta['status'] = 'Tidak Lolos'

def tampilkan_tabel(pendaftar):
   
    print("\n===========================================")
    print("        TABEL PERINGKAT PESERTA")
    print("===========================================\n") 
    
    pendaftar.sort(key=lambda x: (x['status'] == 'Lolos Seleksi', x['nilai_tes'], -x['imt']), reverse=True)

    print(f"\n{'Peringkat':<10}{'Nama':<25}{'Jenis Kelamin':<15}{'Nilai Tes':<12}{'IMT':<6}{'Status':<20}")
    print("=" * 100)
    for idx, peserta in enumerate(pendaftar, start=1):
        print(f"{idx:<10}{peserta['nama']:<25}{peserta['jenis_kelamin']:<15}{peserta['nilai_tes']:<12}{peserta['imt']:<6.2f}{peserta['status']:<20}")

# Fungsi untuk menampilkan daftar peserta berdasarkan status
def tampilkan_berdasarkan_status(pendaftar, status):
    
    print("\n===========================================")
    print("  DAFTAR PESERTA YANG ",{status.upper()})
    print("===========================================\n")

    filtered = [peserta for peserta in pendaftar if peserta['status'] == status]
    
    print(f"\nDaftar Peserta yang {status}:")
    print(f"{'Nama':<25}{'Jenis Kelamin':<15}{'Nilai Tes':<12}{'IMT':<6}{'Status':<20}")
    print("=" * 90)
    for peserta in filtered:
        print(f"{peserta['nama']:<25}{peserta['jenis_kelamin']:<15}{peserta['nilai_tes']:<12}{peserta['imt']:<6.2f}{peserta['status']:<20}")

def main():
    print("===================================")
    print("Selamat Datang di Seleksi Kedinasan!")
    print("===================================")
    
    baca_akun_csv()
    global pendaftar

    pendaftar = baca_pendaftar_csv()
  #  print(f"{len(pendaftar)} peserta ditemukan dalam database.")
    
    # Pilih antara login atau signup
    while True:
        pilihan = input("Apakah Anda sudah memiliki akun? (ya/tidak): ").lower()
        if pilihan == 'ya':
            if login():
                break
        elif pilihan == 'tidak':
            if signup():
                simpan_akun_csv()  # Simpan akun ke file CSV
                break
        else:
            print("Pilihan tidak valid. Pilih antara 'ya' atau 'tidak'.")
    
    # Setelah login/signup berhasil, lanjutkan ke menu seleksi
    pendaftar = []  # List untuk menyimpan data peserta
    while True:
        print("\nMenu Seleksi Kedinasan:")
        print("1. Input data peserta")
        print("2. Lihat daftar peserta yang lolos")
        print("3. Lihat daftar peserta yang tidak lolos")
        print("4. Lihat peringkat peserta")
        print("5. Keluar")
        

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            while True:
                try:
                    n = int(input("Masukkan jumlah pendaftar: "))
                    if n > 0:
                        break
                    else:
                        print("Jumlah pendaftar harus lebih dari 0. Coba lagi.")
                except ValueError:
                    print("Input tidak valid. Masukkan angka yang benar.")
            while True:
                try:
                    bobot_tiu = int(input("Masukkan bobot TIU (maks 10): "))
                    if 0 <= bobot_tiu <= 10:
                        break
                    else:
                        print("Bobot TIU harus antara 0 dan 10.")
                except ValueError:
                    print("Input tidak valid. Masukkan angka yang benar.")
            
            while True:
                try:
                    bobot_twk = int(input("Masukkan bobot TWK (maks 10): "))
                    if 0 <= bobot_twk <= 10:
                        break
                    else:
                        print("Bobot TWK harus antara 0 dan 10.")
                except ValueError:
                    print("Input tidak valid. Masukkan angka yang benar.")
            
            while True:
                try:
                    bobot_tkp = int(input("Masukkan bobot TKP (maks 10): "))
                    if 0 <= bobot_tkp <= 10:
                        break
                    else:
                        print("Bobot TKP harus antara 0 dan 10.")
                except ValueError:
                    print("Input tidak valid. Masukkan angka yang benar.")

            while True:
                try:
                    batas_tinggi_laki = float(input("Masukkan batas tinggi badan minimal laki-laki (cm): "))
                    if batas_tinggi_laki > 0:
                        break
                    else:
                        print("Tinggi badan minimal harus lebih dari 0.")
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka yang valid.")

            while True:
                try:
                    batas_tinggi_perempuan = float(input("Masukkan batas tinggi badan minimal perempuan (cm): "))
                    if batas_tinggi_perempuan > 0:
                        break
                    else:
                        print("Tinggi badan minimal harus lebuh dari 0")
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka yang valid.")
            
            while True:
                try:
                    nilai_minimum = int(input("Masukkan nilai tes tertulis minimum untuk lolos: "))
                    if nilai_minimum > 0:
                        break
                    else:
                        print("Nilai minimum harus lebih dari 0.")
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka yang valid.")
                    
            jumlah_soal_tiu = 20
            jumlah_soal_twk = 20
            jumlah_soal_tkp = 20

            # Menu untuk input data peserta
            print("\nMenu Input Data Peserta:")
            for i in range(n):
                print(f"\nInput data peserta {i+1}:")
                while True:
                    nama = input("Masukkan nama: ").strip()
                    if nama:
                        break
                    else:
                        print("harap masukkan nama yang valid.")
                
                while True:
                    jenis_kelamin = input("Jenis Kelamin (L/P): ").upper()
                    if jenis_kelamin in ['L', 'P']:
                        break
                    else:
                        print("Jenis kelamin tidak valid. Harap masukkan 'L' untuk Laki-laki atau 'P' untuk Perempuan.")
                
                while True:
                    try:
                        tinggi_badan = input("Tinggi Badan (cm): ")
                        if tinggi_badan == "":
                            raise ValueError("Input tidak boleh kosong.")
                        tinggi_badan = float(tinggi_badan)
                        break
                    except ValueError:
                        print("Input tidak valid. Harap masukkan angka yang valid untuk tinggi badan.")
                
                while True:
                    try:
                        berat_badan = input("Berat Badan (kg): ")
                        if berat_badan == "": 
                            raise ValueError("Input tidak boleh kosong.")
                        berat_badan = float(berat_badan)
                        break
                    except ValueError:
                        print("Input tidak valid. Harap masukkan angka yang valid untuk berat badan.")
                
                while True:
                    try:
                        jml_benar_tiu = int(input(f"Jumlah soal benar TIU (maks {jumlah_soal_tiu}): "))
                        if jml_benar_tiu <= jumlah_soal_tiu:
                            break  # Jika valid, keluar dari loop
                        else:
                            print(f"Jumlah soal benar TIU tidak boleh lebih dari {jumlah_soal_tiu}. Cek kembali.")
                    except ValueError:
                        print("Input tidak valid. Harap masukkan angka yang valid untuk jumlah soal benar TIU.")
                
                while True:
                    try:
                        jml_benar_twk = int(input(f"Jumlah soal benar TWK (maks {jumlah_soal_twk}): "))
                        if jml_benar_twk <= jumlah_soal_twk:
                            break  # Jika valid, keluar dari loop
                        else:
                            print(f"Jumlah soal benar TWK tidak boleh lebih dari {jumlah_soal_twk}. Cek kembali.")
                    except ValueError:
                        print("Input tidak valid. Harap masukkan angka yang valid untuk jumlah soal benar TWK.")
                   
                while True:
                    try:
                        jml_benar_tkp = int(input(f"Jumlah soal benar TKP (maks {jumlah_soal_tkp}): "))
                        if jml_benar_tkp <= jumlah_soal_tkp:
                            break  # Jika valid, keluar dari loop
                        else:
                            print(f"Jumlah soal benar TKP tidak boleh lebih dari {jumlah_soal_tkp}. Cek kembali.")
                    except ValueError:
                        print("Input tidak valid. Harap masukkan angka yang valid untuk jumlah soal benar TKP.") 
    
                
                # Tambahkan data peserta ke daftar pendaftar
                pendaftar.append({
                    'nama': nama,
                    'jenis_kelamin': jenis_kelamin,
                    'tinggi_badan': tinggi_badan,
                    'berat_badan': berat_badan,
                    'jml_benar_tiu': jml_benar_tiu,
                    'jml_benar_twk': jml_benar_twk,
                    'jml_benar_tkp': jml_benar_tkp,
                    'imt': 0,  # IMT dihitung nanti
                    'nilai_tes': 0,  # Nilai tes dihitung nanti
                    'status': 'Belum Di Seleksi'  # Status akan diupdate saat seleksi
                })
            seleksi(pendaftar, batas_tinggi_laki, batas_tinggi_perempuan, nilai_minimum, bobot_tiu, bobot_twk, bobot_tkp)
            simpan_pendaftar_csv(pendaftar)  # Simpan data peserta ke file CSV
            print("\nData berhasil diinput. Silakan tekan Enter untuk kembali ke menu utama.")
            input() 
            
        elif pilihan == '2':
            pendaftar = baca_pendaftar_csv()
            if not pendaftar:
                print("Tidak ada data peserta. Silakan input data peserta terlebih dahulu!")
            else:
                # Menjalankan seleksi sebelum menampilkan peserta lolos
                tampilkan_berdasarkan_status(pendaftar, "Lolos Seleksi")

        elif pilihan == '3':
            pendaftar = baca_pendaftar_csv()
            if not pendaftar:
                print("Silakan input data peserta terlebih dahulu!")
            else:
                # Menjalankan seleksi sebelum menampilkan peserta tidak lolos
                tampilkan_berdasarkan_status(pendaftar, "Tidak Lolos")

        elif pilihan == '4':
            pendaftar = baca_pendaftar_csv()
            if not pendaftar:
                print("Silakan input data peserta terlebih dahulu!")
            else:
                tampilkan_tabel(pendaftar)

        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini.")
            simpan_pendaftar_csv(pendaftar)  # Simpan data peserta ke file CSV
            break

            
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang ada.")
            input("Tekan Enter untuk kembali ke menu utama...")

if _name_ == "_main_":
    main()