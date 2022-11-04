import os

nama_barang = ["Shampoo","Soap","Snack","Coffee","Milk"]
Stock_toko = [1,2,3,4,5]
Stock_Inven = [5,5,5,5,5]

def Print_menu():
  print(" {:^24}     {:^24}".format("Menu Toko","Menu Inventory"))
  print("|No. {:15}{:5}  |  No. {:15}{:5}|".format("Nama Barang","Stock","Nama Barang","Stock"))
  for i in range(len(nama_barang)):
    print("|{:2}. {:15}{:5}  |  {:2}. {:15}{:5}|".format(i+1,nama_barang[i],Stock_toko[i],i+1,nama_barang[i],Stock_Inven[i]))
  print("\n1. Pindahin dari toko ke inventory")
  print("2. Pindahin dari inventory ke toko")
  choice = input("yg mana? ")
  if choice == '1':
    toko_inven()
  elif choice == '2':
    inven_toko()
  else:
    print("masukin 1 atau 2 doang")

def toko_inven():
  barang_yg_mana = int(input("\n1. Barang ke brp? "))
  jumlah =int(input("2. Jumlah mau brp? "))
  if (jumlah<=Stock_toko[barang_yg_mana-1]):
    Stock_Inven[barang_yg_mana-1] += jumlah
    Stock_toko[barang_yg_mana-1] -= jumlah
    print("barang berhasil dipindahkan",jumlah)
  else:
    print("barang ngk cukup, cuma ada",Stock_toko[barang_yg_mana-1],"barang")
  input("tekan enter untuk melanjutkan")

def inven_toko():
  barang_yg_mana = int(input("\n1. Barang ke brp? "))
  jumlah =int(input("2. Jumlah mau brp? "))
  if (jumlah<=Stock_Inven[barang_yg_mana-1]):
    Stock_toko[barang_yg_mana-1] += jumlah
    Stock_Inven[barang_yg_mana-1] -= jumlah
    print("barang berhasil dipindahkan",jumlah)
  else:
    print("barang ngk cukup, cuma ada ",Stock_Inven[barang_yg_mana-1],"barang")
  input("tekan enter untuk melanjutkan")

while True:
  Print_menu()
  os.system("clear")
