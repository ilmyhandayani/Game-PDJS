#================================================================================
#Program Petani-Domba-Jagung-Serigala
#Pemain harus memindahkan petani, domba, jagung, dan serigala ke seberang sungai 
#menggunakan perahu yang hanya dapat memuat petani dan satu bawaan
#================================================================================
#import library
import os

#sub program (prosedur dan fungsi)

def tampil_gambar(list_kiri, list_kanan): 
    print("Pindahkan Petani (P), Jagung (J), Domba (D), dan Serigala (S) ke sisi kanan!\n")
    if 'P' in list_kiri:
        print(" ".join([str(a) for a in list_kiri]),"                               "," ".join([str(a) for a in list_kanan]))
        print("=======","\_____/",",,,,,,,,,,,,,,","=======")
    elif 'P' in list_kanan:
        print(" ".join([str(a) for a in list_kiri]),"                               "," ".join([str(a) for a in list_kanan]))
        print("=======",",,,,,,,,,,,,,,","\_____/","=======")
    
def menyeberang(list_kiri, list_kanan):

    print("Masukkan yang Ingin anda sebrangkan")
    pilihan = str(input("Domba(D)/Serigala(S)/Jagung(J) : ").upper())
    if pilihan in list_kiri:
        
        if pilihan == 'P' :
            list_kiri.remove('P')
            list_kanan.append('P')
        elif pilihan in list_kiri and 'P' in list_kiri:  
            list_kiri.remove('P')
            list_kiri.remove(pilihan)
            list_kanan.append('P')
            list_kanan.append(pilihan)
        else:
            print("Pilihan anda tidak bersama petani")
            input("Enter")
        
            

    elif pilihan in list_kanan:
        if pilihan == 'P' :
            list_kanan.remove('P')
            list_kiri.append('P')
        elif pilihan in list_kanan and 'P' in list_kanan:
            list_kanan.remove('P')
            list_kanan.remove(pilihan)
            list_kiri.append('P')
            list_kiri.append(pilihan)
        else :
            print("Pilihan anda tidak bersama petani")
            input("Enter")
    else:
        print("Pilihan Tidak Ada")
        input("Enter")


def cek_selesai(list_kiri, list_kanan):
    if ('P' in list_kanan and 'J' in list_kanan and 'D' in list_kanan and 'S' in list_kanan):
        print("\nSELAMAT, Anda berhasil memindahkan keempatnya ke seberang!")
        input()
        return 1
    elif ('P' in list_kanan and 'J' in list_kiri and 'D' in list_kiri and 'S' in list_kiri):
        print("\nAnda gagal. Mereka akan saling memakan!")
        input()
        return 1
    elif ('J' in list_kiri and 'D' in list_kiri and 'P' in list_kanan):
        print("\nAnda gagal. Jagungnya habis dimakan Domba!")
        input()
        return 1
    elif ('J' in list_kanan and 'D' in list_kanan and 'P' in list_kiri):
        print("\nAnda gagal. Jagungnya habis dimakan Domba!")
        input()
        return 1
    elif ('S' in list_kiri and 'D' in list_kiri and 'P' in list_kanan):
        print("\nAnda gagal. Dombanya mati dimakan Serigala!")
        input()
        return 1
    elif ('S' in list_kanan and 'D' in list_kanan and 'P' in list_kiri):
        print("\nAnda gagal. Dombanya mati dimakan Serigala!")
        input()
        return 1

    #kondisi lainnya (masih lanjut main)
    else:
        return 0

    
#program utama
os.system("cls")
list_kiri = ['P', 'J', 'D', 'S']
list_kanan = []
selesai = False     #False jika permainan belum berakhir. True jika permainan berakhir
main_lagi = 'Y'     #'Y' jika user ingin bermain lagi. 'T' jika user tidak ingin bermain lagi


tampil_gambar(list_kiri, list_kanan)

while (main_lagi.upper() == 'Y'):
    menyeberang(list_kiri, list_kanan)

    os.system("cls")
    tampil_gambar(list_kiri, list_kanan)

    selesai = cek_selesai(list_kiri, list_kanan)

    #jika selesai = True, tanya apakah mau main lagi atau tidak
    if (selesai):
        main_lagi = input("\nMain lagi (Y/T)? ")

        #jika main_lagi = 'Y', reset lagi list_kiri dan list_kanan
        os.system("cls")
        list_kiri = ['P', 'J', 'D', 'S']
        list_kanan = []
        tampil_gambar(list_kiri, list_kanan)



