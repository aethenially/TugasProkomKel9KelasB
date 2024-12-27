from akun import signup, login, baca_akun_csv, simpan_akun_csv
from simpandata import baca_pendaftar_csv, simpan_pendaftar_csv
from perhitungan import seleksi
from tampilkan_data import tampilkan_tabel, tampilkan_berdasarkan_status
import os
import time

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
        print("Menu Seleksi Kedinasan:")
        print("1. Input data peserta")
        print("2. Lihat daftar peserta yang lolos")
        print("3. Lihat daftar peserta yang tidak lolos")
        print("4. Lihat peringkat peserta")
        print("5. Keluar")
        

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            while True:
                try:
                    os.system("cls")
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
                    
            while True:
               try:
                   jumlah_soal_tiu = int(input("Input jumlah soal TIU: "))
                   jumlah_soal_twk = int(input("Input jumlah soal TWK: "))
                   jumlah_soal_tkp = int(input("Input jumlah soal TKP: "))
                   break  # Keluar dari loop jika semua valid
               except ValueError:
                   print("Input tidak valid. Harap masukkan angka yang valid untuk jumlah soal.")

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
            os.system("cls")
            print("Data berhasil diinput!")
            time.sleep(2)
            os.system("cls")
            print("Kembali ke menu utama...")
            time.sleep(2)
            os.system("cls")
            
        elif pilihan == '2':
            pendaftar = baca_pendaftar_csv()
            if not pendaftar:
                print("Tidak ada data peserta. Silakan input data peserta terlebih dahulu!")
            else:
                # Menjalankan seleksi sebelum menampilkan peserta lolos
                tampilkan_berdasarkan_status(pendaftar, "Lolos Seleksi")
                print("\nTekan enter untuk kembali!")
                input()
                os.system("cls")
                print("Kembali ke menu utama...")
                time.sleep(2)
                os.system("cls")
                

        elif pilihan == '3':
            pendaftar = baca_pendaftar_csv()
            if not pendaftar:
                print("Silakan input data peserta terlebih dahulu!")
            else:
                # Menjalankan seleksi sebelum menampilkan peserta tidak lolos
                tampilkan_berdasarkan_status(pendaftar, "Tidak Lolos")
                print("\nTekan enter untuk kembali!")
                input()
                os.system("cls")
                print("Kembali ke menu utama...")
                time.sleep(2)
                os.system("cls")

        elif pilihan == '4':
            pendaftar = baca_pendaftar_csv()
            if not pendaftar:
                print("Silakan input data peserta terlebih dahulu!")
            else:
                tampilkan_tabel(pendaftar)
                print("\nTekan enter untuk kembali!")
                input()
                os.system("cls")
                print("Kembali ke menu utama...")
                time.sleep(2)
                os.system("cls")

        elif pilihan == '5':
            os.system("cls")    
            print("Terima kasih telah menggunakan program ini.")
            time.sleep(2)
            os.system("cls")    
            print("Menutup program....")
            time.sleep(2)
            os.system("cls")    
            break

        else:
            os.system("cls")
            print("Pilihan tidak valid. Silahkan pilih menu yang ada.")
            time.sleep(2)
            os.system("cls")

if __name__ == "__main__":
    main()
