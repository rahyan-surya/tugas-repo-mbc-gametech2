def main():
    import os
    import time
    print("-" *22)
    print("Selamat Datang")
    print("-" *22)
    print('='*22)
    print('Kalkulator Sederhana')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3  Perkalian')
    print('4. Pembagian')
    print('5. Exit')
    print('='*22)

    option = input('Silahkan pilih operasi: ')

    print('=' *10)

    if option == '1':
        bil_1 = eval(input('Masukkan bilangan pertama: '))
        bil_2 = eval(input('Masukkan bilangan kedua: '))
        hasil = bil_1 + bil_2
        print(f'Hasil operasi dari {bil_1} + {bil_2} = {hasil}')
        time.sleep(3)
        os.system('cls')
        main()
    elif option == '2':
        bil_1 = eval(input('Masukkan bilangan pertama: '))
        bil_2 = eval(input('Masukkan bilangan kedua: '))
        hasil = bil_1 - bil_2
        print(f'Hasil operasi dari {bil_1} - {bil_2} = {hasil}')
        time.sleep(3)
        os.system('cls')
        main()
    elif option == '3':
        bil_1 = eval(input('Masukkan bilangan pertama: '))
        bil_2 = eval(input('Masukkan bilangan kedua: ')) 
        hasil = bil_1 * bil_2 
        print(f'Hasil operasi dari {bil_1} * {bil_2} = {hasil}')
        time.sleep(3)
        os.system('cls')
        main()
    elif option == '4':
        bil_1 = eval(input('Masukkan bilangan pertama: '))
        bil_2 = eval(input('Masukkan bilangan kedua: ')) 
        hasil = bil_1 / bil_2   
        print(f'Hasil operasi dari {bil_1} / {bil_2} = {hasil}')
        time.sleep(3)
        os.system('cls')
        main()
    elif option == '5':
        exit()
    else :
        print('Pilihan tidak tersedia')
        time.sleep(2)
        os.system('cls')
        main()

def exit():
    pass

main()