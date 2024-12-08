# KELAS B, KELOMPOK 9, DAFTAR ANGGOTA
1. Linda Rahmadani (I0324052) akun github : lindarahma123
2. Lisa Christy Natalia (I0324053) akun github : aethenially
3. Umrina Aulia (I0324069) akun github : umrinaaulia

# Sistem Seleksi Sekolah Kedinasan
Program ini dirancang untuk membantu menentukan kelayakan calon siswa dalam mengikuti seleksi sekolah kedinasan. Penilaian dilakukan secara komprehensif dengan mempertimbangkan beberapa elemen penting, seperti Indeks Massa Tubuh (IMT), hasil tes tertulis, serta tinggi badan minimal yang sesuai dengan ketentuan. Masing-masing bagian dari tes tertulis—Tes Intelegensia Umum (TIU), Tes Wawasan Kebangsaan (TWK), dan Tes Karakteristik Pribadi (TKP)—memiliki bobot penilaian yang berbeda, yang mencerminkan pentingnya setiap aspek dalam proses seleksi.


# Fitur-fitur aplikasi
1. Input data calon siswa (pendaftar)
2. Perhitungan Indeks Massa Tubuh (IMT)
3. Perhitungan nilai tes tertulis berdasarkan jumlah benar dalam menjawab soal TIU, TWK, dan TKP sesuai dengan bobot yang ditentukan.
4. Penyaringan calon siswa berdasarkan tinggi badan minimal, nilai tes tertulis, dan IMT sesuai dengan jenis kelamin pendaftar.
5. Penyajian output berupa lolos tidaknya peserta dalam bentuk tabel.

# Diagram Alir 
![FLOWCHART TUBES rev 2 3](https://github.com/user-attachments/assets/29efcfc2-b34d-4400-a072-0d1aed75d7a3)


kelompok kami membuat program seleksi masuk kedinasan. program ini memiliki alur sebagai berikut, mula mula user melaku kan login atau signin, setelah berhasil lalu input jumlah pendaftar (n), i = 0 lalu input bobot nilai tes tertulis (TIU, TWK, TKP) dengan bobot tersebut merupakan nilai benar per soal. lalu input batas tinggi badan minimal laki-laki dan perempuan  lalu input nilai tes tertulis minimal yang menjadi acuan untuk menentukan lolos atau tidaknya. lalu lakukan looping dengan input nama pendaftar, jenis kelamin, tinggi badan dan berat badan, jumlah soal yang benar pada TIU, TWK, TKP. setelah n terpenuhi lalu lanjut untuk menghitung IMT pendaftar dengan rumus IMT = BB/TB^2. selanjutnya hitung nilai tes tertulis dengan rumus Nilai Tes Tertulis = (Jmlh benar TIU bobot TIU) + (jmlh benar TWK bobot TWK) + (jmih benar TKP bobot TKP). setelah data disimpan lalu percabangan dengan penentuan jenis kelamin, jika laki laki di seleksi dengan batas tinggi badan minimal, 18,5 <= IMT <= 24,9 dan seleksi dengan nilai tes tulis minimal. jika perempuan seleksi tinggi badan minimal dan 18,5 <= IMT <= 24,9 serta minimum nilai tes tulis, program ini menghasilkan output berupa nama pendaftar, nilai pendaftar, IMT dan status pendaftar berupa lolos seleksi atau tidak lolos seleksi dalam ntuk tabel.