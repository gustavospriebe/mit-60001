total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25

current_savings = 0

r = 0.04

annual_salary = float(input("Enter your annual salary: "))

portion_saved = float(
    input("Enter the percent of your salary to save, as a decimal: "))

semi_annual_raise = float(
    input("Enter the percent of the semi-annual raise to save, as a decimal: "))

monthly_salary = annual_salary / 12

months = 0

while total_cost * portion_down_payment > current_savings:

    if months % 6 == 1 and months != 1:
        monthly_salary = monthly_salary + (monthly_salary * semi_annual_raise)

    current_savings += (current_savings * r / 12) + \
        monthly_salary * portion_saved
    months += 1

print(months)
