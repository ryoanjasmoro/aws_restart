# Caesar Cipher Program - Final Fixed Version

# Double the given alphabet
def getDoubleAlphabet(alphabet):
    return alphabet + alphabet

# Get a message to encrypt
def getMessage():
    return input("Please enter a message to encrypt: ")

# Get a cipher key (FIX #1: harus int)
def getCipherKey():
    return int(input("Please enter a key (whole number from 1-25): "))

# Encrypt message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    
    # FIX #2: normalisasi ke uppercase
    uppercaseMessage = message.upper()
    
    for currentCharacter in uppercaseMessage:
        if currentCharacter in alphabet:
            position = alphabet.find(currentCharacter)
            newPosition = position + cipherKey
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter
    
    return encryptedMessage

# Decrypt message
def decryptMessage(message, cipherKey, alphabet):
    # FIX #3: pakai decryptKey (bukan cipherKey)
    decryptKey = -1 * cipherKey
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
    
    # FIX #4: print variable yang benar
    print(f'Decrypted Message: {myDecryptedMessage}')

# Main logic
runCaesarCipherProgram()