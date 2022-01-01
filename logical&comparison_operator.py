#using two condition
#contoh misal ada dua kondisi yang dibutuhkan, dibutuhkan pengalaman programmer 1 bulan dan jenis kelamin laki-laki.
# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b (sama dengan)
# Not Equals: a != b (tidak sama dengan)
# Less than: a < b (lebih kecil)
# Less than or equal to: a <= b (lebih kecil atau sama dengan)
# Greater than: a > b
# Greater than or equal to: a >= b

print('LOGICAL AND')
print('')
gender_male = True
experience_one_month = False

if gender_male and experience_one_month:
    print('enter as shortlist candidate')
else:
    print('skip the applicant')

print('***'*100)
print('LOGICAL OR')
print('')
gender_male = True
experience_one_month = False

if gender_male or experience_one_month:
    print('enter as shortlist candidate')
else:
    print('skip the applicant')



print('***'*100)
print('LOGICAL and not')
print('')
gender_male = True
has_criminal_record = True

if gender_male and not has_criminal_record:
    print('enter as shortlist candidate')
else:
    print('Danger, the candidate has criminal record')



print('***'*100)
print('EXAMPLE USING LEN AND CONDITION IF')
print('')
name = 'gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg'

if len(name)<3:
    print('at least name more than 3 characters')
elif len(name)>50:
    print('name not more than 50 characters')
else:
    print('sound the good name')
