import json

my_numbers = [1, 2, 3, 4]

print([x**2 for x in my_numbers if x % 2 == 0])

my_file = open("./new_file.txt", "w")
# new array
my_file.write(
    json.dumps(
        [
            {"name": "Victor", "lastname": "Jimenez"},
            {"name": "Victor", "lastname": "Jimenez"},
        ]
    )
)

print("hecho!")
