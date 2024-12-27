# akun.py
import csv
import hashlib
import os

akun_db = {}

def enkripsi_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def simpan_akun_csv():
    with open('akun.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'Password'])
        writer.writeheader()
        for username, password in akun_db.items():
            writer.writerow({'username': username, 'Password': password})

def baca_akun_csv():
    try:
        with open('akun.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                akun_db[row['username']] = row['Password']
    except FileNotFoundError:
        print("File akun.csv tidak ditemukan. Membuat file baru.")

def signup():
    os.system("cls")
    print("Membuat akun.")
    username = input("Masukkan username: ")
    if username in akun_db:
        print("Username sudah terdaftar.")
        return False
    password = input("Masukkan password: ")
    konfirmasi_password = input("Konfirmasi password: ")
    if password != konfirmasi_password:
        print("Password tidak cocok.")
        return False
    akun_db[username] = enkripsi_password(password)
    simpan_akun_csv()
    os.system("cls")
    print("Akun berhasil dibuat!")
    return True

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in akun_db and akun_db[username] == enkripsi_password(password):
        os.system("cls")
        print("Login berhasil!")
        return True
    os.system("cls")
    print("Username atau password salah.")
    return False
