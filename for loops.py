print('berikut fungsi for loop sederhana:')
total = 0
for item in range(1,100):
    print(item)

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


