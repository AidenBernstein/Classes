#Author Name: Aiden Bernstein
#Date: 9/25/2022
#Program Name: Bernstein_Population.py
#Purpose: find the approximate size of a population

def main():
    num = int(input("Starting number of organism: "))
    increase = (int(input("Average daily increase: ")[:-1]))/100    #get input and remove % sign, then divide by 100 to get percentage
    days = int(input("Number of days to multiply: "))

    print("Day approximate\tPopulation")
    for i in range(days):
        print(str((i + 1)) + "\t\t" + format(num, ".5f"))           #format population to 5 decimals
        num *= (increase + 1)                                       #increase number

main()