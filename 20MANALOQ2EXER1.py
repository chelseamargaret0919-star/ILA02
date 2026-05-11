#Electricity Bill Calculator

#Asks the user for the amount of kWh used
print("Welcome to an Electricty Bill Calculator!")
kwh = float(input("Enter the number of kilowatt-hours (kWh) used: "))

def electricity_bill_calculator(kwh):
    #Charges 50 for all customers
    basic_charge = 50

    #Determines the amount based on kWh used
    if kwh <= 100:
        total_bill = basic_charge + 5*kwh
    elif kwh <= 200:
        total_bill = basic_charge + 7*kwh
    elif kwh <= 500:
        total_bill = basic_charge + 10*kwh
    else:
        total_bill = (basic_charge + 12*kwh) + 500

    #Return the calculated total bill
    return total_bill

#Calls the function
bill = electricity_bill_calculator(kwh)
print(f"Your total electricity bill is {bill} pesos.")

        
        
