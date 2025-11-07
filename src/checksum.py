def modulo11Checksum(ISBNNumber: str):

    digits = [int(char) for char in ISBNNumber if char.isdigit()]
    for char in ISBNNumber:
	if char.isdigit():
	    digit.append(int(char))
	elif (len(digit) == 9) and char == 'X':
	    digits.append(10)
	    

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
