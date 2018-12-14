def main():
    print("CHANGING YOUR COMPANY NAME HERE")
    customerList = []
    choice = menuOptions()
    while choice != 0:
        if choice == 1:
            customerList.append(customerInformation())
        elif choice == 2:
            print()
            print("CUSTOMER LIST")
            for customer in customerList:
                fmt1 = "{:15}{:15s}{:15s}{:15s}"
                fmt1_2 = "{:15}{:15s}{:15s}{:5,.2f}"
                print(fmt1.format("First name:","Last name:","Phone:","Monthly payment:"))
                print(fmt1_2.format(customer[0],customer[1],customer[2],customer[3]))
                
        else:
            print("Invalid input")
        choice = menuOptions()
        
            
def loanPayment():
    principal = float(input("Enter the principal of your customer car loan: "))
    interestRate = float(input("Enter your annual interest rate (10% entered  as 0.1): "))
    interestRate = interestRate / 12
    loanTerm = int(input("Enter the loan term in month: "))
    monthlyPayment = (interestRate * principal) / (1 - (1 + interestRate) ** -loanTerm)
    return monthlyPayment

def phoneChecker(phone):
    if len(phone) == 12:
        if phone[3] == "-" and phone[7] == "-":
            if phone[0:3].isdigit() and phone[4:7].isdigit and phone[8:12].isdigit:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def menuOptions():
    print()
    print("MENU OPTIONS")
    optionsList = ["0.Quit","1.Adding customer information","2.Print out the customer list"]
    for options in optionsList:
        print(options)
    choice = input("Enter your choice: ")
    while not choice.isdigit() or int(choice) not in range(len(optionsList)):
        print("Invalid input, try again.")
        choice = input("Enter your choice: ")
    return int(choice)
        
def customerInformation():
    print()
    firstName = input("Enter your customer first name: ")
    lastName = input("Enter your customer last name: ")
    phone = input("Enter your customer phone number (Entered as xxx-xxx-xxx): ")
    while phoneChecker(phone) != True:
        phone = input("Your number is not valid. Please enter your customer phone number (Entered as xxx-xxx-xxx): ")
    monthlyPayment = loanPayment()
    return firstName, lastName, phone, monthlyPayment

main()
