# Caesar Cipher

# hash table with alphabet linked to a number 1-26
CC = {}


# two list data structures to hold the encrypted message (shiftList) and hold the original numeric values (numericList)
numericList = []
shiftList = []


CC['a'] = '1'
CC['b'] = '2'
CC['c'] = '3'
CC['d'] = '4'
CC['e'] = '5'
CC['f'] = '6'
CC['g'] = '7'
CC['h'] = '8'
CC['i'] = '9'
CC['j'] = '10'
CC['k'] = '11'
CC['l'] = '12'
CC['m'] = '13'
CC['n'] = '14'
CC['o'] = '15'
CC['p'] = '16'
CC['q'] = '17'
CC['r'] = '18'
CC['s'] = '19'
CC['t'] = '20'
CC['u'] = '21'
CC['v'] = '22'
CC['w'] = '23'
CC['x'] = '24'
CC['y'] = '25'
CC['z'] = '26'
CC[' '] = '27'

CC['1'] = 'a'
CC['2'] = 'b'
CC['3'] = 'c'
CC['4'] = 'd'
CC['5'] = 'e'
CC['6'] = 'f'
CC['7'] = 'g'
CC['8'] = 'h'
CC['9'] = 'i'
CC['10'] = 'j'
CC['11'] = 'k'
CC['12'] = 'l'
CC['13'] = 'm'
CC['14'] = 'n'
CC['15'] = 'o'
CC['16'] = 'p'
CC['17'] = 'q'
CC['18'] = 'r'
CC['19'] = 's'
CC['20'] = 't'
CC['21'] = 'u'
CC['22'] = 'v'
CC['23'] = 'w'
CC['24'] = 'x'
CC['25'] = 'y'
CC['26'] = 'z'
CC['27'] = ' '


#get user input for the original message to be encrypted and for the key value (if number is greater than 26 the key will loop back to 1, EX: 27 = keyValue 1)
userMessage = input("Enter a message you want to encrypt using the Caesar Cipher: ")
keyValue = int(input("Enter the key value (1-26) to encrypt your message using the Caesar Cipher: "))


#charList is a list of all chars in the user's message 
charList = list(userMessage)

#for loop that will run through charList and add the keyValue to the originalValue of a char then append the encrypted chars to shiftList
for x in range (0, len(userMessage)):
    messageChar = charList[x]

    numericList.append(CC[messageChar])

    
    if(CC[messageChar] == '27'):
        messageNumber = int(CC[messageChar])
    else:
        messageNumber = ((int(CC[messageChar]) + keyValue)%26)
    
    
    shiftList.append(CC[str(messageNumber)])
    

encryptedString = ''.join(shiftList)
print(encryptedString)
