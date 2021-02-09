# Not efficient at all, but not sure of any other ways currently.
b1 = int(input("enter a digit at a time, if theres no more digits put a 0 \n"))
b2 = int(input("enter a digit at a time, if theres no more digits put a 0 \n"))
b3 = int(input("enter a digit at a time, if theres no more digits put a 0 \n"))
b4 = int(input("enter a digit at a time, if theres no more digits put a 0 \n"))
b5 = int(input("enter a digit at a time, if theres no more digits put a 0 \n"))
b6 = int(input("enter a digit at a time, if theres no more digits put a 0 \n"))
b7 = int(input("enter a digit at a time, if theres no more digits put a 0 \n"))
b8 = int(input("enter a digit at a time, if theres no more digits put a 0 \n"))
bd1 = b1 * 1
bd2 = b2 * 2
bd3 = b3 * 4
bd4 = b4 * 8
bd5 = b5 * 16
bd6 = b6 * 32
bd7 = b7 * 64
bd8 = b8 * 128
b21 = int(input("enter a digit at a time for second number, if theres no more digits put a 0 \n"))
b22 = int(input("enter a digit at a time for second number, if theres no more digits put a 0 \n"))
b23 = int(input("enter a digit at a time for second number, if theres no more digits put a 0 \n"))
b24 = int(input("enter a digit at a time for second number, if theres no more digits put a 0 \n"))
b25 = int(input("enter a digit at a time for second number, if theres no more digits put a 0 \n"))
b26 = int(input("enter a digit at a time for second number, if theres no more digits put a 0 \n"))
b27 = int(input("enter a digit at a time for second number, if theres no more digits put a 0 \n"))
b28 = int(input("enter a digit at a time for second number, if theres no more digits put a 0 \n"))
bd21 = b21 * 1
bd22 = b22 * 2
bd23 = b23 * 4
bd24 = b24 * 8
bd25 = b25 * 16
bd26 = b26 * 32
bd27 = b27 * 64
bd28 = b28 * 128
# long math to turn it into a real number the convert it back to binary
dec1 = bd1 + bd2 + bd3 + bd4 + bd5 + bd6 + bd7 + bd8
dec2 = bd21 + bd22 + bd23 + bd24 + bd25 + bd26 + bd27 + bd28
resultdec = dec1 + dec2
print("your binary result is")
# same loop i used in dec-bin converter but slightly modified, outputs correct answer
loop1 = True
while loop1 is True:
    if resultdec == 0:
        loop1 = False
    else: 
        resultdec1 = resultdec // 2
        resultdec3 = resultdec % 2
        resultdec = resultdec1
        print(resultdec3)
# solution worked with every number ive tested so far
input()
