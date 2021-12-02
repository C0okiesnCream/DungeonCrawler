#Hashing algorithm
def hash(password,hashlength):    
    #variables
    salt = 0
    hPass = []
    hPass2 = []
    hashedPassword = 0
    D = 0
    D2 = 0
    D3 = 0

    while D < len(password):
        hPass.append(password[D])
        D += 1

    #hashing
    D = 0
    while D2 < 5:
        while D < len(hPass):
            if hPass[D] == "a":
                hPass[D] = "lO"
            elif hPass[D] == "b":
                hPass[D] = "9oi"
            elif hPass[D] == "c":
                hPass[D] = "qr1"
            elif hPass[D] == "d":
                hPass[D] = "F0"
            elif hPass[D] == "e":
                hPass[D] = "91"
            elif hPass[D] == "f":
                hPass[D] = "K93"
            elif hPass[D] == "g":
                hPass[D] = "gdrH"
            elif hPass[D] == "h":
                hPass[D] = "uu"
            elif hPass[D] == "i":
                hPass[D] = "20B"
            elif hPass[D] == "j":
                hPass[D] = "Luts"
            elif hPass[D] == "k":
                hPass[D] = "JJU"
            elif hPass[D] == "l":
                hPass[D] = "0CK"
            elif hPass[D] == "m":
                hPass[D] = "P4"
            elif hPass[D] == "n":
                hPass[D] = "0"
            elif hPass[D] == "o":
                hPass[D] = "J8"
            elif hPass[D] == "p":
                hPass[D] = "CxZ"
            elif hPass[D] == "q":
                hPass[D] = "P8"
            elif hPass[D] == "r":
                hPass[D] = "981"
            elif hPass[D] == "s":
                hPass[D] = "pSm"
            elif hPass[D] == "t":
                hPass[D] = "n5"
            elif hPass[D] == "u":
                hPass[D] = "lL"
            elif hPass[D] == "v":
                hPass[D] = "V4"
            elif hPass[D] == "w":
                hPass[D] = "Gny"
            elif hPass[D] == "x":
                hPass[D] = "1"
            elif hPass[D] == "y":
                hPass[D] = "27"
            elif hPass[D] == "z":
                hPass[D] = "plK"
            elif hPass[D] == "A":
                hPass[D] = "76l"
            elif hPass[D] == "B":
                hPass[D] = "NlT"
            elif hPass[D] == "C":
                hPass[D] = "py"
            elif hPass[D] == "D":
                hPass[D] = "i"
            elif hPass[D] == "E":
                hPass[D] = "lU"
            elif hPass[D] == "F":
                hPass[D] = "O"
            elif hPass[D] == "G":
                hPass[D] = "61"
            elif hPass[D] == "H":
                hPass[D] = "I7"
            elif hPass[D] == "I":
                hPass[D] = "JJ"
            elif hPass[D] == "J":
                hPass[D] = "oqC"
            elif hPass[D] == "K":
                hPass[D] = "Ohm"
            elif hPass[D] == "L":
                hPass[D] = "df"
            elif hPass[D] == "M":
                hPass[D] = "pO"
            elif hPass[D] == "N":
                hPass[D] = "ZxSa"
            elif hPass[D] == "O":
                hPass[D] = "1L9"
            elif hPass[D] == "P":
                hPass[D] = "li1"
            elif hPass[D] == "Q":
                hPass[D] = "496"
            elif hPass[D] == "R":
                hPass[D] = "u"
            elif hPass[D] == "S":
                hPass[D] = "87"
            elif hPass[D] == "T":
                hPass[D] = "877"
            elif hPass[D] == "U":
                hPass[D] = "P9"
            elif hPass[D] == "V":
                hPass[D] = "lF"
            elif hPass[D] == "W":
                hPass[D] = "rR"
            elif hPass[D] == "X":
                hPass[D] = "xZ"
            elif hPass[D] == "Y":
                hPass[D] = "vRtg"
            elif hPass[D] == "Z":
                hPass[D] = "oOo"
            elif hPass[D] == "0":
                hPass[D] = "op"
            elif hPass[D] == "1":
                hPass[D] = "3rT"
            elif hPass[D] == "2":
                hPass[D] = "i"
            elif hPass[D] == "3":
                hPass[D] = "90"
            elif hPass[D] == "4":
                hPass[D] = "llo"
            elif hPass[D] == "5":
                hPass[D] = "rDJ"
            elif hPass[D] == "6":
                hPass[D] = "D3v11"
            elif hPass[D] == "7":
                hPass[D] = "aH"
            elif hPass[D] == "8":
                hPass[D] = "mbS"
            elif hPass[D] == "9":
                hPass[D] = "vsK"
            elif hPass[D] == "!":
                hPass[D] = "9i"
            elif hPass[D] == "@":
                hPass[D] = "ojG"
            elif hPass[D] == "#":
                hPass[D] = "0"
            elif hPass[D] == "$":
                hPass[D] = "klI"
            elif hPass[D] == "%":
                hPass[D] = "Pof"
            elif hPass[D] == "?":
                hPass[D] = "opNg"
            else:
                hPass[D] = "lrt"
            D += 1
        D3 = ""
        hPass2 = (D3.join(hPass))
        while D < len(hPass2):
            hPass.append(hPass2[D])
            D += 1
        D2 += 1
    #putting characters from the back onto the front 
    D = 1
    while D < 11:
        hPass.insert(0,hPass[-D])
        D += 1

    #turning array into string
    D = ""
    hashedPassword = (D.join(hPass))
    hashedPassword = hashedPassword[:hashlength]
    return(hashedPassword)

#encryption
def encrypt(message,keySpacer):
    import random
    D = 0
    D2 = []
    D3 = 0
    D4 = []
    D5 = 0
    D6 = 0
    encryptedM = 0
    key = 0
    errorCheck = message.isspace()
    messLength = len(message)
    if len(message) < 1 or errorCheck == True:
        encryptedM = "message was blank"
        key = "the message was a lie"
        D5 = [encryptedM, key]
        return D5
    else:

        while D < len(message):
            D2.append(message[D])
            D += 1
        message = D2

        D2 = 0    
        D = 0
        32
        while D < len(message):
            if message[D] == "a":
                message[D] = "01"
            elif message[D] == "b":
                message[D] = "02"
            elif message[D] == "c":
                message[D] = "03"
            elif message[D] == "d":
                message[D] = "04"
            elif message[D] == "e":
                message[D] = "05"
            elif message[D] == "f":
                message[D] = "06"
            elif message[D] == "g":
                message[D] = "07"
            elif message[D] == "h":
                message[D] = "08"
            elif message[D] == "i":
                message[D] = "09"
            elif message[D] == "j":
                message[D] = "10"
            elif message[D] == "k":
                message[D] = "11"
            elif message[D] == "l":
                message[D] = "12"
            elif message[D] == "m":
                message[D] = "13"
            elif message[D] == "n":
                message[D] = "14"
            elif message[D] == "o":
                message[D] = "15"
            elif message[D] == "p":
                message[D] = "16"
            elif message[D] == "q":
                message[D] = "17"
            elif message[D] == "r":
                message[D] = "18"
            elif message[D] == "s":
                message[D] = "19"
            elif message[D] == "t":
                message[D] = "20"
            elif message[D] == "u":
                message[D] = "21"
            elif message[D] == "v":
                message[D] = "22"
            elif message[D] == "w":
                message[D] = "23"
            elif message[D] == "x":
                message[D] = "24"
            elif message[D] == "y":
                message[D] = "25"
            elif message[D] == "z":
                message[D] = "26"
            elif message[D] == "A":
                message[D] = "27"
            elif message[D] == "B":
                message[D] = "28"
            elif message[D] == "C":
                message[D] = "29"
            elif message[D] == "D":
                message[D] = "30"
            elif message[D] == "E":
                message[D] = "31"
            elif message[D] == "F":
                message[D] = "32"
            elif message[D] == "G":
                message[D] = "33"
            elif message[D] == "H":
                message[D] = "34"
            elif message[D] == "I":
                message[D] = "35"
            elif message[D] == "J":
                message[D] = "36"
            elif message[D] == "K":
                message[D] = "37"
            elif message[D] == "L":
                message[D] = "38"
            elif message[D] == "M":
                message[D] = "39"
            elif message[D] == "N":
                message[D] = "40"
            elif message[D] == "O":
                message[D] = "41"
            elif message[D] == "P":
                message[D] = "42"
            elif message[D] == "Q":
                message[D] = "43"
            elif message[D] == "R":
                message[D] = "44"
            elif message[D] == "S":
                message[D] = "45"
            elif message[D] == "T":
                message[D] = "46"
            elif message[D] == "U":
                message[D] = "47"
            elif message[D] == "V":
                message[D] = "48"
            elif message[D] == "W":
                message[D] = "49"
            elif message[D] == "X":
                message[D] = "50"
            elif message[D] == "Y":
                message[D] = "51"
            elif message[D] == "Z":
                message[D] = "52"
            elif message[D] == "0":
                message[D] = "53"
            elif message[D] == "1":
                message[D] = "54"
            elif message[D] == "2":
                message[D] = "55"
            elif message[D] == "3":
                message[D] = "56"
            elif message[D] == "4":
                message[D] = "57"
            elif message[D] == "5":
                message[D] = "58"
            elif message[D] == "6":
                message[D] = "59"
            elif message[D] == "7":
                message[D] = "60"
            elif message[D] == "8":
                message[D] = "61"
            elif message[D] == "9":
                message[D] = "62"
            elif message[D] == "!":
                message[D] = "63"
            elif message[D] == "@":
                message[D] = "64"
            elif message[D] == "#":
                message[D] = "65"
            elif message[D] == "$":
                message[D] = "67"
            elif message[D] == "%":
                message[D] = "68"
            elif message[D] == "?":
                message[D] = "69"
            else:
                message[D] = "00"
            D += 1
        D2 = ""
        #turning array into string
        encryptedM = (D2.join(message))
        D2 = []
        messLength
        D3 = 0
        #creating first section of key
        while D3 < messLength:
            D = random.randint(1, 9)
            D2.append(str(D))
            D3 += 1
        D = ""
        try:
            D2 = (D.join(D2))
        except:
            D2 = D2[0]
        try:
            D2 = int(D2)
        except:
            D2 = "an error occured due to your entry being blank"
        D3 = 0
        encryptedM = int(encryptedM)
        #adding operations to string
        while D3 < 3:
            D = random.randint(1, 3)
            if D == 1:
                D = "A"
                D4.append(D)
                encryptedM += D2
            elif D == 2:
                D = "S"
                D4.append(D)
                encryptedM -= D2
            else:
                D = "M"
                D4.append(D)
                encryptedM *= D2

            D3 += 1
        D = ""
        D4 = (D.join(D4))
        key = (str(D2) + keySpacer + str(D4) + keySpacer)
        encryptedM = hex(encryptedM)
        D5 = [key,encryptedM]
            
        return(D5)
    
#decryption
def decrept(message):
    pass
