#  write a program to check any elememnt randomly of a list whether it is integer or not.
import random

my_list = ["hitesh", 1, 8, 665.65, 45 + 5j, "gift", True]

# Generate a random index in range of the list length
index = random.randint(0, len(my_list) - 1)

# Check the data type of the item at the randomly chosen index
if isinstance(my_list[index], bool):
    print(f"No, {my_list[index]} is not an integer...")
elif isinstance(my_list[index], int):
    print(f"Yes, {my_list[index]} is an integer...")
else:
    print(f"No, {my_list[index]} is not an integer...")


       
