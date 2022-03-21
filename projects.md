{% include navbar.html %}

# [Replit Link](https://replit.com/@CalrethilOfMirk/tri3CSPPortfolio)
ALL PROJECT FILES ARE IN [`/projects`](https://github.com/CalrethonOfMirkwood/tri3CSPPortfolio/tree/master/projects) FOLDER

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@CalrethilOfMirk/tri3CSPPortfolio?embed=true"></iframe>

## TT1 Data Structure'
File is [`week.py`](https://github.com/CalrethonOfMirkwood/tri3CSPPortfolio/tree/master/projects/week1/week1.py)
```
InfoDb = []

# hack1
InfoDb.append({
    "FirstName": "David",
    "LastName": "Williams",
    "DoB": "02/24",
    "Residence": "Portland",
    "Email": "daveyw@protonmail.com",
    "WorkedFor":["National Security Agency", "Walmart", "San Diego Zoo"]
})

InfoDb.append({
    "FirstName": "Joe",
    "LastName": "Taylor",
    "DoB": "11/03",
    "Residence": "Fiji",
    "Email": "coolmanjoe@protonmail.com",
    "WorkedFor":["Walmart", "Petco", "Pho Ca Dao", "US Space Force"]
})

InfoDb.append({
    "FirstName": "Alex",
    "LastName": "Jones",
    "DoB": "08/12",
    "Residence": "Pittsburgh",
    "Email": "aj@sandysdogwash.com",
    "WorkedFor":["McDonalds", "Sandy's Dog Wash", "Self-employed", "Department of Defense", "Walmart"]
})

InfoDb.append({
    "FirstName": "Carl",
    "LastName": "Perkins",
    "DoB": "06/20",
    "Residence": "Salt Lake City",
    "Email": "carl@carlperkins.com",
    "WorkedFor":["Target", "Souplantation", "Google"]
})

# hack2
def for_loop():
    for x in InfoDb:
        print("First Name: " + x["FirstName"])
        print("Last Name: " + x["LastName"])
        print("DoB: " + x["DoB"])
        print("Residence: " + x["Residence"])
        print("Email: " + x["Email"])
        print("Worked For: ", end="")
        print(", ".join(x["WorkedFor"]))
        print()
    return


def while_loop():
    count = 0
    while count < len(InfoDb):
        print("First Name: " + InfoDb[count]["FirstName"])
        print("Last Name: " + InfoDb[count]["LastName"])
        print("DoB: " + InfoDb[count]["DoB"])
        print("Residence: " + InfoDb[count]["Residence"])
        print("Email: " + InfoDb[count]["Email"])
        print("Worked For: ", end="")
        print(", ".join(InfoDb[count]["WorkedFor"]))
        print()
        count += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print("First Name: " + InfoDb[n]["FirstName"])
        print("Last Name: " + InfoDb[n]["LastName"])
        print("DoB: " + InfoDb[n]["DoB"])
        print("Residence: " + InfoDb[n]["Residence"])
        print("Email: " + InfoDb[n]["Email"])
        print("Worked For: ", end="")
        print(", ".join(InfoDb[n]["WorkedFor"]))
        print()
        recursive_loop(n+1)
    return

def hack2():
    print("------------------For loop------------------")
    for_loop()
    print("------------------While loop------------------")
    while_loop()  # requires initial index to start while
    print("------------------Recursive loop------------------")
    recursive_loop(0)  # requires initial index to start recursion

def fibonacci(num):
    try:
        if num < 0 or type(num) != int:
            num2 = str(num)
            # python can return any type without type errors
            return ("An error occurred, please input a positive integer. " + num2 + " is not a valid input.")
        else:
            if num < 2:
                return num
            else:
                return fibonacci(num - 1) + fibonacci(num - 2)
    except:
        num2 = str(num)
        return ("An error occurred, please input a positive integer. " + num2 + " is not a valid input.")

def week1():
    print("hack2 loops:")
    print("------------------For loop------------------")
    for_loop()
    print("------------------While loop------------------")
    while_loop()  # requires initial index to start while
    print("------------------Recursive loop------------------")
    recursive_loop(0)  # requires initial index to start recursion
    print()
    print("hack3 recursive fibonacci sequence:")
    for x in range(11):
        print("fibonacci value for %d: %d" % (x, fibonacci(x)))
    print("------------------Error handling demonstration------------------")
    print("fibonacci value for -1: " + str(fibonacci(-1)))
    print("fibonacci value for 2.72: " + str(fibonacci(2.72)))
    print("fibonacci value for -5.23: " + str(fibonacci(-5.23)))

week1()

```

## TT0 Python Menu, Replit, GitHub
Files are [`menu.py`](https://github.com/CalrethonOfMirkwood/tri3CSPPortfolio/tree/master/projects/menu.py) and [`loading.py`](https://github.com/CalrethonOfMirkwood/tri3CSPPortfolio/tree/master/projects/week0/loading.py).  Type `python3 projects/tt0menu.py` to run the week's project.

### [menu.py](https://github.com/CalrethonOfMirkwood/tri3CSPPortfolio/tree/master/projects/tt0menu.py)
```
import time
from loading import loading

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
```

### [loading.py](https://github.com/CalrethonOfMirkwood/tri3CSPPortfolio/tree/master/projects/loading.py)
```
import time
import os

textpic = ["",
           "  ⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝ ",
           " ⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇ ",
           "⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏ ",
           "⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀",
           "⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀",
           "⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀",
           "⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀",
           "⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀",
           "⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
           "⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
           "⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
           "⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
           "⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀"]

def loading():
    for i in range(30):
        os.system("clear")
        for str in textpic:
            print(' '*(30-i)+str)
        print("    <------------------------------mega man loading")
        time.sleep(0.1)
```
