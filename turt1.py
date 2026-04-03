ALPHABET          = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
#theresa's additional variables:
alphabet2 = "abcdefghijklmnopqrstuvwxyz"
newmessage = "" #test message, hopefully will replace with real message



def encrypt(message, shift):
    howLong = len(message)
    for x in range(howLong): 
        if ord(message[x]) == 32:
            addChar = chr(32)
            newmessage = newmessage + addChar
            print("SPACE")
        elif 97 <= ord(message[x]) <= 122: #LOWERCASE
            pos = ord(message[x]) - ord("a")
            newpos = (pos + shift) % 26
            addChar = chr(newpos + ord("a"))
            newmessage = newmessage + addChar
            print("lowercase")
        elif 65 <= ord(message[x]) <= 97: #uppercase
            pos = ord(message[x]) - ord("A")
            newpos = (pos + shift) % 26
            addChar = chr(newpos + ord("A"))
            newmessage = newmessage + addChar
            print("UPPERCASE")
        else:
            addChar = message[x]
            newmessage = newmessage + addChar
            print("NOT APPLICABLE")

    finalMsg = str(newmessage)
    return finalMsg





rdyToPrint = encrypt("#sforjkekfdf$ TEST MESSAGE 5686$$2a", 0) 

print(rdyToPrint)