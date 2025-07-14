# apu_chain = -4

# if apu_chain > 30 :
#     print("APU chain is greater than 30")
# elif apu_chain > 25:
#     print("APU chain  is less than 30")
# elif apu_chain > 10 :
#     print("APU chain is greater than 10")
# else:
#     print("APU chain -4")

# logical operators (and, or, not)
# high_income = True
# good_credit = True
# # good_credit = False
# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")


# chaining comparisons
age = 22
# if age >= 18 and age < 65:
#     print("Eligible to vote")

# if 18 <= age < 65:
#     print("Eligible to vote")

# ternary operator

# if age >= 18:
#     message = "Eligible to vote"
# else:
#     message = "Not eligible to vote"

# 
# x = 0 
# result = "positive" if x > 0 else "negative"
# result = "positive" if x > 0 else ("zero " if x == 0 else "negative")
# print(result)  
quantity = 5
unit_price = 1000
is_regular_customer = True
discount = 0.1 

toal_price = quantity * unit_price

# print(f"Total price: {toal_price}")

if is_regular_customer:
    discount = toal_price * discount
    # toal_price = toal_price - discount
    toal_price -= discount

print(f"Discount applied: {discount}")
print(f"Total price after discount: {toal_price}")
