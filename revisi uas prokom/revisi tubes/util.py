
import os 
import time

def tampilkan_tabel(pendaftar):
    if not pendaftar:
        print("Tidak ada data peserta untuk ditampilkan.")
        return

    print("=" * 90)
    print("{:<20} {:<15} {:<15} {:<15} {:<15} {:<10} {:<10}".format(
        "Nama", "Jenis Kelamin", "Tinggi Badan", "Berat Badan", "IMT", "status", "Total Nilai"))
    print("=" * 90)
    
    for peserta in pendaftar:
        print("{:<20} {:<15} {:<15} {:<15} {:<15} {:<10} {:<10}".format(
            peserta['nama'], peserta['jenis_kelamin'], peserta['tinggi_badan'], 
            peserta['berat_badan'], peserta['imt'], peserta['status'], peserta['nilai_tes']))
    print("=" * 90)

def tampilkan_berdasarkan_status(pendaftar, status):
    peserta_lolos = [peserta for peserta in pendaftar if peserta['status'] == status]
    if peserta_lolos:
        print("=" * 100)
        print("{:<20} {:<15} {:<15} {:<15} {:<10} {:<15} {:<10}".format(
            "Nama", "Jenis Kelamin", "Tinggi Badan", "Berat Badan", "IMT", "status", "Total Nilai"))
        print("=" * 100)
        for peserta in peserta_lolos:
            print("{:<20} {:<15} {:<15} {:<15} {:<10} {:<15} {:<10}".format(
                peserta['nama'], peserta['jenis_kelamin'], peserta['tinggi_badan'], 
                peserta['berat_badan'], peserta['imt'], peserta['status'], peserta['nilai_tes']))
    else:
        print("tidak ada peseta yang lolos pada tahun ini")
        print("Tekan enter untuk kembali ke menu!")
        input()
        os.system('cls')
        print("Kembali ke menu...")
        time.sleep(2)
        os.system('cls')
        
        
        
        
        
        
        
        
        
        
        
        
        
