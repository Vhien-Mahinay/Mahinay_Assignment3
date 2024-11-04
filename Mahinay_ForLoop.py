# Define the range
start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))

# For loop to calculate sum of even numbers
even_sum = 0
for num in range(start, end + 1):
    if num % 2 == 0:
        even_sum += num

print("Sum of even numbers:", even_sum)