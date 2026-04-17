# Caesar Cipher Program - Bug #3 FIXED

# Double the given alphabet
def getDoubleAlphabet(alphabet):
    return alphabet + alphabet

# Get a message to encrypt
def getMessage():
    return input("Please enter a message to encrypt: ")

# Get a cipher key
def getCipherKey():
    return input("Please enter a key (whole number from 1-25): ")

# Encrypt message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        
        if currentCharacter in alphabet:
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter
    
    return encryptedMessage

# Decrypt message (FIX DI SINI)
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Main program logic
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    
    myMessage = getMessage()
    print(myMessage)
    
    myCipherKey = getCipherKey()
    print(myCipherKey)
    
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

# Main logic
runCaesarCipherProgram()