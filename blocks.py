# for i in range(1, 13):
#     print(f"No. {i:2} squared is {i ** 2:3} and cubed is {i ** 3:4}")
#
# print("*" * 80)

name = input("Please enter your name: ")
age = int(input(f"How old are you {name}? "))
print(age)

if age >= 18:
    print("You're old enough to vote!")
    print("Please put an X in the box")
else:
    print(f"Please come back in {18 - age} years")

if age < 18:
    print(f"Please come back in {18 - age} years")
else:
    print("You're old enough to vote!")
    print("Please put an X in the box")
