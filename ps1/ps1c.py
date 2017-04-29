annual_salary = float(input("Enter the starting salary:"))

total_cost = 1000000
semi_annual_raise = 0.07
r = 0.04 
portion_down_payment = 0.25 * total_cost
monthly_salary = annual_salary / 12
current_savings = 0

epsilon = 100 
low = 0
high = 10000
steps = 0

if monthly_salary * 36 < portion_down_payment:
    print ("It is not possible to pay the down payment in three years")
    
while abs(portion_down_payment - current_savings) >= epsilon:
    current_savings = 0
    portion_saved = (high + low) / 2
    monthly_salary = annual_salary / 12
                    
    for count_month in range (36):
        
        if (count_month + 1) % 6 == 0:
            monthly_salary = monthly_salary * (semi_annual_raise + 1)
       
        monthly_savings = monthly_salary * (portion_saved/10000)
        current_savings = (current_savings * r / 12) + current_savings + monthly_savings
        
    if current_savings < portion_down_payment:
        low = portion_saved
        
    else:
        high = portion_saved
        steps += 1 

if portion_saved > portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
    
else:
    print("Best savings rate:", portion_saved/10000)
    print("Steps in bisection search:", steps)