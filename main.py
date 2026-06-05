def say_hello(user_name):
    print("Hello", user_name, "how r u?")

say_hello("hanisoo")
say_hello("nico")


def tax_cal(money):
    print("Your tax is",money*0.35)

tax_cal(15000000000000000)
tax_cal(25000000000000000)


def say_hello(user_name="anonymous"):
    print("hello",user_name)

say_hello("hanisoo")
say_hello()


def plus(a=0, b=0):
    print(a - b)
   
plus()


def tex_calcul(money):
    return money * 0.35

def pay_tax(tax):
    print("Thank you for paying", tax)

to_pay=tex_calcul(15000000000000000)
pay_tax(to_pay)

pay_tax(tex_calcul(15000000000000000))


my_name="hanisoo"
my_age=55
my_eye_color="brown"

print(f"Hello I'm {my_name}, I have {my_age} years in the earth, {my_eye_color} is my eye color")


def make_americano(coffee):
    return f"{coffee}+🫗"

def add_milk(americano):
    return f"{americano}+🥛"

def add_ice(milk_coffee):
    return f"{milk_coffee}+🧊"

americano = make_americano("🫘")
milk_coffee = add_milk(americano)
iced_latte = add_ice(milk_coffee)

print(iced_latte)