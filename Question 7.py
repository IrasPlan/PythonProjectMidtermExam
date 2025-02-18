import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Create a new list to store only even numbers, but doubled
filtered_numbers = []

for num in random_numbers:
    if num % 2 == 0:  # Check if the number is even
        filtered_numbers.append(num * 2)  # Double the even number

# Print the final list
print(filtered_numbers)