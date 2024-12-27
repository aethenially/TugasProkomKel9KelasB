# main.py
import os
import time

from akun import signup, login, baca_akun_csv, simpan_akun_csv
from parameter import simpan_parameter_seleksi_csv, baca_parameter_seleksi_csv, input_parameter_seleksi
from peserta import simpan_pendaftar_csv, seleksi, baca_pendaftar_csv
from util import tampilkan_tabel, tampilkan_berdasarkan_status


def main():
    print("===================================")
    print("Selamat Datang di Seleksi Kedinasan!")
    print("===================================")
    
    baca_akun_csv()
    
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
        print("\nMenu:")
        print("1. Input parameter seleksi")
        print("2. Input peserta seleksi")
        print("3. Lihat peserta lolos")
        print("4. Lihat peringkat peserta")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == '1':
            os.system("cls")
            input_parameter_seleksi()
            print("parameter berhasil disimpan. Tekan enter untuk kembali ke menu utama!")
            input()
            os.system("cls")
            print("kembali ke menu utama....")
            time.sleep(2)
            os.system("cls")
            
        
        elif pilihan == '2':
            os.system("cls")
            tahun = input("Masukkan tahun seleksi: ")

            parameter = baca_parameter_seleksi_csv(tahun)
            if parameter:
                pendaftar = []
                while True:  # Loop untuk memasukkan peserta
                    try:
                        jumlah_pendaftar = int(input("Masukkan jumlah peserta yang mendaftar: "))
                        if jumlah_pendaftar <= 0:
                            raise ValueError("Jumlah peserta harus lebih besar dari 0.")
                        for _ in range(jumlah_pendaftar):
                            # Input nama peserta
                            nama = input("Masukkan nama peserta: ")

                    # Input jenis kelamin dengan validasi
                            while True:
                                jenis_kelamin = input("Masukkan jenis kelamin (L/P): ").upper()
                                if jenis_kelamin in ['L', 'P']:
                                    break
                                print("Jenis kelamin harus 'L' atau 'P'. Coba lagi.")
                    
                    # Input tinggi badan dengan validasi
                            while True:
                                try:
                                    tinggi_badan = float(input("Masukkan tinggi badan (cm): "))
                                    if tinggi_badan <= 0:
                                        raise ValueError("Tinggi badan harus lebih besar dari 0.")
                                    break
                                except ValueError as e:
                                    print(f"Input tidak valid: {e}. Harap masukkan tinggi badan yang valid.")
                    
                    # Input berat badan dengan validasi
                            while True:
                                try:
                                    berat_badan = float(input("Masukkan berat badan (kg): "))
                                    if berat_badan <= 0:
                                        raise ValueError("Berat badan harus lebih besar dari 0.")
                                    break
                                except ValueError as e:
                                    print(f"Input tidak valid: {e}. Harap masukkan berat badan yang valid.")
                    
                    # Input jumlah soal benar untuk setiap mata tes
                            jml_benar = {}
                           
                            # if parameter:
                            for mata_tes in parameter['bobot']:
                                while True:
                                    try:
                                        jml_benar[mata_tes] = int(input(f"Masukkan jumlah soal benar untuk mata tes {mata_tes}: "))
                                        if jml_benar[mata_tes] < 0:
                                            raise ValueError("Jumlah soal benar tidak boleh negatif.")
                                        break
                                    except ValueError as e:
                                        print(f"Input tidak valid: {e}. Harap masukkan jumlah soal benar yang valid.")
                    
                    # Menyimpan data peserta yang sudah valid
                            pendaftar.append({
                                'nama': nama,
                                'jenis_kelamin': jenis_kelamin,
                                'tinggi_badan': tinggi_badan,
                                'berat_badan': berat_badan,
                                'jml_benar': jml_benar
                            })
                        break  # Keluar dari loop setelah semua peserta dimasukkan
                    except ValueError as e:
                        print(f"Input tidak valid: {e}. Silakan coba lagi.")
                        time.sleep(2)
                        os.system("cls")
                
                # simpan_pendaftar_csv(pendaftar, tahun)
                simpan_pendaftar_csv(pendaftar, tahun, parameter)
                print("Data berhasil disimpan")
                print("tekan enter untuk kembali ke menu!")
                input()
                os.system('cls')
                print("kembali ke menu...") 
                time.sleep(2)  
                os.system('cls')         


            else:
                print(f"ERROR: data parameter seleksi untuk tahun {tahun} tidak ditemukan, silakan input parameter terlebih dahulu!")### debugging
                print("tekan enter untuk kembali ke menu!")
                input()
                os.system('cls') 
                print("kembali ke menu...") 
                time.sleep(2)  
                os.system('cls')         

        
        elif pilihan == '3':
            os.system("cls")
            tahun = input("Masukkan tahun seleksi: ")
            parameter = baca_parameter_seleksi_csv(tahun)
            if parameter:
                file_name = f'peserta_{tahun}.csv'
                if not os.path.isfile(file_name) or os.path.getsize(file_name) == 0:
                    print(f"Tidak ada data peserta pada tahun {tahun}, silahkan input peserta terlebih dahulu.")
                    input("Tekan enter untuk kembali ke menu utama...")  # Menghindari input ganda
                    os.system("cls")
                    print("Kembali ke menu utama...")
                    time.sleep(1.5)
                    os.system("cls")
                     # Kembali ke menu utama tanpa melanjutkan
                else:
                    pendaftar = baca_pendaftar_csv(tahun)
                    tampilkan_berdasarkan_status(pendaftar, 'Lolos')
            else:
                print(f"ERROR: data parameter seleksi untuk tahun {tahun} tidak ditemukan, silakan input parameter terlebih dahulu!")### debugging
                print("tekan enter untuk kembali ke menu!")
                input()
                os.system('cls') 
                print("kembali ke menu...") 
                time.sleep(2)  
                os.system('cls')      
                      
        elif pilihan == '4':
            os.system("cls")
            tahun = input("Masukkan tahun seleksi: ")
            file_name = f'peserta_{tahun}.csv'
            if not os.path.isfile(file_name) or os.path.getsize(file_name) == 0:
                print(f"Tidak ada data peserta pada tahun {tahun}, silahkan input peserta terlebih dahulu.")
                input("Tekan enter untuk kembali ke menu utama...")  # Menghindari input ganda
                os.system("cls")
                print("Kembali ke menu utama...")
                time.sleep(1.5)
                os.system("cls")
            else:
                pendaftar = baca_pendaftar_csv(tahun)  # Membaca data peserta
                tampilkan_tabel(pendaftar)  # Menampilkan tabel peringkat peserta
        
        elif pilihan == '5':
            os.system("cls")
            print("Keluar dari program...")
            time.sleep(2)
            os.system("cls")
            break
        
        else:
            os.system("cls")
            print("Pilihan tidak valid, coba lagi. Kembali ke menu...")
            time.sleep(2)
            os.system("cls")

if __name__ == "__main__":
    main()
