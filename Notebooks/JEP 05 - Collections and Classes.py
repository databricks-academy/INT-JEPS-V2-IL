# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Collections & Classes
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br>
# MAGIC - Use list methods and syntax to append, remove, or replace elements of a list
# MAGIC - Compare ranges to lists
# MAGIC - Define dictionaries
# MAGIC - Use list and dictionary comprehensions to efficiently transform each element of each data structure
# MAGIC - Define classes and methods

# COMMAND ----------

# MAGIC %md
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Lists
# MAGIC 
# MAGIC We've seen that a list is an ordered sequence of items and that a **`for-in`** expression can be used to iterate over them.
# MAGIC 
# MAGIC The items may be of any type, though in practice you'll usually create lists where all of the values are of the same type.
# MAGIC 
# MAGIC You typically create a list by providing comma-separated values enclosed by square brackets.

# COMMAND ----------

breakfast_list = ["pancakes", "apple", "eggs"]
print(breakfast_list)

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Referencing Elements Of A List
# MAGIC Elemets of a list are referenced by appending a pair of square brackets (which surround an index number) to the end the list variable.
# MAGIC 
# MAGIC It's important to note that in Python, lists are zero-indexed meaning that the first item is referenced by index zero.

# COMMAND ----------

first_item = breakfast_list[0]
second_item = breakfast_list[1]
thrid_item = breakfast_list[2]
# non_existant_item = breakfast_list[3]

print(f"""The first item is "{first_item}".""")
print(f"""The second item is "{second_item}".""")
print(f"""The thrid item is "{thrid_item}".""")

# COMMAND ----------

# MAGIC %md When the length of a list is not know, you can employ the built in function **`len()`** to determine the length of the list and access the last item.
# MAGIC 
# MAGIC This is a common practice in many different programming languages.

# COMMAND ----------

list_length = len(breakfast_list)         # first determine the length of the list
last_item = breakfast_list[list_length-1] # minus one because we are a zero-based index

print(f"The list has {list_length} items in it.")
print(f"""The last item is "{last_item}".""")

# COMMAND ----------

# MAGIC %md But Python goes a long way to make hard things convenient. 
# MAGIC 
# MAGIC For example, you can access the last item in a list by counting backwards, as it where.

# COMMAND ----------

thrid_item_v2 = breakfast_list[-1]
second_item_v2 = breakfast_list[-2]
first_item_v2 = breakfast_list[-3]


print(f"""From the end, the thrid item is "{thrid_item_v2}".""")
print(f"""From the end, the second item is "{second_item_v2}".""")
print(f"""From the end, the first item is "{first_item_v2}".""")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Altering Lists
# MAGIC Lists are _mutable_ collections, meaning that we can change the contents of the list with operations that update, append to, and delete the elements of a list.

# COMMAND ----------

breakfast_list = ["pancakes", "apple", "eggs"]
print(f"Before the update: {breakfast_list}")

# Replace pancakes with waffles
breakfast_list[0] = "waffles" 

print(f"After the update:  {breakfast_list}")

# COMMAND ----------

# MAGIC %md
# MAGIC Because a list is an object, it also supports additional methods such as the **`append()`** method:

# COMMAND ----------

breakfast_list = ["pancakes", "apple", "eggs"]
print(f"Before the append: {breakfast_list}")

# Append an item to the end of the list
breakfast_list.append("oatmeal")

print(f"After the append:  {breakfast_list}")

# COMMAND ----------

# MAGIC %md The **`del`** keyword allows you to remove an item from a list if you know it's specific index.

# COMMAND ----------

breakfast_list = ["pancakes", "apple", "eggs"]
print(f"Before the delete: {breakfast_list}")

# Remove the eggs (the last item in the list) to go vegan
del breakfast_list[2]
# del breakfast_list[-1]

print(f"After the delete:  {breakfast_list}")

# COMMAND ----------

# MAGIC %md
# MAGIC Or you can use another of the list's methods, the **`remove()`** method.

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "apple"]
print(f"Before the remove: {breakfast_list}")

# Remove the eggs, wherever it may be
breakfast_list.remove("eggs")

print(f"After the remove:  {breakfast_list}")

# COMMAND ----------

# MAGIC %md
# MAGIC #### List Contains Value?
# MAGIC 
# MAGIC You can test for the presence or absence of an item in a list using the **`in`** and **`not in`** operations, respectively.

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "apple"]

if "apple" in breakfast_list:
  print("You had an apple for breakfast.")

if "bacon" not in breakfast_list:
  print("You did not have bacon for breakfast.")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Built-in Functions for Lists
# MAGIC 
# MAGIC Python has built-in functions for determining the length, minimum, and maximum of a collection.
# MAGIC 
# MAGIC We already saw the **`len()`** function, but we can also use the **`min`** and **`max`** functions on a list.
# MAGIC 
# MAGIC Caution: What these functions return depend largely on the contents of the list.

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "apple", "chicken"]

item_count = len(breakfast_list)
item_min = min(breakfast_list)
item_max = max(breakfast_list)

print(f"You had {item_count} items for breakfast")
print(f"""The "min" value in the list is "{item_min}".""")
print(f"""The "max" value in the list is "{item_max}".""")

# COMMAND ----------

# MAGIC %md The **`max`** and **`min`** functions make more sense with a list of numbers.

# COMMAND ----------

some_numbers = [1, 32, 22, 54, 21, 32, 30]

item_count = len(some_numbers)
min_value = min(some_numbers)
max_value = max(some_numbers)

print(f"You had {item_count} items for breakfast")
print(f"""The "min" value in the list is {min_value}.""")
print(f"""The "max" value in the list is {max_value}.""")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Ranges
# MAGIC 
# MAGIC A _range_ represents an _immutable_ sequence of numbers.
# MAGIC 
# MAGIC It is commonly used for looping through a sequence of numbers with a **`for-in`** expression.
# MAGIC 
# MAGIC We saw this in action in the previous lesson.

# COMMAND ----------

# Note that a range includes the start value and excludes the stop value

# A range from 1 up to but not including 5 (exclusive)
for i in range(1, 5):
  print(f"This is item #{i}")

# COMMAND ----------

# MAGIC %md But the **`range()`** function has a lot more versatility to it than just that...
# MAGIC 
# MAGIC Most loops start with zero, so the one-arg variant makes that assumption for you

# COMMAND ----------

# A range from 0 to 5 exclusive
for i in range(5):
  print(f"This is item #{i}")

# COMMAND ----------

# MAGIC %md
# MAGIC We can also skip numbers by specifying the third parameter, **`step`** .

# COMMAND ----------

# Only even numbers between 0 & 10 exclusive
for i in range(0, 10, 2):
  print(f"This is item #{i}")

# COMMAND ----------

# MAGIC %md And we can count backwards just as easily

# COMMAND ----------

# Every 3rd number, counting backwards, starting with 12
for i in range(12, 0, -3):
  print(f"This is item #{i}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) List Comprehensions
# MAGIC 
# MAGIC A common task is to take a collection of values and create a new collection that is a transformation of the original values.
# MAGIC 
# MAGIC You can do this explicitly with a **`for-in`** expression.

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "apple", "chicken"]
print(f"Before transformation: {breakfast_list}")

caps_list = []  # Create an empty list
      
for item in breakfast_list:
  caps_list.append(item.capitalize())
  
print(f"After transformation:  {caps_list}")

# COMMAND ----------

# MAGIC %md
# MAGIC A more compact and efficient technique to accomplish the same thing is a _list comprehension_. 
# MAGIC 
# MAGIC The following is equivalent to the example above:

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "apple", "chicken"]
print(f"Before transformation: {breakfast_list}")

comp_caps_list = [item.capitalize() for item in breakfast_list]

print(f"After transformation:  {comp_caps_list}")

# COMMAND ----------

# MAGIC %md
# MAGIC A comprehension can also include a filter expression to process only the items that match a condition.

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "apple", "chicken"]
print(f"Before filtering: {breakfast_list}")

comp_caps_list = [item.capitalize() for item in breakfast_list]

short_list = [item.upper() for item in breakfast_list if len(item) >= 7]
print(f"After filtering:  {short_list}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Dictionaries
# MAGIC 
# MAGIC A Python <a href="https://docs.python.org/3/library/stdtypes.html#mapping-types-dict" target="_blank">dictionary</a> is a mutable collection of elements where each element is a key-value pair.
# MAGIC 
# MAGIC * All of the keys in a dictionary must be unique.
# MAGIC * The keys must be of an immutable type, typically strings or integers.
# MAGIC * The values may be mutable and of any type.
# MAGIC * Prior to Python 3.6, dictionaries are _unordered_ collections. The order of elements can change as you add and delete elements.
# MAGIC * In Python 3.6 and later, dictionaries are _ordered_ collections, which means that they keep their elements in the same order in which they were originally inserted.
# MAGIC 
# MAGIC You can create a dictionary like this:

# COMMAND ----------

breakfast_dict = {
  "eggs": 160,
  "apple": 100,
  "pancakes": 400,
  "waffles": 300,
}
print(breakfast_dict)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Accessing Dictionary Values
# MAGIC 
# MAGIC Once created, you can retrieve the value corresponding to a given key like this:

# COMMAND ----------

choice = "apple"
apple_calories = breakfast_dict[choice]

print(f"Your {choice} had {apple_calories} calories.")

# COMMAND ----------

# MAGIC %md
# MAGIC However, if the dictionary does not contain an element with that key, Python raises a `KeyError`.

# COMMAND ----------

# Uncomment the following line and run this cell
# breakfast_dict["oatmeal"]

# COMMAND ----------

# MAGIC %md
# MAGIC Alternatively, you can use the dictionary **`get()`** method.
# MAGIC 
# MAGIC This returns the value for the given key if present.
# MAGIC 
# MAGIC If the key is not present in the dictionary, **`get()`** returns either the specified default value or **`None`**.

# COMMAND ----------

choiceA = "oatmeal"
caloriesA = breakfast_dict.get(choiceA, -1)
print(f"Your {choiceA} had {caloriesA} calories.")

choiceB = "waffles"
caloriesB = breakfast_dict.get(choiceB, -1)
print(f"Your {choiceB} had {caloriesB} calories.")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Dictionary Contains Key?
# MAGIC 
# MAGIC You can test for the presence or absence of a key in a dictionary using the **`in`** and **`not in`** operators, respectively.

# COMMAND ----------

print(f"Original dictionary: {breakfast_dict}")

choice = "bacon"

if choice in breakfast_dict:
  print(f"{choice.upperCase()} has {breakfast_dict[choice]} calories")
  
elif choice not in breakfast_dict:
  print(f"""I couldn't find "{choice}" in the dictionary""")
  
else:
  print("This logically cannot happen :-)")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Updating Dictionaries
# MAGIC 
# MAGIC Because a dictionary is a mutable collection, we can change its contents with operations like inserting, updating, and deleting elements.

# COMMAND ----------

breakfast_dict = {"eggs": 160, "apple": 100, "pancakes": 400, "waffles": 300,}
print(f"Before insert: {breakfast_dict}")

# Insert orange juice with 110 calories
breakfast_dict["orange juice"] = 110
print(f"After insert:  {breakfast_dict}")

# COMMAND ----------

breakfast_dict = {"eggs": 160, "apple": 100, "pancakes": 400, "waffles": 300,}
print(f"Before update: {breakfast_dict}")

# Update the calorie count for pancakes
breakfast_dict["pancakes"] = 350
print(f"After update:  {breakfast_dict}")

# COMMAND ----------

breakfast_dict = {"eggs": 160, "apple": 100, "pancakes": 400, "waffles": 300,}
print(f"Before delete: {breakfast_dict}")

# Delete the waffles
del breakfast_dict["waffles"]
print(f"After delete:  {breakfast_dict}")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Iterating Over the Elements of a Dictionary
# MAGIC 
# MAGIC You can use the **`for-in`** expression to iterate over the keys of a dictionary like this:

# COMMAND ----------

breakfast_dict = {"eggs": 160, "apple": 100, "pancakes": 400, "waffles": 300,}
print("Food          Calories")

for food in breakfast_dict:
  print(f"{food:13} {breakfast_dict[food]}")

# COMMAND ----------

# MAGIC %md
# MAGIC Alternatively, you can unpack the key-value pairs while iterating over a dictionary using the **`items()`** method:

# COMMAND ----------

print("Food          Calories")
for key_value in breakfast_dict.items():
  key = key_value[0]
  value = key_value[1]
  print(f"{key:13} {value}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Tuples
# MAGIC 
# MAGIC The method **`items()`** is returning a new data type called **`dict_items`** which is a sub-type of **`tuple`**.
# MAGIC 
# MAGIC We will elaborate on sub-types a bit later, but a **`tuple`** is an immutable sequence of values, much like a list.
# MAGIC 
# MAGIC As seen above, elements of a tuple are accessed like an array.
# MAGIC 
# MAGIC In this case, index **`0`** was the key and **`1`** was the value.
# MAGIC 
# MAGIC Here are some more examples...

# COMMAND ----------

dict_type = type(breakfast_dict.items())                # What type is it exactly?
print(f"breakfast_dict.items() is of type {dict_type}") # Print the result

my_tuple = ("apple", 100)                               # Create your own tuple
tuple_type = type(my_tuple)                             # What type is it exactly?
print(f"my_tuple is of type {tuple_type}")              # Print the result

first_item = my_tuple[0]                                # Access the first element of the tuple
second_item = my_tuple[1]                               # Access the second element of the tuple

print()                                                 # Print a blank line
print(f"First item:  {first_item}")                     # Print the first item
print(f"Second item: {second_item}")                    # Print the second item

# COMMAND ----------

# MAGIC %md Tuples can also be "unpacked" as seen here:

# COMMAND ----------

my_tuple = ("Smith", 39)    # Create your own tuple
last_name, age = my_tuple   # Unpack the tuple

print(f"Name: {last_name}") # Print the last name
print(f"Age:  {age}")       # Print the age

# COMMAND ----------

# MAGIC %md
# MAGIC Back to our dictionary and our **`dict_items`**.
# MAGIC 
# MAGIC As a tuple, we can also unpack what was previously in the **`key_value`** variable:

# COMMAND ----------

print("Food          Calories")
for food, calories in breakfast_dict.items():
  print(f"{food:13} {calories}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Classes
# MAGIC 
# MAGIC A [_class_](https://www.w3schools.com/python/python_classes.asp) is a custom type that you can define that is in essence a custom data structure.
# MAGIC 
# MAGIC * The class definition itself serves as a "template" that you can use to create any number of individual _objects_ (also known as _instances_ in object oriented programming).
# MAGIC * These objects will have the same characteristics and behaviors, but their own data values (also known as _attributes_ or _properties_ in OOP).
# MAGIC 
# MAGIC As an analogy, you can think of a class as though it were a blueprint for a house.
# MAGIC 
# MAGIC * The blueprint isn't a house itself, but it describes how to build a house.
# MAGIC * From one blueprint (class), a developer could build any number of houses (objects/instances).
# MAGIC * Each house would have the same floorplan, but each house could have its own unique paint colors, floor tiling, etc. (attributes/properties).
# MAGIC 
# MAGIC NOTE: We've already encountered and used classes in this course. 
# MAGIC 
# MAGIC For example, Python has a built-in **`str`** class that defines the capabilities of all strings. 
# MAGIC 
# MAGIC Similarly, **`list`** and **`dict`** are built-in classes defining the capabilities of lists and dictionaries, respectively. 
# MAGIC 
# MAGIC You can see that for yourself by using the **`help()`** function on these types:

# COMMAND ----------

help(dict)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Class Methods
# MAGIC 
# MAGIC A class definition usually consists of one or more function definitions, which are also called _methods_.
# MAGIC 
# MAGIC * These methods are automatically associated with each object created using the class.
# MAGIC * When you invoke a method, Python automatically passes a reference to the associated object as the first argument, followed by any other arguments that you passed explicitly.
# MAGIC * By convention, `self` is used as the parameter name for the object reference.
# MAGIC 
# MAGIC Here's a simple example of a class definition and its use:

# COMMAND ----------

class Thing:
  def greet(self, greeting="Hello!"):
    print(f'{self} says, "{greeting}"')

thing1 = Thing()  # Create an instance of Thing
thing2 = Thing()  # Create another Thing

thing1.greet()                # Call the greet() method on thing1
thing2.greet("Guten Tag!")    # Call the greet() method on thing2

# COMMAND ----------

# MAGIC %md
# MAGIC Wow, that's ugly. 
# MAGIC 
# MAGIC We can see that the value of `self` is different for `thing1` and `thing2` because each is a separate instance of `Thing`. 
# MAGIC 
# MAGIC But the string representation of `self` is not informative to us as programmers. 
# MAGIC 
# MAGIC To make things more interesting and useful, we need to define some class properties.

# COMMAND ----------

# MAGIC %md
# MAGIC #### Class Properties and the Constructor Method
# MAGIC 
# MAGIC Class properties are usually defined in a special method called a _constructor_.
# MAGIC 
# MAGIC * The constructor method **must** be named `__init__()`.
# MAGIC * Python calls the constructor method automatically whenever you create an instance of the class.
# MAGIC * The purpose of the constructor is to initialize the newly created instance, most typically by setting the initial values of the object's properties.
# MAGIC 
# MAGIC The following is an example of a more interesting class that includes a constructor method that sets two properties and two additional methods:

# COMMAND ----------

class Person:
  
  # Defining the class constructor method
  def __init__(self, first_name, last_name):
    # Here we create the properties on self with the values provided in the constructor
    self.first_name = first_name
    self.last_name = last_name
  
  # Defining other class methods
  def greet(self, greeting="Hello!"):
    print(f'{self.first_name} says, "{greeting}"')
    
  def full_name(self):
    return self.last_name + ", " + self.first_name

person1 = Person("Ming-Na", "Wen")
person2 = Person(first_name="Anil", last_name="Kapoor")
person3 = Person("Walter", "Carlos")

person1.greet()
person2.greet("Hi!")

print()

print(f"person3's current name: {person3.full_name()}")
person3.first_name = "Wendy"  # You can change the value of object properties
print(f"person3's updated name: {person3.full_name()}")


# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>