# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

def interest_calculation():
    loan = float(input("Enter Your loan Amount: "))
    rate = float(input("Enter your interest rate: "))
    time = float(input("Enter your duration (in years): "))

    simple_interest = round((loan * rate * time) / 100, 2)

    print(f"Your total simple interest accrued is: ${simple_interest:.2f}")

interest_calculation()
