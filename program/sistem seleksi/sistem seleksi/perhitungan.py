def hitung_imt(berat_badan, tinggi_badan):
    """Fungsi untuk menghitung IMT."""
    return berat_badan / (tinggi_badan / 100) ** 2

def hitung_nilai_tes_tulis(jml_benar_tiu, jml_benar_twk, jml_benar_tkp, bobot_tiu, bobot_twk, bobot_tkp):
    """Fungsi untuk menghitung nilai tes tulis."""
    return (jml_benar_tiu * bobot_tiu) + (jml_benar_twk * bobot_twk) + (jml_benar_tkp * bobot_tkp)

def seleksi(pendaftar, batas_tinggi_laki, batas_tinggi_perempuan, nilai_minimum, bobot_tiu, bobot_twk, bobot_tkp):
    for peserta in pendaftar:
        imt = hitung_imt(peserta['berat_badan'], peserta['tinggi_badan'])
        
        jml_benar_tiu = peserta.get('jml_benar_tiu', 0)
        jml_benar_twk = peserta.get('jml_benar_twk', 0)
        jml_benar_tkp = peserta.get('jml_benar_tkp', 0)
        
        # Hitung nilai tes dengan data yang valid
        nilai_tes = hitung_nilai_tes_tulis(
            jml_benar_tiu, jml_benar_twk, jml_benar_tkp,
            bobot_tiu, bobot_twk, bobot_tkp
        )
        
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
