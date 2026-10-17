names = ["Ama", "Kofi"]
ages = [22, 30]


for name, age in zip(names, ages):
    print(f"{name} is {age}")

details = dict(zip(names, ages))
print(details)