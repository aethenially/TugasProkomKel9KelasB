# peserta.py
import csv
import os

def hitung_nilai_tes_tulis(jml_benar, bobot):
    """Fungsi untuk menghitung nilai tes tulis secara dinamis berdasarkan input mata tes."""
    return sum(jml_benar[mata_tes] * bobot[mata_tes] for mata_tes in bobot)


def hitung_imt(tinggi_badan, berat_badan):
    tinggi_meter = tinggi_badan / 100.0  # Mengkonversi tinggi badan ke meter
    imt = berat_badan / (tinggi_meter ** 2)
    return round(imt, 2)

def baca_pendaftar_csv(tahun):
    file_name = f'peserta_{tahun}.csv'
    pendaftar = []

    # Membaca file CSV jika ada
    try:
        with open(file_name, mode='r') as file:
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
        return pendaftar
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
        return None
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
        return None

def seleksi(pendaftar, parameter):
    bobot = parameter['bobot']
    batas_tinggi_laki = parameter['batas_tinggi_laki']
    batas_tinggi_perempuan = parameter['batas_tinggi_perempuan']
    nilai_minimum = parameter['nilai_minimum']

    for peserta in pendaftar:
        total_nilai = hitung_nilai_tes_tulis(peserta['jml_benar'], bobot)
        peserta['nilai_tes'] = total_nilai
        imt = hitung_imt(peserta['tinggi_badan'], peserta['berat_badan'])
        peserta['imt'] = imt
        
        if (peserta['jenis_kelamin'] == 'L' and peserta['tinggi_badan'] >= batas_tinggi_laki) and 18.5 <= peserta['imt'] <= 24.9 or \
           (peserta['jenis_kelamin'] == 'P' and peserta['tinggi_badan'] >= batas_tinggi_perempuan) and 18.5 <= peserta['imt'] <= 24.9:
            if peserta['nilai_tes'] >= nilai_minimum:
                peserta['status'] = 'Lolos'
            else:
                peserta['status'] = 'Tidak Lolos'
        else:
            peserta['status'] = 'Tidak Lolos'

def simpan_pendaftar_csv(pendaftar, tahun, parameter):
    file_name = f'peserta_{tahun}.csv'
    file_exists = os.path.isfile(file_name)
    existing_data = set()
    if file_exists:
        with open(file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_data.add(row['Nama'])  # Simpan nama peserta yang sudah ada

    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Nama', 'Jenis Kelamin', 'Tinggi Badan (cm)', 'Berat Badan (kg)', 'IMT', 'Nilai Tes', 'Status'])
        for peserta in pendaftar:
            imt = hitung_imt(peserta['tinggi_badan'], peserta['berat_badan'])
            peserta['imt'] = imt
            seleksi(pendaftar, parameter)
            if peserta['nama'] not in existing_data:
                writer.writerow([
                    peserta['nama'], peserta['jenis_kelamin'], peserta['tinggi_badan'], peserta['berat_badan'],
                    peserta['imt'], peserta['nilai_tes'], peserta['status']
                ])


