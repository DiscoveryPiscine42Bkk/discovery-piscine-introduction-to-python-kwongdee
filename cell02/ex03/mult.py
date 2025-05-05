first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))

result = first_num * second_num

print(f"{first_num} x {second_num} = {result}")

if result > 0:
    print("This result is positive.")

elif result < 0:
    print("This result is negative.")

else:
    print("This result is positive and negative.")