# LAB 8 for Foundation to Programming non-C Class
# Made by: Franky Raymarcell Sinaga (FrankyRayMS)

class Hotel:
    def __init__(self, name: str, rooms: int, price: int):
        # Nama hotel
        self.name = name
        # Banyaknya kamar tersedia
        self.available_room = rooms
        # Harga kamar
        self.room_price = price
        # Profit hotel
        self.profit = 0
        # Daftar guest/tamu/user
        self.guest = []

    def __str__(self):
        return self.name

    def __int__(self):
        return self.profit

    def __iter__(self):
        for guest in self.guest:
            yield guest

    def booking(self, guest, room):
        self.available_room -= room

        if guest not in self.guest:
            self.guest.append(guest)

        if self not in guest.hotel_list:
            guest.hotel_list.append(self)

        price = self.get_room_price(room)
        self.profit += price
        guest.money -= price

    def get_room_price(self, room = 0):
        return self.room_price * room


class User:
    def __init__(self, name: str, balance: int):
        # Nama user
        self.name = name
        # Saldo user
        self.money = balance
        # Daftar hotel yang dipesan
        self.hotel_list = []

    def __str__(self):
        return self.name

    def __int__(self):
        return self.money

    def __iter__(self):
        for hotel in self.hotel_list:
            yield hotel

    def topup(self, money) -> int:
        self.money += money
        return self.money


# Program
def cari_hotel(daftar_hotel: list[Hotel], nama: str) -> Hotel | None:
    try:
        daftar_nama = [str(hotel) for hotel in daftar_hotel]
        return daftar_hotel[daftar_nama.index(nama)]
    except ValueError:
        print("Nama hotel tidak ditemukan di sistem!")

def cari_user(daftar_user: list[User], nama: str) -> User | None:
    try:
        daftar_nama = [str(user) for user in daftar_user]
        return daftar_user[daftar_nama.index(nama)]
    except ValueError:
        print("Nama user tidak ditemukan di sistem!")


def main():
    # Initiate hotels and users
    hotels = []
    users = []

    banyak_hotel = int(input("Masukkan banyak hotel: "))
    banyak_user = int(input("Masukkan banyak user: "))

    for i in range(1, banyak_hotel+1):
        nama = input(f"\nMasukkan nama hotel ke-{i}: ")
        kamar = int(input(f"Masukkan banyak kamar hotel ke-{i}: "))
        harga = int(input(f"Masukkan harga kamar hotel ke-{i}: "))
        user = Hotel(nama, kamar, harga)
        hotels.append(user)

    for i in range(1, banyak_user+1):
        nama = input(f"\nMasukkan nama user ke-{i}: ")
        saldo = input(f"Masukkan saldo awal user ke-{i}: ")
        user = User(nama, saldo)
        users.append(user)

    running = True
    while running:
        print("\n=============Welcome to Paciloka!=============\n")
        perintah = input("Masukkan perintah: ")

        # Cetak daftar hotel dan user
        if perintah == "1": 
            print("Daftar Hotel")
            for idx in range(len(hotels)):
                print(f"{i+1}. {hotels[idx].name}")

            print("\nDaftar User")
            for idx in range(len(users)):
                print(f"{i+1}. {users[idx].name}")

        # Cetak profit hotel
        elif perintah == "2":
            nama = input("Masukkan nama hotel: ")
            hotel = cari_hotel(hotels, nama)
            if not hotel: continue

            print(f"Hotel dengan nama {str(hotel)} mempunyai profit sebesar {int(hotel)}")

        # Cetak saldo user
        elif perintah == "3":
            nama = input("Masukkan nama user: ")
            user = cari_user(users, nama)
            if not user: continue

            print(f"User dengan nama {str(user)} mempunyai saldo sebesar {int(user)}")

        # Topup saldo user
        elif perintah == "4":
            nama = input("Masukkan nama user: ")
            user = cari_user(users, nama)
            if not user: continue

            saldo = int(input("Masukkan jumlah uang yang akan ditambahkan ke user:"))
            if saldo <= 0:
                print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
                continue

            saldo_sekarang = user.topup(saldo)
            print(f"Berhasil menambahkan {saldo} ke user Dek depe. Saldo user menjadi {saldo_sekarang}")

        # Booking kamar hotel
        elif perintah == "5":
            nama_user = input("Masukkan nama user: ")
            user = cari_user(users, nama_user)
            if not user: continue

            nama_hotel = input("Masukkan nama hotel: ")
            hotel = cari_hotel(hotels, nama_hotel)

            kamar = int(input("Masukkan jumlah kamar yang akan di-booking: "))
            if kamar <= 0:
                print("Jumlah kamar yang akan dipesan harus lebih dari 0!")
                continue

            if hotel.available_room < kamar:
                print("Booking tidak berhasil!")
                continue

            # Cek saldo
            if hotel.get_room_price(kamar) > int(user):
                print("Booking tidak berhasil!")
                continue

            hotel.booking(user, kamar)
            print(f"User dengan nama {str(user)} berhasil melakukan booking di hotel {str(hotel)} dengan jumlah {kamar} kamar!")

        elif perintah == "6":
            nama = input("Masukkan nama hotel: ")
            hotel = cari_hotel(hotels, nama)
            if not hotel: continue

            print(f"{str(hotel)} | {', '.join([str(user) for user in list(hotel)])}")

        elif perintah == "7":
            nama = input("Masukkan nama user: ")
            user = cari_user(users, nama)
            if not user: continue

            print(f"{str(user)} | {', '.join([str(hotel) for hotel in list(user)])}")

        # Keluar dari program
        elif perintah == "8":
            print("Terima kasih sudah mengunjungi Paciloka!")
            running = False

        else:
            print("Absurd lu!")


# Run the program
if __name__ == "__main__":
    main()
