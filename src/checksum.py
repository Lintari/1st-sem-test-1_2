def modulo11Checksum(ISBNNumber: str):

    digits = []
    for char in ISBNNumber:
        if char.isdigit():
            digits.append(int(char))
        elif (len(digits) == 9) and char == 'X':
            digits.append(10)
        elif char != '-' and char != ' ':
            return False


    if len(digits) != 10:
        return False

    checkDigit = digits[-1]

    total = 0
    for i in range(len(digits) - 1):
        weight = 10 - i
        digit = digits[i]
        total += digit * weight

    checksum = total + checkDigit
    return checksum % 11 == 0
