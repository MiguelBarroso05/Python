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
