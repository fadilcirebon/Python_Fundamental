birth_year = input('birth year: ')
age = 2021 - int(birth_year)
print(f'usia kamu sudah tua {age}')

# weight_pound = input('your weight in pound: ')
# kilos = 0.45 * float(weight_pound)
# print('your weight in kilos: ', kilos)


#disempuranakan
berat_badan = int(input('masukan berat kamu :  '))
unit = input('(L)bs atau (K)g:')

if unit.upper()== 'L':
    converted = berat_badan * 0.45
    print(f'Berat kamu {converted} kilos, dasar endut')
else:
    converted = berat_badan / 0.45
    print(f'Berat kamu {converted} pound')
