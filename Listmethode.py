numbers = [5,2,1,7,4]
numbers.append(20)
print(numbers)
#add number 20

numbers = [5,2,1,7,4]
numbers.insert(0, 10)
print(numbers)
#add insert in sequence 0

numbers = [5,2,1,7,4]
numbers.remove(5)
print(numbers)
#remove at indexes 5

numbers = [5,2,1,7,4]
numbers.clear()
print(numbers)
#menghapus isi list

numbers = [5,2,1,7,4]
numbers.pop()
print(numbers)
#menghapus list terakhir

numbers = [5,0,1,7,4]
print(numbers.index(4))
#mencari tahu index ke berapa untuk list dengan nilai 4

numbers = [5,2,1,5,7,4]
print(numbers.count(5))
#mencari tahu count list dengan nilai 5

numbers = [5,2,1,5,7,4]
numbers.sort()
print(numbers)
#mensort daftar list secara urut

numbers = [5,2,1,5,7,4]
numbers.sort()
numbers.reverse()
print(numbers)
#mensort daftar list secara urut dari belakang

numbers = [5,2,1,5,7,4]
numbers2 = numbers.copy()
numbers.append(10)
numbers3 = numbers.copy()

print(numbers2)
print(numbers3)

print('#'*100)
print('write program that REMOVE THE DUPLICATES IN THE LIST')


