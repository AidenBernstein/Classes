#Aiden Bernstein
#9/3/2022
#Bernstein_Farenheit_to_celsius.py
#convert temperature from Farenhheit to Celsius

def main():
    user_input = float(input("Input temperature in farenheit: "))   #Get user input as a float
    celsius = (5/9) * (user_input - 32)                             #convert farenheit to celsius
    print("Temperature in celsius is: ", format(celsius, '.2f'))    #print degrees in celsius

main()
