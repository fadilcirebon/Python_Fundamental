def hitung_luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    return luas

var1 = hitung_luas_segitiga(5, 7)
print("Luas segitiga adalah:", var1)

def pangkat_dua (angka):
    return((angka) ** 2)

naga = pangkat_dua (7)
print(naga)

def square(number):
    square=number*number
    return square

print(square(9))



#CREATING REUSABLE FUNCTION
# menjadikan code emojis menjadi fungsi bernama emoji_converter
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ':)': '😊',
        ':(': '😌',
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return(output)

message = input('>')
print(emoji_converter(message))

