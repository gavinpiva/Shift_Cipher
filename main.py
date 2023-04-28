import numpy as np
import math

def keyGen(M):
    alphList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    K = np.random.choice(alphList,M)
    # print(K)
    return K

def encrypt(plain):
    alphList = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
    numListM = []
    numListK = []
    for letters in plain:
        num = alphList.index(letters.lower())
        numListM.append(num)

    # print(numListM)
    pad = keyGen(len(plain))
    for letter in pad:
        padNum = alphList.index(letter.lower())
        numListK.append(padNum)
    # print(numListK)


    encrypted = []
    for i in range(len(numListM)):

        c = (numListM[i] + numListK[i])%26
        # print(c)
        encrypted.append(c)

    # print(encrypted)
    final = []
    for k in range(len(encrypted)):
        final.append(alphList[encrypted[k]])
    print(pad)
    print(final)
def decrypt(cypher,pad):
    alphList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v','w', 'x', 'y', 'z']
    cyphListM = []
    cyphListK = []

    for letters in cypher:
        M = alphList.index(letters.lower())
        cyphListM.append(M)
    for i in pad:
        K = alphList.index(i.lower())
        cyphListK.append(K)

    decrypted = []
    for j in range(len(cyphListM)):
        c = (cyphListM[j] - cyphListK[j]) % 26
        # print(c)
        decrypted.append(c)
    final = []
    for k in range(len(decrypted)):
        final.append(alphList[decrypted[k]])

    print(final)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Type the text you wish to encrypt:")
    # encrypt('Hello')
    decrypt('tyIxtSy','tniLfaY')

