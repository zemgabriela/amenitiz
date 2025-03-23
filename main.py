import json
from function import calculating_price

# Load price and discount data
with open("data/price_data.json", "r") as f:
    price_dict = json.load(f)

with open("data/discount_data.json", "r") as f:
    discount_dict = json.load(f)

def main():
    print("Welcome to the Shopping Cart System")
    print("Enter product codes separated by spaces (e.g., 'GR1 GR1 SR1 CF1')")

    # User input
    cart_input = input("Enter your cart items: ").strip().upper()
    cart = cart_input.split()

    # Calculate final price
    total_price = calculating_price(cart, discount_dict, price_dict)

    print(f"\nFinal total price: €{total_price:.2f}")

if __name__ == "__main__":
    main()
