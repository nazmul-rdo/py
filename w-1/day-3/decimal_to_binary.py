def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_num = ""
    while n > 0:
        binary_num = str(n % 2) + binary_num
        n = n // 2
    return binary_num


number = int(input("Enter your number: "))
binary = decimal_to_binary(number)
print("Binary:", binary)
