def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        return "Error: Non-numeric data found in the list"

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = [10, 20, 'a', 40, 50] 
result = calculate_average(my_numbers) 
print(f"The average is: {result}")
