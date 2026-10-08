# Problem: Calculate discount based on purchase amount
# > $100: 10%, > $500: 20%, > $1000: 30%

amount = 750

if amount > 1000:
    discount = 0.30
elif amount > 500:
    discount = 0.20
elif amount > 100:
    discount = 0.10
else:
    discount = 0

final_price = amount * (1 - discount)
print(f"Original: ${amount}")
print(f"Discount: {discount*100}%")
print(f"Final: ${final_price:.2f}")