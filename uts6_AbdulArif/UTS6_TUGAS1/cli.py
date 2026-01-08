from utils import *
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def input_sks(jumlah):
    sks_list = []
    print("--------- input sks ---------")
    for i in range(1, jumlah + 1):
        sks = int(input(f"SKS {i}: "))
        sks_list.append(sks)
    return sks_list


def input_nilai(jumlah):
    nilai_list = []
    print("--------- input nilai mahasiswa ---------")
    for i in range(1, jumlah + 1):
        nilai = float(input(f"Nilai {i}: "))
        nilai_list.append(nilai)
    return nilai_list


def kumpulan_menu():
    while True:
        cls()
        print("Daftar Menu")
        print("1. Konversi nilai ke label")
        print("2. Konversi label ke bobot")
        print("3. Hitung total sks yang diambil")
        print("4. Hitung total nilai")
        print("5. Hitung IPS")
        print("6. Exit")

        pilihan = input("Pilih menu: ")
        cls()

        if pilihan == "1":
            nilai = float(input("Nilai Mahasiswa: "))
            label = konversi_nilai_ke_label(nilai)
            print("Label:", label)
            input("")

        elif pilihan == "2":
            label = input("Label Nilai Mahasiswa: ")
            bobot = konversi_label_ke_bobot(label)
            print("Bobot Nilai:", bobot)
            input("")

        elif pilihan == "3":
            jumlah = int(input("Jumlah Data: "))
            sks_list = input_sks(jumlah)
            total = hitung_total_sks(sks_list)
            print("Total SKS:", total)
            input("")

        elif pilihan == "4":
            jumlah = int(input("Jumlah Data: "))
            sks_list = input_sks(jumlah)
            nilai_list = input_nilai(jumlah)
            total = hitung_total_nilai(sks_list, nilai_list)
            print("Total Nilai:", round(total, 2))
            input("")

        elif pilihan == "5":
            jumlah = int(input("Jumlah Data: "))
            sks_list = input_sks(jumlah)
            nilai_list = input_nilai(jumlah)
            ips = hitung_ips(sks_list, nilai_list)
            print("IPS:", round(ips, 2))
            input("")

        elif pilihan == "6":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")
            input("")
