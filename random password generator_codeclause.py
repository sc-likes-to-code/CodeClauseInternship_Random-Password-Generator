import string
import random

#The program starts:
print("\n                        **********Password Generator**********\n")

#Taking input of desired length of the randomly generated password from the user:
l = int(input("Enter desired length of password: "))

#Displaying the options available to the user- which types of characters are to be used for creating the password(thereby allowing the user to choose the password complexity):
print('''\nChoose character set for password from these or choose to exit by entering '4' : \n1. Letters\n2. Digits\n3. Special characters\n4. Exit\n''')

#Declaring an empty string variable, later used to store all the different types of characters available to the user to choose from:
cl = ""

#A while loop used to store all the available characters into the string variable cl
while(True):
    c = int(input("Pick a number: "))
    
    if(c == 1):
        cl += string.ascii_letters
    elif(c == 2):
        cl += string.digits
    elif(c == 3):
        cl += string.punctuation
    elif(c == 4):
        break
    else:
        print("Please pick a valid option!")

#List later used to store the randomly generated password:
p = []

#A for loop used to store randomly the characters from the character set cl:
for i in range(l):
    randomchar = random.choice(cl)
    p.append(randomchar)

#Printing the desired output:
print("The random password is " + "".join(p))
print("\n                                        ******************")
