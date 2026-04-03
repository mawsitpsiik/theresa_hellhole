def encrypt(message, shift):
    newmessage = ""
    howLong = len(message)
    for x in range(howLong): 
        if (97 <= ord(message[x])) and (ord(message[x]) <= 122): #LOWERCASE
            pos = ord(message[x]) - ord("a")
            newpos = (pos + shift) % 26
            addChar = chr(newpos + ord("a"))
            newmessage = newmessage + addChar
        elif (65 <= ord(message[x])) and (ord(message[x]) <= 90): #uppercase
            pos = ord(message[x]) - ord("A")
            newpos = (pos + shift) % 26
            addChar = chr(newpos + ord("A"))
            newmessage = newmessage + addChar
        else: #if it's not the latin alphabet, it goes in the string like normal
            addChar = message[x]
            newmessage = newmessage + addChar

    finalMsg = str(newmessage)
    return finalMsg
rdyToPrint = encrypt("Hello, World!", 3) 
print(rdyToPrint)