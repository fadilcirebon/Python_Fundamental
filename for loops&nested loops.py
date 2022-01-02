print('berikut fungsi for loop sederhana:')
total = 0
for item in range(1,101):
    print(item)
    total += (item)
print(f'total jumlah jamleh 1 sampai 100 adalah : {total}')


print('')
print('')
print('Loops untuk 1000 bilangan kuadrat pertama')
#penggunaan loops untuk rumus Jumlah 4 buah bilangan kuadrat pertama adalah 30 (30=1+4+9+16),
# berapakah jumlah 1000 bilangan kuadrat pertama?

total = 0
for item in range(1, 1001):
    total += (item ** 2)
    print((item)**2)

print(f'total jumlah dari bilangan 1000 bilangan kuadrat pertama  adalah: {total}')

print('')
print('')
print('NESTED LOOP EXAMPLE')
for x in range(4):
    for y in range(3):
        print('f({x},{y})')


print('NESTED LOOP EXAMPLE2')
numbers= [5,10,9,8,2]
for item in numbers:
    print('x' * item)

print('')
print('MENCARI BILANGAN TERBESAR DALAM SUATU LIST')

numbers = [100, 50, 3000, 2000]
max = numbers[0]

for number in numbers:
    if number>max:
        max=number

print(max)

