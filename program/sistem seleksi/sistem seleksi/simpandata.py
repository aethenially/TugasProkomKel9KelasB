import os
import csv



def baca_pendaftar_csv():
    pendaftar = []
    try:
        with open('peserta.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pendaftar.append({
                    'nama': row['Nama'],
                    'jenis_kelamin': row['Jenis Kelamin'],
                    'tinggi_badan': float(row['Tinggi Badan (cm)']),
                    'berat_badan': float(row['Berat Badan (kg)']),
                    'imt': float(row['IMT']),
                    'nilai_tes': float(row['Nilai Tes']),
                    'status': row['Status']
                })
    except FileNotFoundError:
        print("File peserta.csv tidak ditemukan. Membuat file baru.")
    return pendaftar


def simpan_pendaftar_csv(pendaftar):
    # Baca data yang sudah ada di file CSV
    file_exists = os.path.isfile('peserta.csv')
    existing_data = set()
    if file_exists:
        with open('peserta.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_data.add(row['Nama'])  # Simpan nama peserta yang sudah ada

    # Tulis data baru tanpa duplikasi
    with open('peserta.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Nama', 'Jenis Kelamin', 'Tinggi Badan (cm)', 'Berat Badan (kg)', 'IMT', 'Nilai Tes', 'Status'])
        for peserta in pendaftar:
            if peserta['nama'] not in existing_data:  # Periksa apakah peserta sudah ada
                writer.writerow([
                    peserta['nama'], peserta['jenis_kelamin'], peserta['tinggi_badan'], peserta['berat_badan'],
                    peserta['imt'], peserta['nilai_tes'], peserta['status']
                ])

