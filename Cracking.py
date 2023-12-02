import itertools #importing all the modules
import string
import sys
import hashlib
import bcrypt

alpha = string.printable #set alpha equal too all the printible a


choice = int(input("\n\n*******MENU*******\n\n1.Plaintext\n2.Encrpyted\nWhat mode: "))

if choice == 2:
    encryptMode = int(input("1.MD5\n2.SHA-256\n3.BCrypt\nWhat encrpytion cracking mode: "))
    
method = int(input("1.BruteForce\n2.Dictionary\nWhat method: "))

password = str(input("What is the target? "))
       
if (choice == 1):
    if (method == 1):

        max_length = int(input("What is the max length you want to brute force? ")) #asking for the max length of the brute force try

        counter = 0 #counter for how many tries it takes

        for length in range(1, max_length + 1): #tries all lengths from 1 to max
            for comb in itertools.product(alpha, repeat=length): #tries all the combinations of the ascii letters
                target = "".join(comb)
                counter += 1
                if (target == password): #compare guess to the password
                    print("Password found: " + target + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program
    if (method == 2):
        counter = 0 #counter for how many tries it takes
        passList = open("passList.txt", "r").read() #read file
        pList = passList.splitlines() #create a list of passwords
        for p in pList: #itterates over the passwords
            counter += 1
            if (p == password): #compare guess to the password
                print("Password found: " + p + " took " + str(counter) + " tries")
                sys.exit() #when password is found kill the program
            elif (counter == 10000):
                print ("Password wasn't found in dictionary :(")
                
if (choice == 2):
    if (method == 1):
        if (encryptMode == 1): #md5

            counter = 0 #counter for how many tries it takes

            for length in range(1, 999): #tries all lengths from 1 to max
                for comb in itertools.product(alpha, repeat=length): #tries all the combinations of the ascii letters
                    target = "".join(comb)
                    hashedTarget = hashlib.md5(target.encode('utf-8')).hexdigest() #hashes target with MD5
                    counter += 1
                    if (hashedTarget == password): #compare guess hash with actual hash
                        print("Password found: " + target + " took " + str(counter) + " tries")
                        sys.exit() #when password is found kill the program
                        
        if (encryptMode == 2): #sha256

            counter = 0 #counter for how many tries it takes

            for length in range(1, 999): #tries all lengths from 1 to max
                for comb in itertools.product(alpha, repeat=length): #tries all the combinations of the ascii letters
                    target = "".join(comb)
                    hashedTarget = hashlib.sha256(target.encode('utf-8')).hexdigest() #hashes target with MD5
                    counter += 1
                    if (hashedTarget == password): #compare guess hash with actual hash
                        print("Password found: " + target + " took " + str(counter) + " tries")
                        sys.exit() #when password is found kill the program
        
