#Avneet Sidhu
#Student Number: 
#CPS109 

# Problem: I wanted to make a program that encrypts given text, so I can encrypt my passwords and messages.  

# this is an application that allows the user to encode and decode text using the Caeser Shift 
# and Vigenere Square Ciphers, the application runs until the user ends the program. 
# the user is given a series of prompts, to first enter the string, then to encrypt or decrypt
# followed by the type of cipher to encrypt or decrypt with. The user can encrypt a string multiple times
# using different combinations of the 2 ciphers with different keys. The output file provided shows the encryption
# of the string "hello world" first done with the caeser cipher using a key of 5 then the decryption of the 
# encrypted string, followed by another encryption of "hello world" using the key word "lemon" and lastly 
# the decryption of this encrypted string. Recently, I used this program to further secure my passwords so they 
# are different for different websites. 


outputFileList = []

outputFile = open('output.txt', 'w')

alphabet = "abcdefghijklmnopqrstuvwxyz" 

alphabetList = list(alphabet) #turns the alphabet into a list 

def caeserEncoder(sentence,key): #function that encrypts the given string using Caeser Shift with the desired key
    encoded = [] #list that will hold the encrypted characters of the string 
    for letter in sentence: #loops through the provided text's letters
        if letter not in alphabetList: #if the chracter is a symbol, space or number it is not encrypted, if the character is not a letter it is appended to the encoded list
            encoded.append(letter) 
        else: #if the character is a letter its position in the alphabet is found and shifted, the letter at the new position is appended to the  encoded list
            alphaPosition = alphabetList.index(letter) 
            alphaPosition += key 
            if alphaPosition > 25 :
                alphaPosition = alphaPosition - 26 
            encoded.append(alphabetList[alphaPosition]) 
    return "".join(encoded) #returns the list of encoded characters joined as a string

def caeserDecoder(sentence,key): #decrypt a string that is encoded using the caeser shift using a key provided by the user 
    decoded = [] #list that will hold the decoded string's letters
    for letter in sentence: #loops through the letters of the encoded string
        if letter not in alphabetList: #if the character is not a letter it is appended to the decoded list
            decoded.append(letter) 
        else: #if the letter is a part of the alphabet its position is found and shifted back, and the letter at the new position is appended to the decoded list  
            alphaPosition = alphabetList.index(letter)
            alphaPosition -= key 
            if alphaPosition < 0 :
                alphaPosition = alphaPosition + 26
            decoded.append(alphabetList[alphaPosition])
    return "".join(decoded)

def vigenereEncoder(sentence,key): #encrypt a given string using the Vignere Square Cipher using the desired key 
    spacesIndex=[] # list that will hold the positions of the spaces in the given text, if there are any
    if " " in sentence: #if there is a space in the text, the text is looped through and its positions are found and saved
        for x, char in enumerate (sentence):
            if char == " ":
                spacesIndex.append(x)
    sentence = sentence.replace(" ","") #the spaces are removed from the sentence 
    keystream = (len(sentence) // len(key)) * key + key[0:len(sentence) % len(key)] #a keystream used to to encode the string is formed, using the key provided by the user.
    encoded = [] #list that will hold the encoded characters of the string 
    for i, letter  in enumerate (keystream): #loops through the keystream's characters
        row = alphabet[alphabet.index(letter):len(alphabet)] + alphabet[0:alphabet.index(letter)] #this line creates the corresponding row on the Vignere Square to the letter of the keystream
        encoded += row[alphabet.index(sentence[i])] #the encoded character found from the row is appended to the encoded list 
    encoded = "".join(encoded)
    for item in spacesIndex: #the spaces that existed in the string before encryption are added to the string again 
        encoded = encoded[:item:] + " " + encoded[item:]
    return encoded #the encoded string is returned 

def vigenereDecoder(sentence,key): #decrypt a given string that was encoded using the Vignere Square Cipher using a key provided by the user 
    spacesIndex =[] #will hold the indexes of the spaces if there are any 
    if " " in sentence:
        for x, char in enumerate (sentence): #finds and saves the indexes of the spaces 
            if char == " ":
                spacesIndex.append(x)
    sentence = sentence.replace(" ","") #removes the spaces in the string 
    keystream = (len(sentence) // len(key)) * key + key[0:len(sentence) % len(key)] #generates a keystream using the key 
    decoded = [] #will hold the decoded characters of the string
    for i, letter  in enumerate (keystream): #loops through the keystream 
        row = alphabet[alphabet.index(letter):len(alphabet)] + alphabet[0:alphabet.index(letter)] #creates the row in the vigenere square 
        decoded += alphabet[row.index(sentence[i])] #appends the decoded letter to the decoded list
    decoded = "".join(decoded)
    for item in spacesIndex: #adds the spaces if there are any back to the string 
        decoded = decoded[:item:] + " " + decoded[item:]
    return decoded

def operationSelector(operation,type,string): #function that manages what operation is executed depending on the user's selections
    if operation == 1: #if the operation type 1 is chosen then the encoding options are shown 
        print("You have chosen to encode a message:")
        if type == 1:
            print("You have selected the Caeser Cipher")
            key = int(input("Enter a key(positive integer):"))
            outputFileList.append("\nEncrypting, " + string + ", using Caeser Cipher with a key of " + str(key))
            return caeserEncoder(string,key)
        if type == 2:
            print("You have selected the Vignere Square Cipher:")
            key = input("Enter a key(word):")
            outputFileList.append("\nEncrypting, " + string + ", using Vigenere Cipher with keyword " + key)
            return vigenereEncoder(string,key)
        if type == 0:
            return  "You have cancelled the operation."
    elif operation == 2: #if encoding operation type 2 is chosen then the decoding options are shown
        print("You have chosen to decode a message:")
        if type == 1:
            print("You have selected the Caeser Cipher")
            key = int(input("Enter the key(positive integer):"))
            outputFileList.append("\nDecrypting, " + string + ", using Caeser Cipher with a key of " + str(key))
            return caeserDecoder(string, key)
        if type == 2:
            print("You have selected the Vignere Square Cipher")
            key = input("Enter the Key:")
            outputFileList.append("\nDecrypting, " + string + ", using Vigenere Cipher with keyword " + key)
            return vigenereDecoder(string, key)
        if type == 0:
            return  "You have cancelled the operation"
    else:
        print("invalid command")

run = True #variable used to run the while loop that acts as the interface 

while run == True: #while loop that allows the user to encode or decode their message 
    userString = input("enter a string(0 to end):") #asks the user for a string 
    if userString == "0":
        print("You have ended the program \n Your encryption history will outputted to a text file")
        break
    selection = int(input("1 - Encode or 2 - Decode or 0 to end:")) #asks the user if they would like to encode their string or if the string needs to be decoded, saves their response
    if selection == 0: #checks if the user has chosen to end the application
        print("You have closed the program. \n Your encryption history will outputted to a text file")
        break
    typeOfCipher = int(input("1 - Caeser or 2 - Vignere Square or 0 - Back:"))
    result = (operationSelector(selection,typeOfCipher,userString.lower())) #prints the return of the operationSelector Function which returns the encoded or decoded message
    print(result)
    outputFileList.append("\n" + "resulting string:" + result)
    print("===================================================") #prints a line to seperate different operations performed by the user
    outputFileList.append("\n ===============================================")

outputFile.writelines(outputFileList)
outputFile.close()
