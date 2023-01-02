print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = float(input("What percentage of tip would you like to give? 10, 12 or 15? "))

bill = total_bill + (tip/100)*total_bill

share = bill/people

print("$" + str(round(share,1)))