# Databricks notebook source
# MAGIC 
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Fizz Buzz Lab
# MAGIC  
# MAGIC * If the number is divisible by 3 print `Fizz`. If the number is divisible by 5 print `Buzz`. If it is divisible by both 3 and 5 print `FizzBuzz` on one line.
# MAGIC * If the number is not divisible by 3 or 5, just print the number.
# MAGIC 
# MAGIC HINT: Look at the [modulo (`%`) operator](https://www.educative.io/edpresso/what-is-a-modulo-operator-in-python).

# COMMAND ----------

# ANSWER

num = 10

if (num % 5 == 0) and (num % 3 == 0):
  print("FizzBuzz")
elif num % 5 == 0:
  print("Buzz")
elif num % 3 == 0:
  print("Fizz")
else:
  print(num)

# COMMAND ----------

# MAGIC %md
# MAGIC What happens if you pass in a string here? It will error! Add in a check so that if the input is not numeric (either `float` or `int`) print `Not a number`.
# MAGIC 
# MAGIC HINT: Use [type()](https://www.w3schools.com/python/ref_func_type.asp).

# COMMAND ----------

# ANSWER
num = "hello"

if type(num) == int or type(num) == float:
  if (num % 5 == 0) and (num % 3 == 0):
    print("FizzBuzz")
  elif num % 5 == 0:
    print("Buzz")
  elif num % 3 == 0:
    print("Fizz")
  else:
    print(num)
else:
  print("Not a number")

# COMMAND ----------

# MAGIC %md
# MAGIC But what if the argument passed to the function were a list of values? Write a function that accepts a list of inputs, and applies the function to each element in the list.
# MAGIC 
# MAGIC A sample list is provided below to test your function.

# COMMAND ----------

num_list = [1, 1.56, 3, 5, 15, 30, 50, 77, "Hello"]

# COMMAND ----------

# ANSWER
for num in num_list:
  if type(num) == int or type(num) == float:
    if (num % 5 == 0) and (num % 3 == 0):
      print("FizzBuzz")
    elif num % 5 == 0:
      print("Buzz")
    elif num % 3 == 0:
      print("Fizz")
    else:
      print(num)
  else:
    print("Not a number")


# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>