annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the % of your salary to save, as decimal:"))
total_cost = float(input("Enter the cost of your dream house: "))
monthly_salary = annual_salary / 12
count_months = 0
monthly_savings = monthly_salary * portion_saved
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04

while current_savings <= portion_down_payment:
    current_savings = current_savings * r / 12 + monthly_savings + current_savings
    count_months += 1
print(count_months)

