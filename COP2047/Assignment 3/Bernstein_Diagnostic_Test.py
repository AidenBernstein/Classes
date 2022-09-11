#Aiden Bernstein
#9/11/2022
#Bernstein_Diagnostic_Test.py
#Differentiate between COVID-19, Flu, Allergies, and Cold

def main():
    Question2 = ""                                                          # Create the "Question2" variable
    fever = input("Do you have a fever? (yes/no): ").lower()                # Get user input in all lower case letters

    if (fever == "yes"):                                                    # Place the next question in the "Question2" variable
        Question2 = "Are you experiencing shortness of breath? (yes/no): "
    elif (fever == "no"):
        Question2 = "Do you have itchy eyes? (yes/no): "
    else:
        print("Invalid input entered, program ended")                       # Exit the program if invalid input is input
        exit


    Q2Answer = input(Question2).lower()                                     # Get answer to question 2 in all lower case

    if(fever == "yes" and Q2Answer == "yes"):                               # tell the user what illness they may have
        print("You MAY have COVID-19")
    elif(fever == "yes" and Q2Answer == "no"):
        print("You MAY have the flu")
    elif(fever == "no" and Q2Answer == "yes"):
        print("You MAY have allergies")
    elif(fever == "no" and Q2Answer == "no"):
        print("You MAY have the common cold")
    else:
        print("Invalid input entered, program ended")                       # Exit the program if invalid input is input
        exit


main()                                                                      # run the program