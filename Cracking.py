import itertools #importing all the modules
import string
import sys
import hashlib
import bcrypt

try: #catching arguements from the console
    argTrue = False
    password = str(sys.argv[1])
    
    methodArg = str(sys.argv[2])
    if (methodArg != "-b" and methodArg != "-d"): #raise exception if outside of param
        print ("hi")
        raise Exception
    elif(methodArg == "-b"):
        method = 1
    else:
        method = 2
        
    choiceArg = str(sys.argv[3])
    if (choiceArg != "-p" and choiceArg != "-e"):#raise exception if outside of param
        raise Exception
    elif(choiceArg == "-p"):
        choice = 1
    else:
        choice = 2
       
    if (choiceArg == "-e"): #ask for encryptMode if user selects enryption
        encryptModeArg = str(sys.argv[4])
        if (encryptModeArg != "-m" and encryptModeArg != "-s" and encryptModeArg != "-b"):#raise exception if outside of param
            raise Exception
        elif(encryptModeArg == "-m"):
            encryptMode = 1
        elif (encryptModeArg == "-s"):
            encryptMode = 2
        else:
            encryptMode = 3
        
        
    argTrue = True
except:
    print("Looks like your arguements were bad. ")
    end = int(input("1.Yes\n2.No\nWould you like to continue without commandline arguements? "))
    if (end == 2):
        print("Try again")
        sys.exit()

alpha = string.printable #set alpha equal too all the printible a

if (not argTrue):
    choice = int(input("\n\n*******MENU*******\n\n1.Plaintext\n2.Encrpyted\nWhat mode: "))

    if choice == 2:
        encryptMode = int(input("1.MD5\n2.SHA-256\n3.BCrypt (very slow)\nWhat encrpytion cracking mode: "))
    
    method = int(input("1.BruteForce\n2.Dictionary\nWhat method: "))

    password = str(input("What is the target? "))
       
if (choice == 1): #plaintext cracking
    if (method == 1): #bruteforce

        max_length = int(input("What is the max length you want to brute force? ")) #asking for the max length of the brute force try

        counter = 0 #counter for how many tries it takes

        for length in range(1, max_length + 1): #tries all lengths from 1 to max
            for comb in itertools.product(alpha, repeat=length): #tries all the combinations of the ascii letters
                target = "".join(comb)
                counter += 1
                if (target == password): #compare guess to the password
                    print("Password found: " + target + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program
                    
    if (method == 2): #dictionary
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
                
if (choice == 2): #hash cracking
    if (method == 1): #bruteforce
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
                        
        elif (encryptMode == 2): #sha256

            counter = 0 #counter for how many tries it takes

            for length in range(1, 999): #tries all lengths from 1 to max
                for comb in itertools.product(alpha, repeat=length): #tries all the combinations of the ascii letters
                    target = "".join(comb)
                    hashedTarget = hashlib.sha256(target.encode('utf-8')).hexdigest() #hashes target with sah256
                    counter += 1
                    if (hashedTarget == password): #compare guess hash with actual hash
                        print("Password found: " + target + " took " + str(counter) + " tries")
                        sys.exit() #when password is found kill the program
            
        elif (encryptMode == 3): #bcrypt

            counter = 0 #counter for how many tries it takes

            for length in range(1, 999): #tries all lengths from 1 to max
                for comb in itertools.product(alpha, repeat=length): #tries all the combinations of the ascii letters
                    target = "".join(comb)
                    encodeTarget = target.encode('utf-8') 
                    counter += 1
                    if (bcrypt.checkpw(encodeTarget, password.encode('utf-8'))): #compare guess to the hash using bcrypt 
                        print("Password found: " + target + " took " + str(counter) + " tries")
                        sys.exit() #when password is found kill the program
                        
    if (method == 2): #dictionary
        
        if (encryptMode == 1): #md5
            counter = 0 #counter for how many tries it takes
            passList = open("passList.txt", "r").read() #read file
            pList = passList.splitlines() #create a list of passwords
            for p in pList: #itterates over the passwords
                counter += 1
                hashedp = hashlib.md5(p.encode('utf-8')).hexdigest() #hashes target with MD5
                if (hashedp == password): #compare guess to the password
                    print("Password found: " + p + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program
                elif (counter == 10000):
                    print ("Password wasn't found in dictionary :(")
                
        elif (encryptMode == 2): #sha256
            counter = 0 #counter for how many tries it takes
            passList = open("passList.txt", "r").read() #read file
            pList = passList.splitlines() #create a list of passwords
            for p in pList: #itterates over the passwords
                counter += 1
                hashedp = hashlib.sha256(p.encode('utf-8')).hexdigest() #hashes target with sha256
                if (hashedp == password): #compare guess to the password
                    print("Password found: " + p + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program
                elif (counter == 10000):
                    print ("Password wasn't found in dictionary :(")
                    
        elif (encryptMode == 3): #bcrypt
            counter = 0 #counter for how many tries it takes
            passList = open("passList.txt", "r").read() #read file
            pList = passList.splitlines() #create a list of passwords
            for p in pList: #itterates over the passwords
                counter += 1
                encodep = p.encode('utf-8') 
                if (bcrypt.checkpw(encodep, password.encode('utf-8'))): #compare guess to the hash using bcrypt
                    print("Password found: " + p + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program
                elif (counter == 10000):
                    print ("Password wasn't found in dictionary :(")
