def bintodec(binary):
    decimal_num = 0
    power = len(binary) - 1

    for digit in binary:
        decimal_num += int(digit) * (2 ** power)
        power -= 1

    return decimal_num

def dectobin(decimal):

    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2

    return binary

