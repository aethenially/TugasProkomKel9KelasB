# KELAS B, KELOMPOK 9, DAFTAR ANGGOTA
1. Linda Rahmadani (I0324052) akun github : lindarahma123
2. Lisa Christy Natalia (I0324053) akun github : aethenially
3. Umrina Aulia (I0324069) akun github : umrinaaulia

# Sistem Seleksi Sekolah Kedinasan
kelompok kami membuat program seleksi untuk masuk sekolah kedinasan. program ini memiliki alur sebagai berikut, mula mula user melakukan login atau signin, setelah berhasil lalu input jumlah pendaftar (n), i = 0 lalu input bobot nilai tes tertulis (TIU, TWK, TKP) dengan bobot tersebut merupakan nilai benar per soal. lalu input batas tinggi badan minimal laki-laki dan perempuan, lalu input nilai tes tertulis minimal yang menjadi acuan untuk menentukan lolos atau tidaknya. lalu lakukan looping dengan input nama pendaftar, jenis kelamin, tinggi badan dan berat badan, jumlah soal yang benar pada TIU, TWK, TKP. setelah n terpenuhi lalu lanjut untuk menghitung IMT pendaftar dengan rumus IMT = BB/TB^2. selanjutnya hitung nilai tes tertulis dengan rumus Nilai Tes Tertulis = (Jmlh benar TIU bobot TIU) + (jmlh benar TWK bobot TWK) + (jmlh benar TKP bobot TKP). setelah data disimpan lalu percabangan dengan penentuan jenis kelamin, jika laki laki di seleksi dengan batas tinggi badan minimal, 18,5 <= IMT <= 24,9 dan seleksi dengan nilai tes tulis minimal. jika perempuan seleksi tinggi badan minimal dan 18,5 <= IMT <= 24,9 serta minimum nilai tes tulis, program ini menghasilkan output berupa nama pendaftar, nilai pendaftar, IMT dan status pendaftar berupa lolos seleksi atau tidak lolos seleksi dalam ntuk tabel.


# Fitur-fitur aplikasi
1. Input data calon siswa (pendaftar)
2. Perhitungan Indeks Massa Tubuh (IMT)
3. Perhitungan nilai tes tertulis berdasarkan jumlah benar dalam menjawab soal TIU, TWK, dan TKP sesuai dengan bobot yang ditentukan.
4. Penyaringan calon siswa berdasarkan tinggi badan minimal, nilai tes tertulis, dan IMT sesuai dengan jenis kelamin pendaftar.
5. Penyajian output berupa lolos tidaknya peserta dalam bentuk tabel.

# Diagram Alir 
![FLOWCHART TUBES rev 2 3](https://github.com/user-attachments/assets/29efcfc2-b34d-4400-a072-0d1aed75d7a3)


Flowchart ini menggambarkan proses seleksi kelulusan berdasarkan beberapa kriteria, yaitu tinggi badan minimum sesuai dengan jenis kelamin, nilai tes tertulis yang mencakup TWK, TIU, dan TKP yang masing-masing memiliki bobot yang telah ditetapkan, dan Indeks Massa Tubuh (IMT) yang ideal yaitu antara 18,5 – 24,9. 
Setelah menginput kriteria lalu kita dapat melanjutkannya dengan menginput jumlah pendaftar yang akan mengikuti seleksi, lalu menginput data diri berupa nama, jenis kelamin, tinggi badan, dan berat badan, serta  jumlah soal yang benar pada setiap jenis TKD (Tes Kompetensi Dasar). Program akan meminta input data setiap pendaftar selama i <= n. Jika sudah mencapai jumlah pendaftar, program akan otomatis melakukan perhitungan Indeks Massa Tubuh (IMT) dan Nilai Tes Tertulis lalu program akan melakukan proses penyeleksian berdasarkan kriteria yang telah ditetapkan dan menghasilkan output berupa lolos atau tidak lolos setiap pendaftar selama i <= n. jika sudah mencapai jumlah pendaftar program ini akan berakhir.






