# Assignment: Hands on Python Data Structures
# For Cognizant Externship – Python Fundamentals
# Jordan Wang
# 6/5/2025

# Task 1 - Working with Lists
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Original list:", fruits)

# adding a new fruit
fruits.append('fig')
print("After adding a fruit:", fruits)

# removing one fruit
fruits.remove('apple')
print("After removing a fruit:", fruits)

# reversing the list using slicing
reversed_fruits = fruits[::-1]
print("Reversed list:", reversed_fruits)

# Task 2 - Exploring Dictionaries
my_info = {
    "name": "Jordan Wang",
    "age": 21,
    "city": "Portsmouth"
}

# adding my favorite color
my_info["favorite color"] = "green"

# updating the city
my_info["city"] = "New York"

# printing the keys and values
print("\nKeys and values:")
for key, value in my_info.items():
    print(f"{key}: {value}")

# Task 3 - Using Tuples
favorites = ("Revenge of the Sith", "苦茶 - 心动版", "I'm not so sure")
print("\nFavorite things:", favorites)

# trying to modify a tuple
try:
    favorites[0] = "Interstellar"
except TypeError:
    print("Oops! Tuples cannot be changed.")

# printing the length of tuple
print("Length of tuple:", len(favorites))
