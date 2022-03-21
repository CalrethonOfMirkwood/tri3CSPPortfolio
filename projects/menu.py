import time
from projects.week0.loading import loading

amogus = [ [1,2,3],[4,5,6],[7,8,9] ]

def printMenu():
    print('1 -- *ring ring ring*' )
    print('2 -- Christmas Tree' )
    print('3 -- Loading Bar' )
    print('4 -- Exit' )

def bananaphone():
    print('*phone noises*')
    for sus in amogus:
        for baka in sus:
            print(baka, end =" ")
        print()

def waragainstchristmas():
    print('O Christmas tree,')
    time.sleep(1)
    print('O happy I\'d be,')
    time.sleep(1)
    print('The joy to be...')
    time.sleep(1)
    for i in range(10):
        print(' '*(10-i)*3+'ZAMN! '*i)
        time.sleep(0.1)
        print()
    print((' '*28+'sus\n')*2)
    print("... together!")

def megaman():
    loading()

def runoptions():
    while True:
        try:
            printMenu()
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                print()
                bananaphone()
                print()
            elif option == 2:
                print()
                waragainstchristmas()
                print()
            elif option == 3:
                megaman()
            elif option == 4:
                print('Exiting! Thank you! Good Bye...')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

runoptions()
