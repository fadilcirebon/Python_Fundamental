i = 1
while i <= 5:
    print('$' * i)
    i = i + 1
print('done')

# find the exercise for deep insight whiteloops
print('')
print('GUESS GAME')
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_limit > guess_count:
    guess = int(input('Guess:   '))
    guess_count += 1
    if guess == secret_number:
        print('You Won')
        break
else:
    print('Sorry you failed')

print('')
print('CAR GAME')

command = ''
started = False
while True:
    command = input(">").lower()
    if command == 'start':
        if started:
            print('car already started')
        else:
            started = True
            print('Engine started')
    elif command == 'stop':
        if not started:
            print('Car Already Stopped.')
        else:
            started = False
            print('car stopped')
    elif command == 'help':
        print('''
start - to start enggine
stop - to stop enggine
quit - to quit the car''')
    elif command == 'quit':
         print('sampai ketemu lagi kawan')
         break
    else:
        print('I dont understand, ngomong apa njenengan')

