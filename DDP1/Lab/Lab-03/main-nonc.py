# Name : Franky Raymarcell Sinaga
# Class: DDP1 ~ C
# This code was made for fun from non-DDP1 C Lab task

file_found = False
while not file_found:
    print("Selamat datang! Masukkan dua nama file yang berisi daftar makanan yang kamu miliki.")
    file_in_str = input("Masukkan nama file input daftar makanan: ") # Lab3/inputs/in1.txt
    file_out_str = input("Masukkan nama file output: ")

    try:
        file_in = open(file_in_str, "r")
        file_found = True
    except FileNotFoundError:
        print("Maaf, file input tidak ada")
        continue

makanan_list = file_in.readlines()

makanan_gabungan = ""
makanan_persamaan = ""

makanan_1 = ""
temp_makanan_1 = makanan_list[0][18:-1]
indeks_koma = 0
while indeks_koma != -1:
    temp_idx_comma = temp_makanan_1.find(",", indeks_koma + 1)

    if temp_idx_comma == -1:
        makanan = temp_makanan_1[indeks_koma + 1:].lower()
    elif indeks_koma == 0:
        makanan = temp_makanan_1[:temp_idx_comma].lower()
    else:
        makanan = temp_makanan_1[indeks_koma + 1:temp_idx_comma].lower()

    if makanan not in makanan_1:
        makanan_1 += "," + makanan

    indeks_koma = temp_idx_comma

# Menambahkan makanan_1 ke makanan_gabungan
makanan_gabungan = makanan_1

makanan_2 = ""
temp_makanan_2 = makanan_list[1][18:]
indeks_koma = 0
while indeks_koma != -1:
    temp_idx_comma = temp_makanan_2.find(",", indeks_koma + 1)

    if temp_idx_comma == -1:
        makanan = temp_makanan_2[indeks_koma + 1:].lower()
    elif indeks_koma == 0:
        makanan = temp_makanan_2[:temp_idx_comma].lower()
    else:
        makanan = temp_makanan_2[indeks_koma + 1:temp_idx_comma].lower()

    if makanan not in makanan_2:
        makanan_2 += "," + makanan
    if makanan not in makanan_gabungan:
        makanan_gabungan += "," + makanan
    if makanan in makanan_1:
        makanan_persamaan += "," + makanan

    indeks_koma = temp_idx_comma

# Menghilangkan koma di awal string
makanan_1 = makanan_1[1:]
makanan_2 = makanan_2[1:]
makanan_gabungan = makanan_gabungan[1:]
makanan_persamaan = makanan_persamaan[1:]

file_in.close()

running = True
pesan_output = ""
while running:
    print("Apa yang ingin kamu lakukan?")
    print("================================================")
    print("1. Tampilkan daftar makanan pertama")
    print("2. Tampilkan daftar makanan kedua")
    print("3. Tampilkan gabungan makanan dari dua daftar")
    print("4. Tampilkan makanan yang sama dari dua daftar")
    print("5. Keluar")
    print("================================================")
    menu = input("Masukkan aksi yang ingin dilakukan: ")

    if menu == "1":
        pesan = "Daftar makanan pertama:\n" + makanan_1
        print(pesan)
        pesan_output += pesan + "\n" * 2
    elif menu == "2":
        pesan = "Daftar makanan kedua:\n" + makanan_2
        print(pesan)
        pesan_output += pesan + "\n" * 2
    elif menu == "3":
        pesan = "Gabungan makanan favorit dari kedua daftar:\n" + makanan_gabungan
        print(pesan)
        pesan_output += pesan + "\n" * 2
    elif menu == "4":
        if makanan_persamaan == "":
            pesan = "Tidak ada makanan yang sama dari kedua daftar."
        else:
            pesan = "Makanan yang sama dari dua daftar:\n" + makanan_persamaan
        print(pesan)
        pesan_output += pesan + "\n" * 2
    elif menu == "5":
        print("Terima kasih telah menggunakan program ini!\nSemua keluaran telah disimpan pada file", file_out_str)
        running = False

file_out = open(file_out_str, "w")
file_out.write(pesan_output)
file_out.close()
