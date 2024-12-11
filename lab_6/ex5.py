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