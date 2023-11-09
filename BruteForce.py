import itertools #importing all the modules
import string
import sys

alpha = string.printable #set alpha equal too all the printible a


password = input("What is the target? ")

max_length = int(input("What is the max legnth you want to brute force? ")) #asking for the max length of the brute force try

counter = 0 #counter for how manay tries it takes

for length in range(1, max_length + 1): #tries all lengths from 1 to max
    for comb in itertools.product(alpha, repeat=length): #tries all the combinations of the ascii letters
        target = "".join(comb)
        counter += 1
        if target == password: #compare guess to the password
            print("Password found: " + target + " took " + str(counter) + " tries")
            sys.exit() #when password is found kill the program
