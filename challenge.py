# 연간 매출 
def get_yearly_revenue(monthly_revenue):
    return monthly_revenue*12

monthly_revenue = 5500000
yearly_revenue = get_yearly_revenue(monthly_revenue)

print(f"Your  yearly revenue is: {yearly_revenue}$")


# 연간 비용
def get_yearly_expenses(monthly_expenses):
    return monthly_expenses

monthly_expenses = 2700000
yearly_expenses = get_yearly_expenses(monthly_expenses)

print(f"Your yearly expenses is: {yearly_expenses}$")

# 세금 

def get_tax_amount(profit):

    if profit > 100000:
        return profit * 0.25

    else:
        return profit * 0.15

yearly_revenue = 66000000
yearly_expenses = 2700000

profit = yearly_revenue - yearly_expenses

tax_amount = get_tax_amount(profit)

print(f"Your tax amount is: {tax_amount}$")

# 세액 공제 

def final_tax_amount(tax_amount, tax_credits):
    return tax_amount - (tax_amount * tax_credits)

tax_amount = 15825000
tax_credits = 0.01

print(f"Your final tax bill is: ${final_tax_amount(tax_amount, tax_credits)}$")



# BLUEPRINT | DONT EDIT

# monthly_revenue = 5500000

# monthly_expenses = 2700000

# tax_credits = 0.01
#
# yearly_revenue = get_yearly_revenue(monthly_revenue)
# yearly_expenses = get_yearly_expenses(monthly_expenses)
#
# profit = yearly_revenue - yearly_expenses
#
# tax_amount = get_tax_amount(profit)
#
# final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)
#
# print(f"Your tax bill is: ${final_tax_amount}")