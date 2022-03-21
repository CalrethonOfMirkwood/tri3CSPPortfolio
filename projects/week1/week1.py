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
