
#soal pertama
angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

#soal ke2
try:
    angka1 = int(input('Masukkan angka pertama: '))
    angka2 = int(input("masukkan angka kedua : "))
    hasil = angka1 / angka2
    print(f'Hasil bagi antara {angka1} dengan {angka2} yaitu = {hasil}')

except ValueError:
    print('Error: Input harus berupa angka!')

except ZeroDivisionError:
    print('Error: Tidak bisa dibagi dengan nol!')

except Exception as e:
    print(f'Error tidak terduga: {e}')