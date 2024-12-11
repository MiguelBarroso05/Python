def verify_gtin_code(code):
    digits = [int(d) for d in str(code)]
    if len(digits) < 2:
        return False
    provided_check_digit = digits[-1]
    digits = digits[:-1]
    total = 0
    for i, digit in enumerate(reversed(digits)):
        weight = 3 if i % 2 == 0 else 1  
        total += digit * weight
    calculated_check_digit = (10 - (total % 10)) % 10
    if total == 0:
        return False
    return provided_check_digit == calculated_check_digit


print(verify_gtin_code(12345670))
print(verify_gtin_code(12345678))
print(verify_gtin_code(00000000))
