num = int(input("Enter your number: "))

if num % 2 == 0:
    print("The number is even:", num)
else:
    print("The number is odd:", num)

evensum = 0
for i in range(num + 1):
    if i % 2 == 0:
        evensum += i

print("Sum of even numbers from 1 to", num, ":", evensum)

oddsum = 0
for i in range(num + 1):
    if i % 2 != 0:
        oddsum += i

print("Sum of odd numbers from 1 to", num, ":", oddsum)




# best way

# def is_even(num):
#     return num % 2 == 0
#
#
# def sum_even_numbers(n):
#     return sum(i for i in range(1, n + 1) if i % 2 == 0)
#
#
# def sum_odd_numbers(n):
#     return sum(i for i in range(1, n + 1) if i % 2 != 0)
#
#
# def main():
#     num = int(input("Enter your number: "))
#
#     if is_even(num):
#         print("The number is even:", num)
#     else:
#         print("The number is odd:", num)
#
#     evensum = sum_even_numbers(num)
#     print("Sum of even numbers from 1 to", num, ":", evensum)
#
#     oddsum = sum_odd_numbers(num)
#     print("Sum of odd numbers from 1 to", num, ":", oddsum)
#
#
# if __name__ == "__main__":
#     main()
