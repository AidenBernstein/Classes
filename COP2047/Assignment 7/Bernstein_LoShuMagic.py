#Author Name: Aiden Bernstein
#Date: 10/16/2022
#Program Name: Bernstein_LoShuMagic.py
#Purpose: Verify magic squares of any order

def main():
    order = int(input("Please enter order of magic square (side length): "))    #get order of magic square
    square = [[0] * order for i in range(order)]                                #generate 2d array of the correct order

    num = 0                                                                     #populate array with starting values
    for i in range(len(square)):
        for j in range(len(square[0])):
            num += 1
            square[i][j] = num

    for i in square:                                                            #print starting array
        for j in i:
            print(j, end='\t')
        print()

    for i in range(len(square)):                                                #get values for each cell in array
        for j in range(len(square[i])):
            square[i][j] = int(input(f'Please enter number {(((i)*len(square)) + (j+1))}: '))

    for i in square:                                                            #print array again
        for j in i:
            print(j, end='\t')
        print()

    magic_num = 0

    for i in square[0]:                                                         #find the magic number
        magic_num += i

    for i in square:                           #Verify rows
        sum = 0
        for j in i:
            sum += j
        if sum != magic_num:
            return "Not a magic square"

    for j in range(len(square[0])):             #verify columns
        sum = 0
        for i in range(len(square)):
            sum += square[i][j]
        if sum != magic_num:
            return "Not a magic square"

    sum = 0
    for i in range(len(square)):                #verify diagonal from top left to bottom right
        sum += square[i][i]
    if sum != magic_num:
        return "Not a magic square"
    
    sum = 0
    i = len(square) - 1                         #verify diagonal from bottom left to top right
    j = 0
    while i >= 0:
        sum += square[i][j]
        i -= 1
        j += 1
    if sum != magic_num:
        return "Not a magic square"

    return "Found magic square"

    



print(main())