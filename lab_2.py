#Point 2
date = {
    "day": 27,
    "month": "October",
    "year": 1971
}
calender_event = {
    "title" : "class",
    "date" : date,
    "hour" : 20,
    "description" : "lorem ipsum",
}
person = {
    "name" : "Miguel",
    "age" : 23,
    "city" : "Vendas Novas"
}
product ={
    "name" : "Razer Barracuda",
    "price" : 59.99,
    "quantity_available" : 37,
    "category" : "Headphones"
}
print(date,"\n", calender_event,"\n", person,"\n", product)
print("-"*50)
date["day"] = 5
calender_event["hour"] = 16
person["city"] = "Evora"
product["price"] = 89.99
print(date,"\n", calender_event,"\n", person,"\n", product)
print("-"*50)
person["job"] = "Programmer"
print(person)
print("-"*50)
person.pop("job")
print(person)
print("-"*50)
#Point 3
numbers = [12, 7, 25, 43, 18, 5, 36, 9, 21, 50]
names = ["Carolina", "João", "Maria", "Pedro", "Sofia"]
tasks = [
    "Prepare breakfast",
    "Respond to emails",
    "Study Python",
    "Exercise",
    "Prepare dinner"
]
print(numbers[0],numbers[-1])
print(names[0],names[-1])
print(tasks[0],tasks[-1])
print("-"*50)

numbers.append(49)
names.append("Miguel")
tasks.append("Go to Sleep")

print(numbers)
print(names)
print(tasks)
print("-"*50)

numbers.pop(1)
names.pop(1)
tasks.pop(1)

print(numbers)
print(names)
print(tasks)
print("-"*50)

numbers.sort()
names.sort()
tasks.sort()

print(numbers)
print(names)
print(tasks)
print("-"*50)

for name in names:
    print(f"Hello {name}")
print("-"*50)
#Point 4
student = {
    "name": "Carlos",
    "age": 21,
    "grades": [8.5, 9.2, 7.8]
}
products = [
    {"name": "T-shirt", "price": 29.99, "quantity": 50},
    {"name": "Sneakers", "price": 120.00, "quantity": 30},
    {"name": "Watch", "price": 250.50, "quantity": 15}
]

print(student["grades"])
print("-"*50)

student["grades"].append(7.5)
print(student["grades"])
print("-"*50)

for product2 in products:
    print(product2["name"])
print("-"*50)

products[1]["price"]= 100

print(products[1])
print("-"*50)

products.pop(-1)

print(products)