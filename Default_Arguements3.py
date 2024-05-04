# Define a function 'greet' with parameters 'type' and 'name' with default value "Friend :)"


def greet(type, name="Friend :)"):
    print(type, name)

# function call with no arguements
greet()                                 # Generate Error !!!
# function call with arguements
greet('Good Morning ', 'Syed')          
# by default it will take : type='Syed'
greet("Syed")                       
# Call greet with 'name'='Syed'
greet(name="Syed")                      # Generate Error !!!         
greet(type="Hi ! ")                     # This will print the provided value for 'type' and the default value for 'name'
