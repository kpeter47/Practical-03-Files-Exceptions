import random

# What did you see on line 1?
# Line 1 displays a random integer between 5 and 20, inclusive.

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 5, and the largest is 20.

# What did you see on line 2?
# Line 2 displays a random integer between 3 (inclusive) and 10 (exclusive) with a step of 2.

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 3, and the largest is 9. No, line 2 could not have produced a 4, as it's not within the specified range.

# What did you see on line 3?
# Line 3 displays a random floating-point number between 2.5 (inclusive) and 5.5 (exclusive).

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 2.5, and the largest is 5.499999999999999.

# Code to produce a random number between 1 and 100 inclusive:
random_number = random.randint(1, 100)
print(random_number)
