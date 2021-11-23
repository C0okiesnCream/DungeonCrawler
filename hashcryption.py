#Hashing algorithm
def hash(password,hashlength):    
    #variables
    salt = 0
    hPass = []
    hPass2 = []
    hashedPassword = 0
    dummy = 0
    dummy2 = 0
    dummy3 = 0

    while dummy < len(password):
        hPass.append(password[dummy])
        dummy += 1

    #hashing
    dummy = 0
    while dummy2 < 5:
        while dummy < len(hPass):
            if hPass[dummy] == "a":
                hPass[dummy] = "lO"
            elif hPass[dummy] == "b":
                hPass[dummy] = "9oi"
            elif hPass[dummy] == "c":
                hPass[dummy] = "qr1"
            elif hPass[dummy] == "d":
                hPass[dummy] = "F0"
            elif hPass[dummy] == "e":
                hPass[dummy] = "91"
            elif hPass[dummy] == "f":
                hPass[dummy] = "K93"
            elif hPass[dummy] == "g":
                hPass[dummy] = "gdrH"
            elif hPass[dummy] == "h":
                hPass[dummy] = "uu"
            elif hPass[dummy] == "i":
                hPass[dummy] = "20B"
            elif hPass[dummy] == "j":
                hPass[dummy] = "Luts"
            elif hPass[dummy] == "k":
                hPass[dummy] = "JJU"
            elif hPass[dummy] == "l":
                hPass[dummy] = "0CK"
            elif hPass[dummy] == "m":
                hPass[dummy] = "P4"
            elif hPass[dummy] == "n":
                hPass[dummy] = "0"
            elif hPass[dummy] == "o":
                hPass[dummy] = "J8"
            elif hPass[dummy] == "p":
                hPass[dummy] = "CxZ"
            elif hPass[dummy] == "q":
                hPass[dummy] = "P8"
            elif hPass[dummy] == "r":
                hPass[dummy] = "981"
            elif hPass[dummy] == "s":
                hPass[dummy] = "pSm"
            elif hPass[dummy] == "t":
                hPass[dummy] = "n5"
            elif hPass[dummy] == "u":
                hPass[dummy] = "lL"
            elif hPass[dummy] == "v":
                hPass[dummy] = "V4"
            elif hPass[dummy] == "w":
                hPass[dummy] = "Gny"
            elif hPass[dummy] == "x":
                hPass[dummy] = "1"
            elif hPass[dummy] == "y":
                hPass[dummy] = "27"
            elif hPass[dummy] == "z":
                hPass[dummy] = "plK"
            elif hPass[dummy] == "A":
                hPass[dummy] = "76l"
            elif hPass[dummy] == "B":
                hPass[dummy] = "NlT"
            elif hPass[dummy] == "C":
                hPass[dummy] = "py"
            elif hPass[dummy] == "D":
                hPass[dummy] = "i"
            elif hPass[dummy] == "E":
                hPass[dummy] = "lU"
            elif hPass[dummy] == "F":
                hPass[dummy] = "O"
            elif hPass[dummy] == "G":
                hPass[dummy] = "61"
            elif hPass[dummy] == "H":
                hPass[dummy] = "I7"
            elif hPass[dummy] == "I":
                hPass[dummy] = "JJ"
            elif hPass[dummy] == "J":
                hPass[dummy] = "oqC"
            elif hPass[dummy] == "K":
                hPass[dummy] = "Ohm"
            elif hPass[dummy] == "L":
                hPass[dummy] = "df"
            elif hPass[dummy] == "M":
                hPass[dummy] = "pO"
            elif hPass[dummy] == "N":
                hPass[dummy] = "ZxSa"
            elif hPass[dummy] == "O":
                hPass[dummy] = "1L9"
            elif hPass[dummy] == "P":
                hPass[dummy] = "li1"
            elif hPass[dummy] == "Q":
                hPass[dummy] = "496"
            elif hPass[dummy] == "R":
                hPass[dummy] = "u"
            elif hPass[dummy] == "S":
                hPass[dummy] = "87"
            elif hPass[dummy] == "T":
                hPass[dummy] = "877"
            elif hPass[dummy] == "U":
                hPass[dummy] = "P9"
            elif hPass[dummy] == "V":
                hPass[dummy] = "lF"
            elif hPass[dummy] == "W":
                hPass[dummy] = "rR"
            elif hPass[dummy] == "X":
                hPass[dummy] = "xZ"
            elif hPass[dummy] == "Y":
                hPass[dummy] = "vRtg"
            elif hPass[dummy] == "Z":
                hPass[dummy] = "oOo"
            elif hPass[dummy] == "0":
                hPass[dummy] = "op"
            elif hPass[dummy] == "1":
                hPass[dummy] = "3rT"
            elif hPass[dummy] == "2":
                hPass[dummy] = "i"
            elif hPass[dummy] == "3":
                hPass[dummy] = "90"
            elif hPass[dummy] == "4":
                hPass[dummy] = "llo"
            elif hPass[dummy] == "5":
                hPass[dummy] = "rDJ"
            elif hPass[dummy] == "6":
                hPass[dummy] = "D3v11"
            elif hPass[dummy] == "7":
                hPass[dummy] = "aH"
            elif hPass[dummy] == "8":
                hPass[dummy] = "mbS"
            elif hPass[dummy] == "9":
                hPass[dummy] = "vsK"
            elif hPass[dummy] == "!":
                hPass[dummy] = "9i"
            elif hPass[dummy] == "@":
                hPass[dummy] = "ojG"
            elif hPass[dummy] == "#":
                hPass[dummy] = "0"
            elif hPass[dummy] == "$":
                hPass[dummy] = "klI"
            elif hPass[dummy] == "%":
                hPass[dummy] = "Pof"
            elif hPass[dummy] == "?":
                hPass[dummy] = "opNg"
            else:
                hPass[dummy] = "lrt"
            dummy += 1
        dummy3 = ""
        hPass2 = (dummy3.join(hPass))
        while dummy < len(hPass2):
            hPass.append(hPass2[dummy])
            dummy += 1
        dummy2 += 1
    #putting characters from the back onto the front 
    dummy = 1
    while dummy < 11:
        hPass.insert(0,hPass[-dummy])
        dummy += 1

    #turning array into string
    dummy = ""
    hashedPassword = (dummy.join(hPass))
    hashedPassword = hashedPassword[:hashlength]
    return(hashedPassword)

#encryption
def encrypt(message):
    dummy = 0
    dummy2 = []
    encryptedM = 0

    while dummy < len(message):
        dummy2.append(message[dummy])
        dummy += 1
    message = dummy2

    dummy2 = 0    
    dummy = 0
    while dummy < len(message):
        if message[dummy] == "a":
            message[dummy] = "08"
        elif message[dummy] == "b":
            message[dummy] = "97"
        elif message[dummy] == "c":
            message[dummy] = "85"
        elif message[dummy] == "d":
            message[dummy] = "45"
        elif message[dummy] == "e":
            message[dummy] = "32"
        elif message[dummy] == "f":
            message[dummy] = "06"
        elif message[dummy] == "g":
            message[dummy] = "88"
        elif message[dummy] == "h":
            message[dummy] = "27"
        elif message[dummy] == "i":
            message[dummy] = "34"
        elif message[dummy] == "j":
            message[dummy] = "76"
        elif message[dummy] == "k":
            message[dummy] = "43"
        elif message[dummy] == "l":
            message[dummy] = "11"
        elif message[dummy] == "m":
            message[dummy] = "20"
        elif message[dummy] == "n":
            message[dummy] = "01"
        elif message[dummy] == "o":
            message[dummy] = "83"
        elif message[dummy] == "p":
            message[dummy] = "90"
        elif message[dummy] == "q":
            message[dummy] = "51"
        elif message[dummy] == "r":
            message[dummy] = "33"
        elif message[dummy] == "s":
            message[dummy] = "98"
        elif message[dummy] == "t":
            message[dummy] = "57"
        elif message[dummy] == "u":
            message[dummy] = "75"
        elif message[dummy] == "v":
            message[dummy] = "77"
        elif message[dummy] == "w":
            message[dummy] = "44"
        elif message[dummy] == "x":
            message[dummy] = "48"
        elif message[dummy] == "y":
            message[dummy] = "32"
        elif message[dummy] == "z":
            message[dummy] = "21"
        elif message[dummy] == "A":
            message[dummy] = "04"
        elif message[dummy] == "B":
            message[dummy] = "65"
        elif message[dummy] == "C":
            message[dummy] = "64"
        elif message[dummy] == "D":
            message[dummy] = "63"
        elif message[dummy] == "E":
            message[dummy] = "72"
        elif message[dummy] == "F":
            message[dummy] = "13"
        elif message[dummy] == "G":
            message[dummy] = "56"
        elif message[dummy] == "H":
            message[dummy] = "39"
        elif message[dummy] == "I":
            message[dummy] = "29"
        elif message[dummy] == "J":
            message[dummy] = "42"
        elif message[dummy] == "K":
            message[dummy] = "86"
        elif message[dummy] == "L":
            message[dummy] = "54"
        elif message[dummy] == "M":
            message[dummy] = "14"
        elif message[dummy] == "N":
            message[dummy] = "12"
        elif message[dummy] == "O":
            message[dummy] = "69"
        elif message[dummy] == "P":
            message[dummy] = "60"
        elif message[dummy] == "Q":
            message[dummy] = "04"
        elif message[dummy] == "R":
            message[dummy] = "82"
        elif message[dummy] == "S":
            message[dummy] = "37"
        elif message[dummy] == "T":
            message[dummy] = "68"
        elif message[dummy] == "U":
            message[dummy] = "19"
        elif message[dummy] == "V":
            message[dummy] = "18"
        elif message[dummy] == "W":
            message[dummy] = "17"
        elif message[dummy] == "X":
            message[dummy] = "16"
        elif message[dummy] == "Y":
            message[dummy] = "15"
        elif message[dummy] == "Z":
            message[dummy] = "53"
        elif message[dummy] == "0":
            message[dummy] = "57"
        elif message[dummy] == "1":
            message[dummy] = "51"
        elif message[dummy] == "2":
            message[dummy] = "10"
        elif message[dummy] == "3":
            message[dummy] = "40"
        elif message[dummy] == "4":
            message[dummy] = "49"
        elif message[dummy] == "5":
            message[dummy] = "58"
        elif message[dummy] == "6":
            message[dummy] = "21"
        elif message[dummy] == "7":
            message[dummy] = "20"
        elif message[dummy] == "8":
            message[dummy] = "40"
        elif message[dummy] == "9":
            message[dummy] = "78"
        elif message[dummy] == "!":
            message[dummy] = "32"
        elif message[dummy] == "@":
            message[dummy] = "08"
        elif message[dummy] == "#":
            message[dummy] = "09"
        elif message[dummy] == "$":
            message[dummy] = "89"
        elif message[dummy] == "%":
            message[dummy] = "39"
        elif message[dummy] == "?":
            message[dummy] = "71"
        else:
            message[dummy] = "00"
        dummy += 1
    print(message)
    dummy2 = ""
    encryptedM = (dummy2.join(message))
    return(encryptedM)
    
#decryption
def decrept(message):
    pass
