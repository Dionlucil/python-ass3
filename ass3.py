# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    # Apply discount only if 20% or more
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price  # No discount applied

# Prompt the user for input
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Output the result
if discount_percent >= 20:
    print(f"Discount applied! The final price is: {final_price:.2f}")
else:
    print(f"No discount applied. The price remains: {final_price:.2f}")
