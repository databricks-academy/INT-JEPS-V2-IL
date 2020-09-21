# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Conditionals and Loops
# MAGIC 
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br><br>
# MAGIC 
# MAGIC  - Define syntax for writing lists and accessing their elements
# MAGIC  - Apply basic control flow statements to write programs that:
# MAGIC      - Repeat an action
# MAGIC      - Apply a function to any item on a list
# MAGIC      - Use conditional statements to how a program will execute 

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1) List
# MAGIC 
# MAGIC Let's make a [list](https://www.w3schools.com/python/python_lists.asp) of what everyone ate for breakfast this morning.
# MAGIC 
# MAGIC <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Scrambed_eggs.jpg/1280px-Scrambed_eggs.jpg" width="20%" height="10%">

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]

# COMMAND ----------

# MAGIC %md
# MAGIC Let's get the first breakfast element from this list.
# MAGIC 
# MAGIC **Note:** Everything in Python is 0-indexed, so the first element is at position 0.

# COMMAND ----------

breakfast_list[0]

# COMMAND ----------

# MAGIC %md
# MAGIC Let's get the last breakfast item from this list.

# COMMAND ----------

breakfast_list[-1]

# COMMAND ----------

# MAGIC %md
# MAGIC What if I want the second breakfast item and onwards?

# COMMAND ----------

breakfast_list[1:]

# COMMAND ----------

# MAGIC %md
# MAGIC Let's add an element to our list.

# COMMAND ----------

breakfast_list += ["apple"]

# The += is a short cut for
# breakfast_list = breakfast_list + ["apple"]

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2) For Loops
# MAGIC 
# MAGIC What if we wanted to print every breakfast we had this morning?
# MAGIC 
# MAGIC Loops are a way to repeat a block of code while iterating over a sequence (["for-loop"](https://www.w3schools.com/python/python_for_loops.asp)). Notice how in the code below the syntax is:
# MAGIC 
# MAGIC ```
# MAGIC  for element in list:
# MAGIC    do something
# MAGIC ```
# MAGIC 
# MAGIC Anything you want executed multiple times needs to be indented inside the for loop. `food` is a temporary variable we define below, but you can call it anything you like.

# COMMAND ----------

for food in breakfast_list:
  print(food)
  
print("This is executed once because it is outside the for loop")

# COMMAND ----------

# MAGIC %md
# MAGIC You can also get it to print out the index of the element in the list too, by using `enumerate`.

# COMMAND ----------

for i, food in enumerate(breakfast_list):
  print(i, food)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3) Conditionals
# MAGIC 
# MAGIC Sometimes, depending on certain conditions, we don't always want to execute every line of code. We can control this through using the `if`, `elif`, and `else` [conditionals](https://www.w3schools.com/python/python_conditions.asp).
# MAGIC 
# MAGIC You are not required to have elif/else statements following an if statement.

# COMMAND ----------

if food == "eggs":
  print("Make scrambled eggs")
elif food == "waffles":
  print("I want maple syrup on my waffles")
else:
  print(food)

# COMMAND ----------

# MAGIC %md
# MAGIC You can also nest these if/elif/else statements, or combine them with `or` & `and`

# COMMAND ----------

if food != "eggs":
  if (food == "waffles") or (food == "pancakes"):
    print("I want maple syrup on my waffles")
  else:
    print("It must be an apple")
else:
  print(food)

# COMMAND ----------

# MAGIC %md
# MAGIC We can put these if/elif/else statements inside of a for loop.

# COMMAND ----------

for food in breakfast_list:
  if food != "eggs":
    if (food == "waffles") or (food == "pancakes"):
      print("I want maple syrup on my waffles")
    else:
      print("It must be an apple")
  else:
    print(food)


# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>