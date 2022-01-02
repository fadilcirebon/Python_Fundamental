coordinates = (1, 2, 3)
x, y, z = coordinates
print(y)

customer = {
    'name':'john',
    'email':'johnwick@gmail.com',
    'phone':'123456'}
print(customer)

phone= input('phone: ')
digit_mapping   ={
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven'
    }

output=''
for ph in phone:
    output += digit_mapping.get(ph,'!')+' '

print(output)