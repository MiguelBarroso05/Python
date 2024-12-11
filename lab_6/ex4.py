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