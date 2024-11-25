# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:18:45 2024

@author: Lenovo
"""
import os 
import csv
import hashlib
from tabulate import tabulate 

# Database sederhana untuk menyimpan akun (Email dan Password)
akun_db = {}

# Fungsi untuk mengenkripsi password
def enkripsi_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def simpan_akun_csv():
    with open('akun.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Email', 'Password'])
        writer.writeheader()
        for email, password in akun_db.items():
            writer.writerow({'Email': email, 'Password': password})

def baca_akun_csv():
    try:
        with open('akun.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                akun_db[row['Email']] = row['Password']  # Muat data ke akun_db
    except FileNotFoundError:
        print("File akun.csv tidak ditemukan. Membuat file baru.")

# Fungsi untuk menampilkan tabel peserta dari CSV
import csv

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
    email = input("Masukkan email: ")
    
    # Cek jika email sudah terdaftar
    if email in akun_db:
        print("Email sudah terdaftar, silakan login.")
        return False
    
    password = input("Masukkan password: ")
    konfirmasi_password = input("Konfirmasi password: ")
    
    if password != konfirmasi_password:
        print("Password tidak cocok. Silakan coba lagi.")
        return False
    
    akun_db[email] = enkripsi_password(password)
    print("Akun berhasil dibuat! Silakan login.")
    return True

# Fungsi untuk login
def login():
    print("=========== Login ===========")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")
    
    if email in akun_db and akun_db[email] == enkripsi_password(password):
        print("Login berhasil!")
        return True
    else:
        print("Email atau password salah. Coba lagi.")
        return False

# Fungsi untuk menghitung IMT
def hitung_imt(berat_badan, tinggi_badan):
    return berat_badan / (tinggi_badan / 100) ** 2

# Fungsi untuk menghitung nilai tes tertulis
def hitung_nilai_tes_tulis(jml_benar_tiu, jml_benar_twk, jml_benar_tkp, bobot_tiu, bobot_twk, bobot_tkp):
    return (jml_benar_tiu * bobot_tiu) + (jml_benar_twk * bobot_twk) + (jml_benar_tkp * bobot_tkp)

# Fungsi untuk menampilkan tabel hasil seleksi
# Fungsi untuk menampilkan tabel hasil seleksi
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
    print(f"  DAFTAR PESERTA YANG {status.upper()}")
    print("===========================================\n")

    filtered = [peserta for peserta in pendaftar if peserta['status'] == status]
    
    print(f"\nDaftar Peserta yang {status}:")
    print(f"{'Nama':<25}{'Jenis Kelamin':<15}{'Nilai Tes':<12}{'IMT':<6}{'Status':<20}")
    print("=" * 90)
    for peserta in filtered:
        print(f"{peserta['nama']:<25}{peserta['jenis_kelamin']:<15}{peserta['nilai_tes']:<12}{peserta['imt']:<6.2f}{peserta['status']:<20}")

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
                f"{peserta['tinggi_badan']:.1f}",  # Tinggi badan dengan 1 desimal
                f"{peserta['berat_badan']:.1f}",   # Berat badan dengan 1 desimal
                f"{peserta['imt']:.2f}",          # IMT dengan 2 desimal
                int(peserta['nilai_tes']),        # Nilai tes tanpa desimal
                peserta['status']
            ])
    print("Data peserta berhasil disimpan dengan format rapi ke peserta.csv")


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



# Fungsi untuk melakukan seleksi pendaftar
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

# Program utama
def main():
    print("===================================")
    print("Selamat Datang di Seleksi Kedinasan!")
    print("===================================")

    # Muat data dari CSV
    pendaftar = baca_pendaftar_csv()
  #  print(f"{len(pendaftar)} peserta ditemukan dalam database.")
    
    # Pilih antara login atau signup
    while True:
        pilihan = input("Apakah Anda sudah memiliki akun? (login/signup): ").lower()
        if pilihan == 'login':
            if login():
                break
        elif pilihan == 'signup':
            if signup():
                break
        else:
            print("Pilihan tidak valid. Pilih antara 'login' atau 'signup'.")
    
    # Setelah login/signup berhasil, lanjutkan ke menu seleksi
    pendaftar = []  # List untuk menyimpan data peserta
    
    while True:
        print("\nMenu Seleksi Kedinasan:")
        print("1. Input data peserta")
        print("2. Lihat daftar peserta yang lolos")
        print("3. Lihat daftar peserta yang tidak lolos")
        print("4. Lihat peringkat peserta")
        print("5. Keluar dan simpan pembaruan data")
        print("6. Menampilkan tabel peserta yang telah disimpan ke CSV")  # Lebih deskriptif

        pilihan = input("Pilih menu (1-6): ")
        if pilihan == '1':
            # Input data peserta
            n = int(input("Masukkan jumlah pendaftar: "))
            
            while True:
                bobot_tiu = int(input("Masukkan bobot TIU (maks 10): "))
                if 0 <= bobot_tiu <= 10:
                    break
                else:
                    print("Bobot TIU harus antara 0 dan 10.")
            
            while True:
                bobot_twk = int(input("Masukkan bobot TWK (maks 10): "))
                if 0 <= bobot_twk <= 10:
                    break
                else:
                    print("Bobot TWK harus antara 0 dan 10.")
            
            while True:
                bobot_tkp = int(input("Masukkan bobot TKP (maks 10): "))
                if 0 <= bobot_tkp <= 10:
                    break
                else:
                    print("Bobot TKP harus antara 0 dan 10.")

            batas_tinggi_laki = float(input("Masukkan batas tinggi badan minimal laki-laki (cm): "))
            batas_tinggi_perempuan = float(input("Masukkan batas tinggi badan minimal perempuan (cm): "))
            nilai_minimum = int(input("Masukkan nilai tes tertulis minimum untuk lolos: "))

            jumlah_soal_tiu = 20
            jumlah_soal_twk = 20
            jumlah_soal_tkp = 20

            # Menu untuk input data peserta
            print("\nMenu Input Data Peserta:")
            for i in range(n):
                print(f"\nInput data peserta {i+1}:")
                nama = input("Nama: ")
                
                while True:
                    jenis_kelamin = input("Jenis Kelamin (L/P): ").upper()
                    if jenis_kelamin in ['L', 'P']:
                        break
                    else:
                        print("Jenis kelamin tidak valid. Harap masukkan 'L' untuk Laki-laki atau 'P' untuk Perempuan.")
                
                tinggi_badan = float(input("Tinggi Badan (cm): "))
                berat_badan = float(input("Berat Badan (kg): "))
                
                while True:
                    jml_benar_tiu = int(input(f"Jumlah soal benar TIU (maks {jumlah_soal_tiu}): "))
                    jml_benar_twk = int(input(f"Jumlah soal benar TWK (maks {jumlah_soal_twk}): "))
                    jml_benar_tkp = int(input(f"Jumlah soal benar TKP (maks {jumlah_soal_tkp}): "))

                    if (jml_benar_tiu <= jumlah_soal_tiu and 
                        jml_benar_twk <= jumlah_soal_twk and 
                        jml_benar_tkp <= jumlah_soal_tkp):
                        break
                    else:
                        print("Jumlah soal benar tidak valid. Cek kembali.")
                
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

        elif pilihan == '2':
            if not pendaftar:
                print("Silakan input data peserta terlebih dahulu!")
            else:
                # Menjalankan seleksi sebelum menampilkan peserta lolos
                seleksi(pendaftar, batas_tinggi_laki, batas_tinggi_perempuan, nilai_minimum, bobot_tiu, bobot_twk, bobot_tkp)
                tampilkan_berdasarkan_status(pendaftar, "Lolos Seleksi")

        elif pilihan == '3':
            if not pendaftar:
                print("Silakan input data peserta terlebih dahulu!")
            else:
                # Menjalankan seleksi sebelum menampilkan peserta tidak lolos
                seleksi(pendaftar, batas_tinggi_laki, batas_tinggi_perempuan, nilai_minimum, bobot_tiu, bobot_twk, bobot_tkp)
                tampilkan_berdasarkan_status(pendaftar, "Tidak Lolos")

        elif pilihan == '4':
            if not pendaftar:
                print("Silakan input data peserta terlebih dahulu!")
            else:
                seleksi(pendaftar, batas_tinggi_laki, batas_tinggi_perempuan, nilai_minimum, bobot_tiu, bobot_twk, bobot_tkp)
                tampilkan_tabel(pendaftar)

        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini.")
            simpan_akun_csv()  # Simpan akun ke file CSV
            simpan_pendaftar_csv(pendaftar)  # Simpan data peserta ke file CSV
            print("Data telah disimpan. Terima kasih telah menggunakan program ini.")
            break

        elif pilihan == '6':
            print("\nMenampilkan tabel peserta dari file CSV:")
            tampilkan_tabel_csv()
            
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang ada.")
            
if __name__ == "__main__":
    # Muat data akun
    baca_akun_csv()

    # Muat data peserta
    global pendaftar
    pendaftar = baca_pendaftar_csv()

    # Jalankan program utama
    main()

