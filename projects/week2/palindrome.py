# week 2 palindrome

class palindrome:
    string = ""
    def __init__(self, s):
        self.string = s
    def ispalindrome(self):
        for i in range(0, int(len(self.string)/2)):
            if self.string[i] != self.string[len(self.string)-i-1]:
                return False
        return True

# function called by menu.py
def palindromefunction():
    string = str(input("Input string to test if palindrome: "))
    stringChecker = palindrome(string)
    result = stringChecker.ispalindrome()
    if (result):
        print("%s is a palindrome"%(string))
    else:
        print("%s is not a palindrome"%(string))