# Caesar Cipher

CC = {}
CC2 = {}
test= ""

userMessage = input("Enter a message you want to encrypt using the Caesar Cipher: ")
keyValue = 5     #= input("Enter the key value (1-25) to encrypt your message using the Caesar Cipher: ")


charList = list(userMessage)
print(charList)


for x in range (0, len(userMessage)):
    test = charList[x]
    print(test)
    

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

CC2[str((1 + keyValue)%26)] = 'a'
CC2[str((2 + keyValue)%26)] = 'b'
CC2[str((3 + keyValue)%26)] = 'c'
CC2[str((4 + keyValue)%26)] = 'd'
CC2[str((5 + keyValue)%26)] = 'e'
CC2[str((6 + keyValue)%26)] = 'f'
CC2[str((7 + keyValue)%26)] = 'g'
CC2[str((8 + keyValue)%26)] = 'h'
CC2[str((9 + keyValue)%26)] = 'i'
CC2[str((10 + keyValue)%26)] = 'j'
CC2[str((11 + keyValue)%26)] = 'k'
CC2[str((12 + keyValue)%26)] = 'l'
CC2[str((13 + keyValue)%26)] = 'm'
CC2[str((14 + keyValue)%26)] = 'n'
CC2[str((15 + keyValue)%26)] = 'o'
CC2[str((16 + keyValue)%26)] = 'p'
CC2[str((17 + keyValue)%26)] = 'q'
CC2[str((18 + keyValue)%26)] = 'r'
CC2[str((19 + keyValue)%26)] = 's'
CC2[str((20 + keyValue)%26)] = 't'
CC2[str((21+ keyValue)%26)] = 'u'
CC2[str((22 + keyValue)%26)] = 'v'
CC2[str((23 + keyValue)%26)] = 'w'
CC2[str((24 + keyValue)%26)] = 'x'
CC2[str((25 + keyValue)%26)] = 'y'
CC2[str((26 + keyValue)%26)] = 'z'
CC2[str(27)] = ' '
