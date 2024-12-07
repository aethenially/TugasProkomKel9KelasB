from tabulate import tabulate
import os
import time

def tampilkan_tabel(pendaftar):
    os.system("cls")
    print("Memuat daftar peserta...")
    time.sleep(2)
    os.system("cls")
    print("===========================================")
    print("        TABEL PERINGKAT PESERTA")
    print("===========================================") 
    
    pendaftar.sort(key=lambda x: (x['status'] == 'Lolos Seleksi', x['nilai_tes'], -x['imt']), reverse=True)

    print(f"\n{'Peringkat':<10}{'Nama':<25}{'Jenis Kelamin':<15}{'Nilai Tes':<12}{'IMT':<6}{'Status':<20}")
    print("=" * 100)
    for idx, peserta in enumerate(pendaftar, start=1):
        print(f"{idx:<10}{peserta['nama']:<25}{peserta['jenis_kelamin']:<15}{peserta['nilai_tes']:<12}{peserta['imt']:<6.2f}{peserta['status']:<20}")

# Fungsi untuk menampilkan daftar peserta berdasarkan status
def tampilkan_berdasarkan_status(pendaftar, status):
    os.system("cls")
    print("Memuat daftar peserta...")
    time.sleep(2)
    os.system("cls")
    print("===========================================")
    print("  DAFTAR PESERTA YANG ",status.upper())
    print("===========================================\n")

    filtered = [peserta for peserta in pendaftar if peserta['status'] == status]
    
    print(f"{'Nama':<25}{'Jenis Kelamin':<15}{'Nilai Tes':<12}{'IMT':<6}{'Status':<20}")
    print("=" * 90)
    for peserta in filtered:
        print(f"{peserta['nama']:<25}{peserta['jenis_kelamin']:<15}{peserta['nilai_tes']:<12}{peserta['imt']:<6.2f}{peserta['status']:<20}")

