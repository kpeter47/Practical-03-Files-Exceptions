import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_prices.txt"  # Define the output file name

# Initialize variables
price = INITIAL_PRICE
day = 1

# Open the output file for writing
out_file = open(OUTPUT_FILE, 'w')

# Display the starting price
print(f"Starting price: ${price:.2f}")
print(f"Starting price: ${price:.2f}", file=out_file)

# Simulate stock price changes
while MIN_PRICE <= price <= MAX_PRICE:
    # Generate a random integer of 1 or 2
    # If it's 1, the price increases; otherwise, it decreases
    if random.randint(1, 2) == 1:
        # Generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    # Ensure the price is within the specified range
    price = max(MIN_PRICE, min(price, MAX_PRICE))

    # Display the price and write it to the output file
    print(f"On day {day} price is: ${price:.2f}")
    print(f"On day {day} price is: ${price:.2f}", file=out_file)

    day += 1

# Close the output file
out_file.close()
