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
# MAGIC ## In this lesson you:
# MAGIC - Create a simple list
# MAGIC - Iterate over a list using a **`for`** expression
# MAGIC - Conditionally execute statements using **`if`**, **`elif`** and **`else`** expressions

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) C-Style For Loops
# MAGIC 
# MAGIC If you have any programming experience in other structured programming languages, you should be familair with **C-Style For Loops**
# MAGIC 
# MAGIC If not, a little history wont hurt...
# MAGIC 
# MAGIC The classic c-style for loop will look something like this:

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ```
# MAGIC for (i = 0; i < 10; i++) {
# MAGIC   print(i)
# MAGIC }
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC What is unique about this syntax is:
# MAGIC * **`i`** is a varaible that is initially set to **`0`**
# MAGIC * **`i`** is incremented by one (**`i++`**) after each iteration of the loop
# MAGIC * Incrementation and block-execution is repeated while the prescribed condition (**`i < 10`**) is true

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) For-In Loops
# MAGIC 
# MAGIC More modern programming languages such as Python, Scala, Java, and others, have abandoned if not deprecated this type of loop.
# MAGIC 
# MAGIC Instead they use a for-in methodology that amounts to executing a block of code once for every item in a list.
# MAGIC 
# MAGIC To see how this works, we need to first introduce a list - we will cover lists in more details in a latter section.

# COMMAND ----------

# MAGIC %md
# MAGIC Let's make a <a href="https://docs.python.org/3/library/stdtypes.html#list" target="_blank">list</a> of what everyone ate for breakfast this morning.
# MAGIC 
# MAGIC <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Scrambed_eggs.jpg/1280px-Scrambed_eggs.jpg" width="20%" height="10%">

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"] # Declare the list
print(breakfast_list)                            # Print the entire list

# COMMAND ----------

# MAGIC %md
# MAGIC There are a lot of different things we can do with a list such as:
# MAGIC * Iterating over a list
# MAGIC * Accessing specific elements of a list
# MAGIC * Slicing a list
# MAGIC * Appending to a list
# MAGIC * Removing items from a list
# MAGIC * Concatenating lists
# MAGIC * and so on...
# MAGIC 
# MAGIC For now, let's focus on iterating over a list and printing each individual item in the list:

# COMMAND ----------

for food in breakfast_list:
  print(food)
  
print("This is executed once because it is outside the for loop")

# COMMAND ----------

# MAGIC %md So how does one replicate a C-Style For Loop on a range of numbers in Python?
# MAGIC 
# MAGIC For that, we can use the <a href="https://docs.python.org/3/library/functions.html#func-range" target="_blank">range</a> function which produces an immutable collection of nubmers (a type of list).

# COMMAND ----------

for i in range(0, 5):
  print(i)

# COMMAND ----------

# MAGIC %md We will talk more about collections in a later section including lists, ranges, dictionaries, etc.
# MAGIC 
# MAGIC The key thing to remember here is that they are all iterable and the **`for-in`** expression allows us to iterate over them.

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Conditionals
# MAGIC 
# MAGIC Before exploring loops further, let's take a look at conditionals.
# MAGIC 
# MAGIC At the end of this lesson, we combine these two concepts so as to develop more complex constructs.

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC We don't always want to execute every line of code.
# MAGIC 
# MAGIC We can that process by employing **`if`**, **`elif`**, and **`else`** expressions.
# MAGIC 
# MAGIC We can see a few examples here:

# COMMAND ----------

food = "bacon"

if food == "eggs":
  print("Make scrambled eggs")
  
print("All done")

# COMMAND ----------

# MAGIC %md In the example above, line #5 is not executed.
# MAGIC 
# MAGIC Edit line #2 above and set the variable **`food`** to **`"eggs"`** and rerun the command.

# COMMAND ----------

# MAGIC %md Let's build on this example with an **`else`** expression...

# COMMAND ----------

food = "bacon"

if food == "eggs":
  print("Make scrambled eggs")
else:
  print(f"I don't know what to do with {food}")
  
print("All done")

# COMMAND ----------

# MAGIC %md And lastly, we can introduce the **`elif`** expression...

# COMMAND ----------

food = "bacon"

if food == "eggs":
  print("Make scrambled eggs")
elif food == "waffles":
  print("I need syrup for my waffles")
else:
  print(f"I don't know what to do with {food}")
  
print("All done")

# COMMAND ----------

# MAGIC %md
# MAGIC What if the expression needs to be more complex?
# MAGIC 
# MAGIC For example, if I need syrup with waffles or pancakes?
# MAGIC 
# MAGIC Each **`if`** and **`elif`** expression can get increasignly more complex by adding more conditional statements and combining them with various **`and`** &amp; **`or`** operators

# COMMAND ----------

food = "bacon"

if food == "eggs":
  print("Make scrambled eggs")
elif food == "waffles" or food == "pancakes":
  print(f"I need syrup for my {food}")
else:
  print(f"I don't know what to do with {food}")
  
print("All done")

# COMMAND ----------

# MAGIC %md
# MAGIC Besides compounding conditional statements, we can also nest **`if`**, **`elif`** and **`else`** expressions:

# COMMAND ----------

food = "bacon"

if food != "eggs":
  if food == "waffles" or food == "pancakes":
    print(f"I need syrup for my {food}")
  else:
    print(f"I don't know what to do with {food}")
else:
  print("Make scrambled eggs")
  
print("All done")

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Loops & Conditionals
# MAGIC 
# MAGIC Lastly, let's take a look at how we can combine these two constructs.
# MAGIC 
# MAGIC Before we do, let's review the contents of our breakfast list:

# COMMAND ----------

for food in breakfast_list:
  print(food)

# COMMAND ----------

# MAGIC %md Next we will iterate over that list and instead of printing each item, we can run through our conditionals instead

# COMMAND ----------

for food in breakfast_list:
  if food != "eggs":
    if food == "waffles" or food == "pancakes":
      print(f"I need syrup for my {food}")
    else:
      print(f"I don't know what to do with {food}")
  else:
    print("Make scrambled eggs")
  
print("All done")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>