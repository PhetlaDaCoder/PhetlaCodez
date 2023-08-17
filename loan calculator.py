print('Welcome to our loan deparment.')


def save_user(): #Saves client details.

    with open('User Details.txt', 'a') as f:
        f.write( user_details() +"\n")



def user_details(): #Prompts client to enter details.
    name = input('Please enter your name: ')
    surname = input('Please enter your surname: ')
    title = input('Please enter Title: ')
    acc_number = int(input('Please enter account number: '))
    id_number =int(input('Please enter you ID Number: '))
    phone = int(input('Please enter your phone number: '))
    email = input('Please enter your email address: ')
    
    

    
def eligabilty(): #checks if client is eligable for a loan.
    employment = str(input('Are you currently employed ? (yes or no) ')).lower()

    if employment == 'yes':
        print("You are eligable for a loan.")
        pass
    
    for answer in employment:
        if answer == 'no':
            print("Sorry your are not eligable for loan.")
            break


def loan_amount():
    loan = int(input('Please enter loan amount R '))
    Mon_Fee = (13/100 * loan + loan)
    Repay = Mon_Fee
    for a in Repay:
        if a in Repay:
            print("Total amount to repay is R", Repay)
            break


while True:
    option = input("Would you like to apply for a loan?  (y/n)") .lower()

    if option == 'n':
        print("Thank your for visting master loan services.")
        break

    
