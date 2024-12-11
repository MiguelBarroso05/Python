def luhn_check(number):
    digits = [int(d) for d in str(number)]
    total = 0
    should_double = False

    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]
        if should_double:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        should_double = not should_double
    if total == 0:
        return False
    return total % 10 == 0


print(luhn_check(4532015112830366))
print(luhn_check(1234567812345678))
print(luhn_check(4111111111111111))
print(luhn_check(0000000000000000))
