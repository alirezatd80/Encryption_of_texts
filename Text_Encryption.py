def Encryption(text):
    result = ''
    for i in text:
        numchar = ord(i) * 2 +10
        result += chr(numchar)
    print('your result is : ', result)

def Decoding(text):
    result = ''
    for i in text:
        numchar = (ord(i)-10)//2
        result += chr(numchar)
    print('your result is : ' , result)

while True:
    inputText = input('enter your text :')
    
    
    orderinput = input('1 for Encryption\n2 for decoding\n3 for exit\nyour order : ')
    
    if orderinput == "1":
        Encryption(inputText)
    elif orderinput == "2":
        Decoding(inputText)
    elif orderinput == "3":
        print('thanks bye')
        break
    else:
        print('enter correct order')
    