print('='*10)
print('Kalkulator Sederhana')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3  Perkalian')
print('4. Pembagian')
print('='*10)

option = input('Silahkan pilih operasi 1/2/3/4')
bil_1 = eval(input('Masukkan bilangan pertama: '))
bil_2 = eval(input('Masukkan bilangan kedua: '))

print('=' *10)

if option == '1':
    hasil = bil_1 + bil_2
    print(f'Hasil operasi dari {bil_1} + {bil_2} = {hasil}')
