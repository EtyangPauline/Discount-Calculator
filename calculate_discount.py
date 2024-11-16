def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or more, apply the discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after applying the discount (if applicable).
    """
    if discount_percent >= 20:
        # Apply discount if percentage is 20% or more
        return price - (price * discount_percent / 100)
    else:
        # No discount applied
        return price


# Main program
try:
    # Prompt the user for the original price and discount percentage
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result based on whether the discount was applied
    if final_price < original_price:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")

except ValueError:
    # Handle invalid input
    print("Invalid input! Please enter numeric values for both price and discount percentage.")
