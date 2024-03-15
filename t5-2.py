# Define a list containing a mix of integers and strings
my_list = [1, 'apple', 3, 'banana', '4', 5]

# Use map() function along with lambda to check if every element is an integer or string
result = all(map(lambda x: isinstance(x, (int, str)), my_list))

if result:
    print("Every element in the list is an integer or a string.")
else:
    print("There are elements in the list that are not integers or strings.")
