# Define the range
start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))

# While loop to calculate sum of odd numbers
odd_sum = 0
num = start
while num <= end:
    if num % 2 != 0:
        odd_sum += num
    num += 1

print("Sum of odd numbers:", odd_sum)