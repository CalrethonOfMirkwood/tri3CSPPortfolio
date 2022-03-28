import week0.week0
import week1.week1
import week2.palindrome
import week2.calculator
import week2.factorial

def menu():
    while True:
        try:
            week = int(input('Enter your week (0-2): '))
            if week == 0:
                week0.week0.printMenu()
                option = int(input('Enter your option: '))
                if option == 1:
                    print()
                    week0.week0.bananaphone()
                    print()
                elif option == 2:
                    print()
                    week0.week0.waragainstchristmas()
                    print()
                elif option == 3:
                    week0.week0.loading()
                elif option == 4:
                    print('Exiting! Thank you! Good Bye...')
                    exit()
                else:
                    print('Invalid option. Please enter a number between 1 and 4.')
            elif week == 1:
                week1.week1.printMenu()
                option = int(input('Enter your option: '))
                if option == 1:
                    week1.week1.week1loops()
                elif option == 2:
                    week1.week1.week1fibonacci()
                elif option == 3:
                    print('Exiting! Thank you! Good Bye...')
                    exit()
                else:
                    print('Invalid option. Please enter a number between 1 and 3.')
            elif week == 2:
                print('1 -- Calculator')
                print('2 -- Factorial')
                print('3 -- Palindrome')
                print('4 -- Exit')
                option = int(input('Enter your option: '))
                if option == 1:
                    week2.calculator.calcfunction()
                elif option == 2:
                    week2.factorial.factorialfunction()
                elif option == 3:
                    week2.palindrome.palindromefunction()
                elif option == 4:
                    print('Exiting! Thank you! Good Bye...')
                else:
                    print('Invalid option. Please enter a number between 1 and 3.')
            else:
                print('Invalid option. Please enter a number between 0 and 2.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

menu()
