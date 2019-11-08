"""
Author: Bipin P. (mailto: bipinp2013@gmail.com)
http://iambipin.com

101010101    10  101010101    10  101     10    101010101
1010101010   10  1010101010   10  1010    10    1010101010
10      101  10  10      101  10  10 01   10    10      101
10      101  10  10      101  10  10  10  10    10      101
1010101010   10  1010101010   10  10   01 10    1010101010
1010101010   10  101010101    10  10    1010    101010101
10      101  10  10           10  10     010    10
10      101  10  10           10  10      10    10
1010101010   10  10           10  10      10    10
101010101    10  10           10  10      10    10  10

Python Program to Convert Floating-Point Decimal to Binary number
"""
def dec2bin(num):
    """"
    Function to convert a floating point decimal number to binary number
    """
    global wholeList
    global decList
    whole, dec = str(num).split('.')
    whole = int(whole)
    dec = int(dec)
    counter = 1
    
    while (whole / 2 >= 1):
            i = int(whole % 2)
            wholeList.append(i)
            whole /= 2
            
    decproduct = dec      
    while (counter <= places):
        decproduct = decproduct * (10**-(len(str(decproduct))))
        decproduct *= 2
        decwhole, decdec = str(decproduct).split('.')
        decwhole = int(decwhole)
        decdec = int(decdec)
        decList.append(decwhole)
        decproduct = decdec
        counter += 1
        
wholeList = []
decList = []
try:
    num = float(input('Enter a floating point decimal number: '))
    
except(ValueError):
    print('Please enter a valid floating point decimal')

try:
    places = int(input('Enter the number of decimal places in the result: '))
    dec2bin(num)
    if(len(wholeList) > 1):
        wholeList.reverse()
    wholeList.insert(0, 1)
    
    aster = '*'
    print(aster * 60)
    
    print('The binary number of {0} is:' .format(num))
    print(*wholeList, end =' ')
    print('.', end = ' ')
    print(*decList)
    
    print(aster * 60)
        
except(ValueError):
    print('Please enter a valid integer number for places')