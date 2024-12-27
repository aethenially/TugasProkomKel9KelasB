# parameter.py
import csv
import os
import time

def simpan_parameter_seleksi_csv(tahun, bobot, batas_tinggi_laki, batas_tinggi_perempuan, nilai_minimum):
    with open('parameter_seleksi.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tahun, str(bobot), batas_tinggi_laki, batas_tinggi_perempuan, nilai_minimum])

def baca_parameter_seleksi_csv(tahun):
    try:
        with open('parameter_seleksi.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == tahun:
                    try:
                        bobot = eval(row[1])  # Mengonversi string bobot menjadi dictionary
                    except Exception:
                        return None
                    
                    batas_tinggi_laki = float(row[2])
                    batas_tinggi_perempuan = float(row[3])
                    nilai_minimum = int(row[4])
                    return {
                        'bobot': bobot,
                        'batas_tinggi_laki': batas_tinggi_laki,
                        'batas_tinggi_perempuan': batas_tinggi_perempuan,
                        'nilai_minimum': nilai_minimum
                    }
    except FileNotFoundError:
        return None

def input_parameter_seleksi(): 
    os.system("cls")
    print("="*50)
    print(" "*12 + "INPUT PARAMETER SELEKSI")
    print("="*50)

    # Input tahun seleksi
    while True:
        try:
            tahun = input("Masukkan tahun seleksi: ")
            if not tahun.isdigit():
                raise ValueError("Tahun harus berupa angka.")
            tahun = int(tahun)  # Mengubah tahun menjadi integer jika valid
            break  # Jika input valid, keluar dari loop
        except ValueError as e:
            print(f"Input tidak valid: {e}. Harap masukkan tahun yang valid.")
            time.sleep(2)
            os.system("cls")

    # Input mata tes
    while True:
        try:
            print("Masukkan mata tes yang diujikan (pisahkan dengan koma jika lebih dari satu):")
            mata_tes = input("Mata tes: ").split(",")
            mata_tes = [tes.strip() for tes in mata_tes]  # Menghapus spasi yang tidak perlu
            if not mata_tes:
                raise ValueError("Mata tes tidak boleh kosong.")
            break  # Jika input valid, keluar dari loop
        except ValueError as e:
            print(f"Input tidak valid: {e}. Harap masukkan mata tes yang valid.")
            time.sleep(2)
            os.system("cls")

    # Input bobot untuk setiap mata tes
    bobot = {}
    for tes in mata_tes:
        while True:
            try:
                # bobot[tes] = int(input(f"Masukkan bobot untuk mata tes {tes}: "))
                bobot[tes] = float(input(f"Masukkan bobot untuk mata tes {tes}: "))
                # if bobot[tes] <= 0:
                if bobot[tes] <= 0.0:
                    raise ValueError("Bobot harus berupa angka positif.")
                break  # Jika input valid, keluar dari loop
            except ValueError as e:
                print(f"Input tidak valid: {e}. Harap masukkan bobot yang valid.")
                time.sleep(2)
                os.system("cls")

    # Input batas tinggi badan
    while True:
        try:
            batas_tinggi_laki = float(input("Masukkan batas tinggi badan laki-laki (cm): "))
            if batas_tinggi_laki <= 0:
                raise ValueError("Batas tinggi badan laki-laki harus lebih besar dari 0.")
            break  # Jika input valid, keluar dari loop
        except ValueError as e:
            print(f"Input tidak valid: {e}. Harap masukkan batas tinggi badan laki-laki yang valid.")
            time.sleep(2)
            os.system("cls")

    while True:
        try:
            batas_tinggi_perempuan = float(input("Masukkan batas tinggi badan perempuan (cm): "))
            if batas_tinggi_perempuan <= 0:
                raise ValueError("Batas tinggi badan perempuan harus lebih besar dari 0.")
            break  # Jika input valid, keluar dari loop
        except ValueError as e:
            print(f"Input tidak valid: {e}. Harap masukkan batas tinggi badan perempuan yang valid.")
            time.sleep(2)
            os.system("cls")

    # Input nilai tes minimum
    while True:
        try:
            nilai_minimum = int(input("Masukkan nilai tes minimum: "))
            if nilai_minimum <= 0:
                raise ValueError("Nilai tes minimum harus lebih besar dari 0.")
            break  # Jika input valid, keluar dari loop
        except ValueError as e:
            print(f"Input tidak valid: {e}. Harap masukkan nilai tes minimum yang valid.")
            time.sleep(2)
            os.system("cls")

    # Simpan parameter seleksi ke CSV
    simpan_parameter_seleksi_csv(tahun, bobot, batas_tinggi_laki, batas_tinggi_perempuan, nilai_minimum)