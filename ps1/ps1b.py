annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the % of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))

monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved
portion_down_payment = 0.25 * total_cost
r = 0.04

current_savings = 0
count_months = 0


while current_savings <= portion_down_payment:    
    current_savings = (current_savings * r / 12) + monthly_savings + current_savings
    count_months += 1
    if count_months % 6 == 0:
        monthly_salary =  monthly_salary + monthly_salary * semi_annual_raise
        monthly_savings = monthly_salary * portion_saved 
print(count_months)


