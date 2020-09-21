# Databricks notebook source
# MAGIC 
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Methods, Functions, Packages
# MAGIC 
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br><br>
# MAGIC * Define and use functions to reuse, not repeat code
# MAGIC   * with and without arguments
# MAGIC   * with and without type hints
# MAGIC * Use assert() statements to "unit test" functions
# MAGIC * Call the `help()` function to learn about modules, functions, classes, and keywords
# MAGIC * Identify differences between functions and methods
# MAGIC * Import libraries
# MAGIC    

# COMMAND ----------

# MAGIC %md
# MAGIC ### Functions
# MAGIC 
# MAGIC In this lesson, we're going to see how we can use functions to make code reusable.
# MAGIC 
# MAGIC Let's start with a simple example:<br>
# MAGIC We know that we can use Python to do math. The modulo operator returns the remainder of a division. The code below returns 0 becuase 42 is even, so this division has no remainder.

# COMMAND ----------

42 % 2

# COMMAND ----------

# MAGIC %md
# MAGIC The code below will return 1 because it is odd. 

# COMMAND ----------

41 % 2

# COMMAND ----------

# MAGIC %md
# MAGIC If we want to determine whether a whole bunch of numbers are even or odd, we can package this same code into a **function**. 
# MAGIC 
# MAGIC A [function](https://www.w3schools.com/python/python_functions.asp) is created with the `def` keyword, followed by the name of the function, any parameters in parentheses, and a colon.

# COMMAND ----------

# General syntax
# def function_name(parameter_name):
#   block of code that is run every time function is called

# defining the function
def evenOdd(num):
  """Optional doc string explaining the function"""
  if num % 2 == 0:
     print("even")
  if num % 2 == 1:
     print("odd")
  else:
     print("UNKNOWN")

# execute the function by passing it a number
evenOdd(42)

# COMMAND ----------

# MAGIC %md
# MAGIC The one problem with printing the result is that if you assign it back to a variable, the variable is a None datatype (the output of print, versus the output of the function).
# MAGIC 
# MAGIC Instead, use the `return` keyword.

# COMMAND ----------

def evenOdd(num):
  """Returns the string even, odd, or unknown"""
  if num % 2 == 0:
    return "even"
  if num % 2 == 1:
    return "odd"
  else:
    return "UNKNOWN"

# execute the function by passing it a number
evenOdd(42)

# COMMAND ----------

# MAGIC %md
# MAGIC A best practice is to create a "unit" test to verify our function.<br>
# MAGIC An "AssertionError:" will only display if the function returns something that is not expected.

# COMMAND ----------

assert "odd" == evenOdd(101)
assert "even" == evenOdd(400)
assert "odd" == evenOdd(5)
assert "even" == evenOdd(2)
assert "even" == evenOdd(3780)
assert "odd" == evenOdd(78963)
assert "UNKNOWN" == evenOdd(1/3)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Help Function
# MAGIC 
# MAGIC The python `help()` function can display the additional information on modules, functions, classes, and keywords.

# COMMAND ----------

help(evenOdd)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Passing in Multiple Arguments<br>
# MAGIC Functions can accept more than one argument.<br>
# MAGIC Our function works well for English, now let's modify our function to make it easy to localize for different languages by accepting two arguments for the local version of even and odd.

# COMMAND ----------

def evenOddInt(num, even, odd):
  if num % 2 == 0:
    return even
  if num % 2 == 1:
    return odd
  else:
    return "UNKNOWN"

# execute the function by passing it a number
evenOddInt(42, "even", "odd")

# COMMAND ----------

# MAGIC %md
# MAGIC A new "unit" test can verify our function.<br>
# MAGIC If you know more than one language feel free edit the code below for a different version of even and odd.

# COMMAND ----------

assert "odd" == evenOddInt(101, "even", "odd")
assert "pair" == evenOddInt(400, "pair", "impair")
assert "περιττός" == evenOddInt(5, "zυγός", "περιττός")
assert "gerade" == evenOddInt(2, "gerade", "ungerade")
assert "genap" == evenOddInt(3780, "genap", "ganjil")
assert "liché" == evenOddInt(78963, "sudé", "liché")
assert "UNKNOWN" == evenOddInt(1/3, "xx", "xx")

# COMMAND ----------

# MAGIC %md
# MAGIC ###Type Hints<br>
# MAGIC Functions can be more strongly typed. Type hinting allows us to indicate the argument and return type.<br>
# MAGIC This is done by adding a colon space and data type to the parameter like below. <br>
# MAGIC `num: int`<br>
# MAGIC The return type is indicated with a hyphen, greater than and data type before the colon at the end of the signature line.<br>
# MAGIC `-> str:`

# COMMAND ----------

def evenOddInt(num: int, even: str, odd: str) -> str:
  if num % 2 == 0:
    return even
  if num % 2 == 1:
    return odd
  else:
    return "UNKNOWN"

# execute the function by passing it a number
evenOddInt(42, "even", "odd")

# COMMAND ----------

# MAGIC %md
# MAGIC We can improve our function further by adding default values for even and odd so these two arguments are not needed for English.

# COMMAND ----------

def evenOddInt(num: int, even: str = "even", odd: str = "odd") -> str:
  if num % 2 == 0:
    return even
  if num % 2 == 1:
    return odd
  else:
    return "UNKNOWN"

# execute the function by passing it a number
evenOddInt(42)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Methods
# MAGIC 
# MAGIC In Python a Method refers to a special kind of function that is applied to an object. <br>
# MAGIC Below we create a string object called name and print it.

# COMMAND ----------

name = 'Databricks'
print(name)

# COMMAND ----------

# MAGIC %md
# MAGIC Next we apply the upper() method to name.

# COMMAND ----------

print(name.upper())

# COMMAND ----------

# MAGIC %md
# MAGIC Certain methods expect an argument.<br>
# MAGIC Below we pass in `a` as an argument to the count() method and it returns the count of number of times `a` is found in the string 

# COMMAND ----------

print(name.count('a'))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Libraries
# MAGIC 
# MAGIC You can also use additional libraries when working with Python, such as [numpy](https://numpy.org/doc/stable/). Numpy is pre-installed on the Databricks runtime. You will need to first `import` numpy.

# COMMAND ----------

import numpy

numpy.sqrt(9)

# COMMAND ----------

help(numpy.sqrt)

# COMMAND ----------

# MAGIC %md
# MAGIC You can also change the name of the library when you import it, such as:

# COMMAND ----------

import numpy as np

np.sqrt(12)

# COMMAND ----------

# MAGIC %md
# MAGIC Or if you want to import every function from numpy, you can use the wildcard `*`

# COMMAND ----------

from numpy import *

sqrt(12)


# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>