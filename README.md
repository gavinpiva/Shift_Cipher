# Shift_Cipher
Python implementation of a shift cipher

Encryption-Decryption Tool

This is a simple encryption-decryption tool written in Python 3. It encrypts a message using a randomly generated key and decrypts the message using the same key.

Prerequisites
The following libraries are required to run the tool:

numpy
math
Usage
To use the tool, simply run the script and follow the prompts. The tool will first ask you to input the text you wish to encrypt. Once you enter the text, it will be encrypted using a randomly generated key and the output will be displayed on the console.

To decrypt a message, you need to have the key that was used to encrypt it. You can input the encrypted message and the key as arguments to the decrypt() function. The decrypted message will be displayed on the console.

Functions
The tool includes the following functions:

keyGen(M)
This function generates a random key of length M.

encrypt(plain)
This function encrypts the message passed as a parameter using a randomly generated key.

decrypt(cypher, pad)
This function decrypts the message passed as a parameter using the key passed as the second parameter.

Example
To decrypt the message tyIxtSy using the key tniLfaY, simply run the script and enter the following command:

encrypt('hello','tniLfaY')

decrypt('tyIxtSy','tniLfaY')

The output will be hello.
