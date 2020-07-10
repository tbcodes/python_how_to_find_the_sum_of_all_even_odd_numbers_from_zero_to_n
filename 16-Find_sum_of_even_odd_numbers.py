# How to calculate the sum of all even/odd numbers from zero to 'n'
# Youtube URL: https://youtu.be/xcu-1cO014Q

total = 0
# num = 500
num = int(input("Please, enter a number: "))
even_numbers = []

for i in range(0, num + 1):
  if i % 2 == 1:
    even_numbers.append(i)
    total += i

print(f"All odd numbers from 0 to {num} is: {even_numbers}")
print("········································")
print("The sum of odd numbers from 0 to {} is: {}".format(num, total))