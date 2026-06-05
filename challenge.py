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



# 챌린지 조건
# get_yearly_revenue (연간 매출 계산)
# monthly_revenue (월간 매출)를 인수로 받고, 연간 매출(revenue for a year)을 리턴.
# get_yearly_expenses (연간 비용 계산)
# monthly_expenses (월간 비용)를 인수로 받고, 연간 비용(expenses for a year)을 리턴.
# get_tax_amount (세금 계산)
# profit (이익)을 인수로 받고, tax_amount (세금 금액)를 리턴.
# apply_tax_credits (세액 공제 적용)
# tax_amount (세금 금액), tax_credits (세액 공제율)을 인수로 받고, 할인할 금액(amount to discount)을 리턴.

# 요구사항:

# get_tax_amount 함수는 if/else를 사용해야 합니다.
# 만약 profit이 100,000 초과이면, 세율은 25%가 되어야 합니다.
# 아닌 경우에는, 세율은 15%가 되어야 합니다.