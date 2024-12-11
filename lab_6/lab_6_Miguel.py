#Ex1

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


#Ex2

def change_unity(temp, unity):
    try:
        if unity == "c":
            return f"{temp * 9/5 + 32} °F"
        elif unity == "f":
            return f"{(temp - 32) * 5/9} °C"
        else:
            return Exception
    except Exception:
        return "Error: invalid input"
    
print(change_unity(0,"c"))
print(change_unity(100,"c"))
print(change_unity(32,"f"))
print(change_unity(-40,"c"))
print(change_unity("ciquenta","c"))


#Ex3

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


#Ex4

def calculate_bmi(weight, height):
    if weight <= 0:
        return "Error: invalid weight"
    if height <= 0:
        return "Error: invalid height"
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        classification = "Bellow the weight"
    elif 18.5 <= bmi <= 24.9:
        classification = "Normal weight"
    elif 25 <= bmi <= 29.9:
        classification = "Above weight"
    elif 30 <= bmi <= 34.9:
        classification = "Obesity grau 1"
    elif 35 <= bmi <= 39.9:
        classification = "Obesity grau 2"
    else:
        classification = "Obesity grau 3"

    return f"IMC = {bmi:.2f}, Classification: \"{classification}\""

print(calculate_bmi(70, 1.75)) 
print(calculate_bmi(50, 1.60)) 
print(calculate_bmi(90, 1.60)) 
print(calculate_bmi(-70, 1.75))
print(calculate_bmi(70, 0))

#Ex5

def convert_distance(distance, unit):
    try:
        distance = float(distance)
        if distance < 0:
            return "Error: distance negative"
    except ValueError:
        return "Error: input invalid"

    if unit.lower() =="km":
        converted_distance = distance * 0.621371  
        return f"{converted_distance:.2f} milhas"
    elif unit.lower() == "milhas":
        converted_distance = distance / 0.621371  
        return f"{converted_distance:.2f} km"
    else:
        return "Error: unity invalid"


print(convert_distance(10, "km"))        
print(convert_distance(5, "milhas"))     
print(convert_distance(-10, "km"))       
print(convert_distance("dez", "km"))     
print(convert_distance(10, "metros"))    
