# PasswordCrack
## 2023 CLHS Cybersecurity
## Rubric (51/51)
- [x] Usage of GitHub (3)
- [x] Load 10,000 most common passwords (4)
- [x] Brute force cracking (10)
- [x] Dictionary cracking (10)
- [x] Can run via command line with arguments (4)
- [x] MD5 hashed passwords can be checked (5)
- [x] SHA-256 hashed passwords can be checked (5)
- [x] BCrypt hashed passwords can be checked (5)
- [x] Includes README.md (1)
## Command Line Arguments
### Method
        -b = brute force 

        -d = dictionary attack

### Mode
        -p = crack plaintext 

        -e = crack encrypted

### Hash Method (only used if mode is set to -e)
        -m = MD5
        
        -s = SHA256
        
        -b = bcrypt

## Formating
`python3 Cracking.py {password} {method} {mode} {hashMethod}`
`python3 Cracking.py 81dc9bdb52d04dc20036dbd8313ed055 -b -e -m `
`python3 Cracking.py 1234 -d -p`
## Dependencies:
`itertools`
`string`
`sys`
`hashlib`
`bcrypt`

## Discalimer
        I used Anaconda Spyder to run this program. Between IDEs I'm unsure if bcrypt works as intended.
