# available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi calbe", "dvd driver"]
# current_choice = "-"
# computer_parts = []
#
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
#
# while current_choice != '0':
#     if current_choice in valid_choices:
#         print(f"Adding {current_choice}")
#         index = int(current_choice)
#         chosen_part = available_parts[index - 1]
#         computer_parts.append(chosen_part)
#     else:
#         print("Please add options from the list below:")
#         for number, part in enumerate(available_parts):
#             print(f"{number + 1}: {part}")
#
#     current_choice = input()
#
# print(computer_parts)

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub"
]

flowers = []
shrubs = []

# write your code here
for i in data:
    plantName = i.split("-")[0].strip()
    plantType = i.split("-")[1].strip()
    if plantType == "Flower":
        flowers.append(plantName)
    else:
        shrubs.append(plantName)

print(flowers)
print(shrubs)
