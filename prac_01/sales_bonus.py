"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


LOW_PROPORTION = 0.1
HIGH_PROPORTION = 0.15
RESTRICT = 1000
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < RESTRICT:
        bonus = sales * LOW_PROPORTION
    else:
        bonus = sales * HIGH_PROPORTION
    print(f"Bonus: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
