# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Methods, Functions &amp; Packages
# MAGIC 
# MAGIC ## In this lesson you:
# MAGIC * Define and use functions
# MAGIC   * with and without arguments
# MAGIC   * with and without type hints
# MAGIC * Use **`assert`** statements to "unit test" functions
# MAGIC * Employ the **`help()`** function to learn about modules, functions, classes, and keywords
# MAGIC * Identify differences between functions and methods
# MAGIC * Import libraries
# MAGIC    

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Functions
# MAGIC 
# MAGIC In this lesson, we're going to see how we can use functions to make code reusable.
# MAGIC 
# MAGIC Let's start with a simple example:
# MAGIC 
# MAGIC We know that we can use Python to do math.
# MAGIC 
# MAGIC The modulo operator returns the remainder of a division.
# MAGIC 
# MAGIC The code below returns 0 becuase 42 is even, so this division has no remainder.

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
# MAGIC A <a href="https://docs.python.org/3/tutorial/controlflow.html#defining-functions" target="_blank">function</a> is created with the **`def`** keyword, followed by the name of the function, any parameters (variables) in parentheses, and a colon.

# COMMAND ----------

# General syntax
# def function_name(parameter_name):
#   """Optional doc string explaining the function"""
#   block of code that is run every time function is called

# defining the function
def printEvenOdd(num):
  """Prints the string "even", "odd", or "UNKNOWN"."""
  
  if num % 2 == 0:
     print("even")
  elif num % 2 == 1:
     print("odd")
  else:
     print("UNKNOWN")

# execute the function by passing it a number
printEvenOdd(42)

# COMMAND ----------

# MAGIC %md
# MAGIC The one problem with printing the result is that if you assign the function's result back to a variable, the value is **`None`**.
# MAGIC 
# MAGIC As we see here:

# COMMAND ----------

result = printEvenOdd(42)
print(f"The result is: {result}")

# COMMAND ----------

# MAGIC %md To make the function more useful, we can instead introduce a **`return`** expression.
# MAGIC 
# MAGIC This directs the method to stop execution of the method and to "return" the specified value

# COMMAND ----------

def evenOdd(num):
  """Returns the string "even", "odd", or "UNKNOWN"."""
  
  if num % 2 == 0:
    return "even"
  elif num % 2 == 1:
    return "odd"
  else:
    return "UNKNOWN"

# execute the function by passing it a number
result = evenOdd(42)
print(f"The result is: {result}")

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Testing Functions
# MAGIC 
# MAGIC When developing functions like this, it's is best practice to test them with various inputs, expecting different outputs.
# MAGIC 
# MAGIC This is commonly refered to as **Unit Testing** - testing a "unit" of code.
# MAGIC 
# MAGIC To do that, we can employ the **`assert`** expression as seen in the previous lesson.
# MAGIC 
# MAGIC If a test fails, execution will stop and an alert (**AssertionError**) will be rended to the console.
# MAGIC 
# MAGIC To see this in action, alter the code below so that the various assertions fail.

# COMMAND ----------

result = evenOdd(101)
assert "odd" == result, f"Expected odd, found {result}"
print("Test #1 passed")

result = evenOdd(400)
assert "even" == result, f"Expected even, found {result}"
print("Test #2 passed")

result = evenOdd(5)
assert "odd" == result, f"Expected odd, found {result}"
print("Test #3 passed")

result = evenOdd(2)
assert "even" == result, f"Expected even, found {result}"
print("Test #4 passed")

result = evenOdd(3780) 
assert "even" == result, f"Expected even, found {result}"
print("Test #5 passed")

result = evenOdd(78963)
assert "odd" == result, f"Expected odd, found {result}"
print("Test #6 passed")

# A slighly more robust version:
value = 1/3
expected = "UNKNOWN"
result = evenOdd(value)
assert expected == result, f"Expected {expected}, found {result} for {value}"
print("Test #7 passed")

# COMMAND ----------

# MAGIC %md The secret to unit testing is two fold:
# MAGIC * Write your code so that it is testable - a whole other topic in and of itself.
# MAGIC * Provide as much information as reasonable in the assertion - in most cases you will be looking at a report of failures and not the code itself.

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) The Help Functions
# MAGIC 
# MAGIC The <a href="https://docs.python.org/3/library/functions.html#help" target="_blank">help()</a> function can display additional information the functions you develop.
# MAGIC 
# MAGIC It relies in large part on the documentation string provided at the top of a function, for example:

# COMMAND ----------

help(evenOdd)

# COMMAND ----------

# MAGIC %md A properly documented function will include information on:
# MAGIC * The parameters
# MAGIC * The parameter's data types
# MAGIC * The return value
# MAGIC * The return value's data type
# MAGIC * A one-line description
# MAGIC * Possibly a more verbose description
# MAGIC * Example usage
# MAGIC * and more...

# COMMAND ----------

def documentedEvenOdd(num):
  """
  Returns the string "even", "odd", or "UNKNOWN".
  
  This would be a more verbose description of 
  what this function might do and could drone 
  one for quite a while
  
  Args:
    num (int): The number to be tested as even or odd
    
  Returns:
    str: "even" if the number is even, "odd" if the number is odd or "UNKNOWN"
    
  Examples:
    evenOdd(32)
    evenOdd(13)
  """
    
  if num % 2 == 0:
    return "even"
  elif num % 2 == 1:
    return "odd"
  else:
    return "UNKNOWN"

# COMMAND ----------

help(documentedEvenOdd)

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Functions Arguments
# MAGIC 
# MAGIC Obviously, functions can accept more than one argument.
# MAGIC 
# MAGIC Our function takes only one argument and works well for English.
# MAGIC 
# MAGIC Now let's modify our function to make it easy to localize for different languages by accepting two additional arguments for the local version of "even" and "odd".

# COMMAND ----------

def evenOddInt(num, evenLabel, oddLabel):
  if num % 2 == 0:
    return evenLabel
  elif num % 2 == 1:
    return oddLabel
  else:
    return "UNKNOWN"

# execute the function by passing it a number and two labels
print( evenOddInt(41, "even", "odd") )
print( evenOddInt(42, "even", "odd") )

# COMMAND ----------

# MAGIC %md
# MAGIC A new set of unit tests can verify that our new function works as expected.
# MAGIC 
# MAGIC And because a unit tests is just more code, we can wrap that up in a test-function as well.

# COMMAND ----------

def testEvenOddInt(value, evenLabel, oddLabel, expected):
  result = evenOddInt(value, evenLabel, oddLabel)
  
  assert expected == result, f"Expected {expected}, found {result} for {value}"
  print(f"Test {value}/{evenLabel}/{oddLabel} passed")

# COMMAND ----------

# MAGIC %md With the test functiond defined, testing many permutations gets even easier.

# COMMAND ----------

# Test our "UNKNOWN" case
testEvenOddInt(1/3, "what", "ever", "UNKNOWN")

# Test around zero
testEvenOddInt(-1, "even", "odd", "odd")
testEvenOddInt(0, "even", "odd", "even")
testEvenOddInt(1, "even", "odd", "odd")
testEvenOddInt(2, "even", "odd", "even")
testEvenOddInt(3, "even", "odd", "odd")

# Additional tests focused on the even/odd labels
testEvenOddInt(400, "pair", "impair", "pair")
testEvenOddInt(5, "zυγός", "περιττός", "περιττός")
testEvenOddInt(2, "gerade", "ungerade", "gerade")
testEvenOddInt(3780, "genap", "ganjil", "genap")
testEvenOddInt(78963, "sudé", "liché", "liché")

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Type Hints
# MAGIC 
# MAGIC Type hinting allows us to indicate the argument and return type of a function.
# MAGIC 
# MAGIC This is done by appending a colon and data type to the end of each parameter.
# MAGIC * For example **`num`** would become **`num:int`**.
# MAGIC 
# MAGIC The return type is documented by adding an "arrow" and data type to the end of a function.
# MAGIC  * For example, **`def someFunc():`** would become **`def someFunc() -> str:`** to indicate that it returns a string.
# MAGIC  
# MAGIC We can see below how our **`evenOddInt()`** function would look with type parameters.

# COMMAND ----------

def evenOddInt(num:int, evenLabel:str, oddLabel:str) -> str:
  if num % 2 == 0:
    return evenLabel
  elif num % 2 == 1:
    return oddLabel
  else:
    return "UNKNOWN"

# execute the function by passing it a number
evenOddInt(42, "even", "odd")

# COMMAND ----------

# MAGIC %md
# MAGIC But there is a catch!
# MAGIC 
# MAGIC Python is dynamically-typed language, so even if you decalre a parameter to be a string, there is little to nothing stoping you from passing other data types to that function.
# MAGIC 
# MAGIC For example....

# COMMAND ----------

resultA = evenOddInt(12, "EVEN", "ODD")
print(f"""The result is "{resultA}" and of type {type(resultA)}""")

resultB = evenOddInt(13, True, False)
print(f"""The result is "{resultB}" and of type {type(resultB)}""")

resultC = evenOddInt(17, 1, 0)
print(f"""The result is "{resultC}" and of type {type(resultC)}""")

# COMMAND ----------

# MAGIC %md
# MAGIC **Question:** If type hints are not inforced in Python, then why provide them?

# COMMAND ----------

# MAGIC %md
# MAGIC **Question:** If type hints won't stop callers of my function from passing the wrong value, what can I do?<br/>
# MAGIC Hint: Consider the following version of our even/odd method:

# COMMAND ----------

def evenOddInt(num:int, evenLabel:str, oddLabel:str) -> str:
  # What can one do to protect a function from bad input?
  
  if num % 2 == 0:
    return evenLabel
  elif num % 2 == 1:
    return oddLabel
  else:
    return "UNKNOWN"

# This should always work
print( evenOddInt(12, "EVEN", "ODD") )

# But can we stop this code from executing?
print( evenOddInt(13, True, False) )
print( evenOddInt(17, 1, 0) )

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Default Values
# MAGIC 
# MAGIC Assuming 90% of the callers of this function expect to use English, requiring them to specify the **`evenLabel`** and **`oddLabel`** everytime is cumbersome.
# MAGIC 
# MAGIC We can improve our function further by adding default values for even and odd so these two arguments are not needed for English.

# COMMAND ----------

def evenOddInt(num: int, evenLabel:str = "even", oddLabel:str = "odd") -> str:
  if num % 2 == 0:
    return evenLabel
  elif num % 2 == 1:
    return oddLabel
  else:
    return "UNKNOWN"

# execute the function by passing it a number
print(evenOddInt(42))
print(evenOddInt(32, "EVEN", "ODD"))
print(evenOddInt(65, "pair", "impair"))

# COMMAND ----------

# MAGIC %md
# MAGIC Of course we now need to update our unit tests to account for the fact that we now have default values.
# MAGIC 
# MAGIC But we can save that for a later date.

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Methods
# MAGIC 
# MAGIC In Python, a Method refers to a special kind of function that is applied to an object.
# MAGIC 
# MAGIC We will talk more about objects and classes in a later lesson, but for now, consdier that:
# MAGIC * A function only operates on the parameters passed to it (generally).
# MAGIC * A method has parameters, but it also has additional state as defined by the object it is attached to.
# MAGIC 
# MAGIC For example, a string (**`str`**) is a type of object:

# COMMAND ----------

name = 'Databricks'
print(name)

# COMMAND ----------

# MAGIC %md
# MAGIC The string object has a method called **`upper()`** which we can invoke.

# COMMAND ----------

result = name.upper()
print(result)

# COMMAND ----------

# MAGIC %md Note that the original object was not modified, but that the **`upper()`** method used the string to produce a new string.

# COMMAND ----------

print(name)

# COMMAND ----------

# MAGIC %md
# MAGIC As with functions, certain methods expect an argument.
# MAGIC 
# MAGIC The string class also has a **`count(str)`** method that returns the total number of times the specified substring is found.
# MAGIC 
# MAGIC In this case, let's count how many times we find the letter **`a`**.

# COMMAND ----------

total = name.count('a')
print(f"I found {total} instances of that substring")

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Libraries
# MAGIC 
# MAGIC Python includes a rich set of libraries developed by an every going community of software develoeprs.
# MAGIC 
# MAGIC Some libraries are included with Python by default.
# MAGIC 
# MAGIC Others are external libraries that have to be "installed".
# MAGIC 
# MAGIC One such library is <a href="https://numpy.org/doc/stable" target="_blank">NumPy</a> - while a 3rd-party library, NumPy is pre-installed on the Databricks runtime.
# MAGIC   
# MAGIC To use any library, you need to first import it into the current name space:

# COMMAND ----------

import numpy

numpy.sqrt(9)

# COMMAND ----------

# MAGIC %md As with other functions, we can use the **`help()`** function on **`numpy.sqrt`** to get more information.

# COMMAND ----------

help(numpy.sqrt)

# COMMAND ----------

# MAGIC %md
# MAGIC You can also change the name of the library when you import it.
# MAGIC 
# MAGIC This can be handy when the code gets too verbose and abreviating or renaming the imported object makes the code easier to read.

# COMMAND ----------

import numpy as np

np.sqrt(12)

# COMMAND ----------

# MAGIC %md
# MAGIC And instead of importing just one function at a time, you can import every function from the NumPy package using the wildcard **`*`**.
# MAGIC 
# MAGIC Caution: importing too many things into the same name space can create confusion.
# MAGIC * Are you using Python's **`count()`** function? Databricks' **`count()`**? NumPy's **`count()`** function?

# COMMAND ----------

from numpy import *

sqrt(12)
absolute(-123)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>