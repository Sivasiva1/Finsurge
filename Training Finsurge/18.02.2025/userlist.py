
numbers = [1, 2, 3, 4, 5]
print(numbers)  

# A list of mixed data types
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)  

fruits = ["apple", "banana", "cherry"]
# Modifying an element by index
fruits[1] = "blueberry"
print(fruits)  
# Appending an element
fruits.append("orange")
print(fruits) 

# Inserting an element at a specific index
fruits.insert(1, "mango")
print(fruits)  

# Removing an element by value
fruits.remove("blueberry") 
print(fruits)  

# Removing an element by index
fruits.pop(2)
print(fruits)  

a = ["python","c","java","kotlin","rust"]

print(a[1:3]) 
print(a[-4:-2]) 

numbers.sort()
print(numbers)  
numbers.sort(reverse=True)
print(numbers)  
(numbers.reverse())
print(numbers)  
print(numbers.index(3))

print(numbers.count(3))
copy = numbers.copy()
print(copy)
numbers.extend({1,2})
print(numbers) 

print(len(fruits))  


print(3 in numbers)  # Output: True

# Concatenating two lists
combined = numbers + fruits
print(combined)  

# Repeating elements in a list
repeated = [1] * 5
print(repeated)  
