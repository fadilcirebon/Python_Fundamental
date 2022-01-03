#contoh satu, dengan exception ValueError
try:
    age= int(input('Age:  '))
    print(age)
except ValueError:
    print('invalid value')


print('*' * 100)


#contoh 2 dengan exception ZeroDivisionError
try:
    age= int(input('Age:  '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age Cannot be 0')
except ValueError:
    print('invalid value')