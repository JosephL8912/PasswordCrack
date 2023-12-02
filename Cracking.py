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
        
        
def bruteForce(mode, pwd):
    counter = 0 #counter for how many tries it takes

    for length in range(1, 999): #tries all lengths from 1 to max
        for comb in itertools.product(alpha, repeat=length): #tries all the combinations of the ascii letters
            target = "".join(comb)
            counter += 1
            if (mode == 0): #plain
                if (target == pwd): #compare guess to the password
                    print("Password found: " + target + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program
            elif (mode == 1): #md5
                hashedTarget = hashlib.md5(target.encode('utf-8')).hexdigest() #hashes target with MD5
                if (hashedTarget == pwd): #compare guess hash with actual hash
                    print("Password found: " + target + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program
            elif (mode == 2): #sha256
                hashedTarget = hashlib.sha256(target.encode('utf-8')).hexdigest() #hashes target with sah256
                if (hashedTarget == pwd): #compare guess hash with actual hash
                    print("Password found: " + target + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program
            elif (mode == 3): #bcrypt
                encodeTarget = target.encode('utf-8') 
                if (bcrypt.checkpw(encodeTarget, pwd.encode('utf-8'))): #compare guess to the hash using bcrypt 
                    print("Password found: " + target + " took " + str(counter) + " tries")
                    sys.exit() #when password is found kill the program

def dictionaryAtk(mode, pwd):
    counter = 0 #counter for how many tries it takes
    passList = open("passList.txt", "r").read() #read file
    pList = passList.splitlines() #create a list of passwords
    for p in pList: #itterates over the passwords
        counter += 1
        if (mode == 0):
            if (p == pwd): #compare guess to the password
                print("Password found: " + p + " took " + str(counter) + " tries")
                sys.exit() #when password is found kill the program
        
        elif (mode == 1):
            hashedp = hashlib.md5(p.encode('utf-8')).hexdigest() #hashes target with MD5
            if (hashedp == pwd): #compare guess to the password
                print("Password found: " + p + " took " + str(counter) + " tries")
                sys.exit() #when password is found kill the program
        
        elif (mode == 2):
            hashedp = hashlib.sha256(p.encode('utf-8')).hexdigest() #hashes target with sha256
            if (hashedp == pwd): #compare guess to the password
                print("Password found: " + p + " took " + str(counter) + " tries")
                sys.exit() #when password is found kill the program
                
        elif (mode == 3):
            encodep = p.encode('utf-8') 
            if (bcrypt.checkpw(encodep, pwd.encode('utf-8'))): #compare guess to the hash using bcrypt
                print("Password found: " + p + " took " + str(counter) + " tries")
                sys.exit() #when password is found kill the program
        
        if (counter == 10000):
            print ("Password wasn't found in dictionary :(")

alpha = string.printable #set alpha equal too all the printible a

if (not argTrue):
    choice = int(input("\n\n*******MENU*******\n\n1.Plaintext\n2.Encrpyted\nWhat mode: "))

    if choice == 2:
        encryptMode = int(input("1.MD5\n2.SHA-256\n3.BCrypt (very slow)\nWhat encrpytion cracking mode: "))
    
    method = int(input("1.BruteForce\n2.Dictionary\nWhat method: "))

    password = str(input("What is the target? "))
       
if (choice == 1): #plaintext cracking
    if (method == 1): #bruteforce
        bruteForce(0,password)
        
    elif (method == 2): #dictionary
        dictionaryAtk(0, password)
                
if (choice == 2): #hash cracking
    if (method == 1): #bruteforce
        bruteForce(encryptMode,password)
                        
    if (method == 2): #dictionary
        dictionaryAtk(encryptMode,password)
