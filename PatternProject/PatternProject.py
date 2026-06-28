#Natividad Mark Lorenz P. ict-102

#pyramid
n = int(input("Enter a no. of rows: "))
c = input("Enter the character you want to print: ")
for rows in range (n):
    for column in range (n-rows-1):
            print(" ", end = "")
    for column in range(rows+1):
            print(c, end = " ")
    print()

#square
a = int(input("Enter a no. of rows: "))
c = input("Input character: ")
for rows in range (a):
    for col in range (a):
        print(c, end = ' ')
    print()

#Increasing triangle
a = int(input("Enter no. rows: "))
b = input("Enter char. :")

for rows in range(a):
    for column in range(rows+1):
        print(b,end = " ")
    print()

#decreasing triangle
a = int(input("Enter rows: "))
b = input("Enter char: ")

for rows in range(a):
    for col in range (rows, a):
        print (b, end = " ")
    print()

#Right sided triangle

a = int(input("enter a rows: "))
b = input("enter char: ")

for row in range(a):
    for col in range(row, a):
        print(" ", end = " ")#for spacing
    for col in range(row+1):
        print(b, end = " ") #for printing the symbol and space of it
    print()

#decreasing right triangle
a = int(input("enter a rows: "))
b = input("enter char: ")

for row in range(a):
    for col in range(row+1):
        print(" ", end = " ")
    for col in range (row, a):
        print(b, end = " ")
    print()

#hill pattern no top
a = int(input("enter a rows: "))
b = input("enter char: ")

for row in range(a):
    for col in range(row,a):
        print(" ", end = " ")#for spacing

    for col in range(row+1): #for printing the symbol and space of symbol
        print(b, end = " ")
    for col in range(row+1):
        print(b, end=" ")
    print()

#hill pattern with top
a = int(input("enter a rows: "))
b = input("enter char: ")

for row in range(a):
    for col in range(row,a):
        print(" ", end = " ")#for spacing

    for col in range(row):#make it 1 less column
        print(b, end = " ")
    for col in range(row+1):#for printing the symbol and space of symbol
        print(b, end=" ")
    print()

#reverse hill pattern
a = int(input("enter a rows: "))
b = input("enter char: ")

for row in range(a):
    for col in range(row+1):
        print(" ", end = " ")#for spacing

    for col in range(row,a-1):#make it 1 less column
        print(b, end = " ")
    for col in range(row,a):#for printing the symbol and space of symbol
        print(b, end=" ")
    print()

#diamond
a = int(input("enter a rows: "))
b = input("enter char: ")
#top
for row in range(a-1):
    for col in range(row,a):
        print(" ", end = " ")#for spacing

    for col in range(row):#make it 1 less column
        print(b, end = " ")
    for col in range(row+1):#for printing the symbol and space of symbol
        print(b, end=" ")
    print()
#bottom
for row in range(a):
    for col in range(row+1):
        print(" ", end = " ")#for spacing

    for col in range(row,a-1):#make it 1 less column
        print(b, end = " ")
    for col in range(row,a):#for printing the symbol and space of symbol
        print(b, end=" ")
    print()