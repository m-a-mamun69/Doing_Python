
def calculate_discount(price, discount):
    final_price = price - (price * discount/100)
    return final_price

original_price = int(input("Enter the Product Price: "))
discount_rate = int(input("Enter the Discount Rate: "))
discounted_price = calculate_discount(original_price, discount_rate)

print(f"The Product Price after Discount is: {discounted_price}BDT")
