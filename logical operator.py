#using two condition
#contoh misal ada dua kondisi yang dibutuhkan, dibutuhkan pengalaman programmer 1 bulan dan jenis kelamin laki-laki.

print('LOGICAL AND')
print('')
gender_male = True
experience_one_month = False

if gender_male and experience_one_month:
    print('enter as shortlist candidate')
else:
    print('skip the applicant')

print('')
print('LOGICAL OR')
print('')
gender_male = True
experience_one_month = False

if gender_male or experience_one_month:
    print('enter as shortlist candidate')
else:
    print('skip the applicant')