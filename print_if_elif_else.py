course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course.find('e'))
print(course.replace('P','J'))
print(course.replace('Python','Anaconda'))
print('python' in course)
print(len(course))
print(course.title())


#ARITHMETIC OPERATION
x = 10 + 3 * 2
print(x)
# exponetiation 2 **3
# multiplication or division
# addition or subtraction

x = (2+3) * 10 -3
print(x)

#round function (fungsi pembulatan) contoh
print('fungsi pembulatan')
y = 4.50
print(round(y))




#fungsi absolute number
x = -17
print(abs(x))
#


# IF ELSE

# if it's hot'
#     it's a hot day' \
#     drink plenty of water
# otherwise if it's cold' \
#     it's a cold day' \
#     wear warm clothes

hot_day = True
cold_day = False

print(' ')
print(' ')
print(' ')
print(' **Fungsi If dan else**')
if hot_day:
    print("it's a hot day")
    print('drink a plenty of water')
elif cold_day:
    print('it is a cold day')
    print('use your jacket')
else:
    print('its lovely day')

print(f'alhamdulillah alaa kulli hal, enjoy your day')

print('')
print('')
print('EXAMPLE')
# price of a house is 1 million
# if buyer has a good credit
#     put down 10 % dp
# otherwise
#     they need to put down 20 %

good_credit = False
bad_credit = False

if good_credit:
    print('put down 10 % DP')
elif bad_credit:
    print('put down 20 % DP')
else:
    print('check testimony from their office')

print('thanks for your visiting')


print('')
print('**EXAMPLE 2**')
experience_programming = False
not_experience_yet= True

if experience_programming:
    print('easy learning a new language')
elif not_experience_yet:
    print('need more and more exercise')
else:
    print('anyway learning is always fun')
print('alhamdulillah alaa kulli hal')


print('')
print('**EXAMPLE 3, Sholat Subuh**')
shubuh_in_a_mosque = True
shubuh_in_home = False

if shubuh_in_a_mosque:
    print('Cah bagus, Insya Allah dicintai Allah')
elif shubuh_in_home:
    print('Cah bagus, apakah di tempatmu sedang hujan atau sedang pandemi')
else:
    print('Mengapa anda tidak sholat')
print('Mohonlah pertolongan Allah dengan sabar dan sholat')


print('')
print('**EXAMPLE 4, Pemilu 2024**')
usia = input('berapa usiamu di 2024?: ')


if int(usia)< 18:
    print('belum cukup usia')
elif int(usia)>80:
    print('Perbanyak istighfar, udah tua kek')
else:
    print('Cocok nih, pilihlah yang benar benar memperjuangkan rakyat')


print('')
print('**EXAMPLE 5, Muslim atau Muslimah**')
memakai_jilbab = False
pakai_baju_koko = False

if memakai_jilbab:
    print('Berati kamu muslimah, insya ALlah kamu taat ya dan ahli syurga')
elif pakai_baju_koko:
    print('berati kamu muslim, jangan lupakan sholat ya')
else:
    print('Asal menutup aurat, syahdat dan sholat maka anda muslim')
print('Mohonlah pertolongan Allah dengan sabar dan sholat')



print('')
print('**EXAMPLE 6, Uang Muka Perumahan**')
harga_rumah = 500000000
have_good_record=False

if have_good_record:
    downpayment = 0.1 * harga_rumah
else:
    downpayment = 0.5 * harga_rumah
print(f'DP yang dibayar:IDR {downpayment}')

