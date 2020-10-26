available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi calbe", "dvd driver"]
current_choice = "-"
computer_parts = []

valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]

while current_choice != '0':
    if current_choice in valid_choices:
        print(f"Adding {current_choice}")
        index = int(current_choice)
        chosen_part = available_parts[index - 1]
        computer_parts.append(chosen_part)
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print(f"{number + 1}: {part}")

    current_choice = input()

print(computer_parts)
