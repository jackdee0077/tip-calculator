# Get cost of food, number of payers and tip percent from the user
# Compute the total bill
# Total bill = tip_amount + cost_of_food + 10% tax
# Compute splited bill if number of payers is greater than 1 
# Repeat program until user enters no


def get_user_inputs(): 
  try:
    cost_of_food = int(input('Enter the cost of your food : '))
    number_of_payers = int(input('How many people will split this bill : '))
    tip_percentage = int(input('What is the percentage of tip : '))
  except ValueError: 
    print('Thats not a valid input') 
  return (cost_of_food, number_of_payers, tip_percentage)

def compute_total_bill(cost_of_food, number_of_payers, tip_percentage, sales_tax):
  tip_amount = cost_of_food * (tip_percentage/100)
  tax = cost_of_food * sales_tax
  total_bill = (tip_amount + cost_of_food + tax)
  print('Total bill: ${:0.2f}'.format(total_bill))
  if number_of_payers > 0: 
     splited_bill = total_bill / number_of_payers
     print ('Each person should pay ${:0.2f}'.format(splited_bill))

def main():
  SALES_TAX = 0.1
  cost_of_food, number_of_payers, tip_percentage = get_user_inputs()
  compute_total_bill(cost_of_food, number_of_payers, tip_percentage, SALES_TAX)


repeat = "yes"
while repeat == "yes":
    main()
    repeat == input("do you want to enter another tip? enter yes/no :")

