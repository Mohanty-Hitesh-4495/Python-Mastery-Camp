# Define a function 'greet' with a default parameter 'name'

def greet(name="Class"):
    print(f"Hello world, Good morning {name} :)")

n = greet("Hitesh")         # This will print the greeting message and assign 'None' to 'n'
print(n)                    # Print the value of 'n' (which is 'None')
greet("Syed")               # This will print the greeting message using the provided name
greet()                     # This will print the default greeting message with the default name 'Class' as no arguements are passed
