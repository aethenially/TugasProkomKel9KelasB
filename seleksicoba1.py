# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:53:25 2024

@author: Lenovo
"""

# Fungsi untuk menghitung IMT
def hitung_imt(berat_badan, tinggi_badan):
    return berat_badan / (tinggi_badan / 100) ** 2

# Fungsi untuk menghitung nilai tes tertulis
def hitung_nilai_tes_tulis(jml_benar_tiu, jml_benar_twk, jml_benar_tkp, bobot_tiu, bobot_twk, bobot_tkp):
    return (jml_benar_tiu * bobot_tiu) + (jml_benar_twk * bobot_twk) + (jml_benar_tkp * bobot_tkp)

# Fungsi untuk menampilkan tabel hasil seleksi
def tampilkan_tabel(pendaftar):
    # Mengurutkan peserta dengan prioritas lolos seleksi, lalu berdasarkan nilai tes dan IMT
    pendaftar.sort(key=lambda x: (x['status'] == 'Lolos Seleksi', x['nilai_tes'], -x['imt']), reverse=True)

    print(f"\n{'Peringkat':<10}{'Nama':<25}{'Nilai Tes':<12}{'IMT':<6}{'Status':<20}")
    print("=" * 80)
    for idx, peserta in enumerate(pendaftar, start=1):
        print(f"{idx:<10}{peserta['nama']:<25}{peserta['nilai_tes']:<12}{peserta['imt']:<6.2f}{peserta['status']:<20}")

# Fungsi untuk menampilkan daftar peserta berdasarkan status
def tampilkan_berdasarkan_status(pendaftar, status):
    filtered = [peserta for peserta in pendaftar if peserta['status'] == status]
    
    print(f"\nDaftar Peserta yang {status}:")
    print(f"{'Nama':<25}{'Nilai Tes':<12}{'IMT':<6}{'Status':<20}")
    print("=" * 70)
    for peserta in filtered:
        print(f"{peserta['nama']:<25}{peserta['nilai_tes']:<12}{peserta['imt']:<6.2f}{peserta['status']:<20}")

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
    
    pendaftar = []  # List untuk menyimpan data peserta
    n = int(input("Masukkan jumlah pendaftar: "))
    
    # Input bobot nilai tes tertulis dengan validasi untuk tidak lebih dari 10
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

    # Input batas tinggi badan
    batas_tinggi_laki = float(input("Masukkan batas tinggi badan minimal laki-laki (cm): "))
    batas_tinggi_perempuan = float(input("Masukkan batas tinggi badan minimal perempuan (cm): "))
    
    # Input nilai tes minimum
    nilai_minimum = int(input("Masukkan nilai tes tertulis minimum untuk lolos: "))
    
    # Input jumlah soal untuk TIU, TWK, dan TKP
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
        
        # Validasi jumlah soal benar tidak melebihi jumlah soal yang ada
        while True:
            jml_benar_tiu = int(input(f"Jumlah soal benar TIU (maks {jumlah_soal_tiu}): "))
            jml_benar_twk = int(input(f"Jumlah soal benar TWK (maks {jumlah_soal_twk}): "))
            jml_benar_tkp = int(input(f"Jumlah soal benar TKP (maks {jumlah_soal_tkp}): "))

            if (jml_benar_tiu <= jumlah_soal_tiu and 
                jml_benar_twk <= jumlah_soal_twk and 
                jml_benar_tkp <= jumlah_soal_tkp):
                break
            else:
                print("Jumlah soal benar tidak boleh lebih dari jumlah soal yang ada (maks 20). Silakan masukkan ulang.")
        
        pendaftar.append({
            'nama': nama,
            'jenis_kelamin': jenis_kelamin,
            'tinggi_badan': tinggi_badan,
            'berat_badan': berat_badan,
            'jml_benar_tiu': jml_benar_tiu,
            'jml_benar_twk': jml_benar_twk,
            'jml_benar_tkp': jml_benar_tkp,
            'status': '',
            'imt': 0,
            'nilai_tes': 0
        })

    # Setelah data peserta dimasukkan, lakukan seleksi
    seleksi(pendaftar, batas_tinggi_laki, batas_tinggi_perempuan, nilai_minimum, bobot_tiu, bobot_twk, bobot_tkp)
    
    # Menu
    while True:
        print("\nMenu Hasil Seleksi:")
        print("1. Tampilkan daftar peserta yang lolos seleksi")
        print("2. Tampilkan daftar peserta yang tidak lolos seleksi")
        print("3. Tampilkan daftar peserta peringkat (lolos dan tidak lolos)")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            # Tampilkan peserta yang lolos seleksi
            tampilkan_berdasarkan_status(pendaftar, 'Lolos Seleksi')
        
        elif pilihan == '2':
            # Tampilkan peserta yang tidak lolos 
            tampilkan_berdasarkan_status(pendaftar, 'Tidak Lolos')
        
        elif pilihan == '3':
            # Tampilkan peserta berdasarkan peringkat (lolos dan tidak lolos)
            tampilkan_tabel(pendaftar)
        
        elif pilihan == '4':
            # Keluar dari program
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4.")

if __name__ == "__main__":
    main()
    