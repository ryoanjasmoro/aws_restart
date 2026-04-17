#!/usr/bin/env python3
# coding: utf-8

# Function: double alphabet
def getDoubleAlphabet(alphabet):
    return alphabet + alphabet

# Function: input message
def getMessage():
    return input("Please enter a message to encrypt: ")

# Function: input key
def getCipherKey():
    return input("Please enter a key (1-25): ")

# Function: encrypt
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    message = message.upper()

    for char in message:
        if char in alphabet:
            position = alphabet.find(char)
            newPosition = position + int(cipherKey)
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += char

    return encryptedMessage

# Function: decrypt
def decryptMessage(message, cipherKey, alphabet):
    return encryptMessage(message, -int(cipherKey), alphabet)

# Main function
def runCaesarCipherProgram():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    doubleAlphabet = getDoubleAlphabet(alphabet)

    message = getMessage()
    key = getCipherKey()

    encrypted = encryptMessage(message, key, doubleAlphabet)
    print("Encrypted:", encrypted)

    decrypted = decryptMessage(encrypted, key, doubleAlphabet)
    print("Decrypted:", decrypted)

# WAJIB: panggil function
runCaesarCipherProgram()