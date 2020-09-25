# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Variables and Data Types
# MAGIC 
# MAGIC ## In this lesson you:
# MAGIC * Explore fundamental Pythopn concepts
# MAGIC * Are introduced to 4 basic data types
# MAGIC * Declare and assign variables
# MAGIC * Employ simple, built-in functions such as **`print()`** and **`type()`**
# MAGIC * Develop and use **`assert`** statements
# MAGIC  

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Comments
# MAGIC 
# MAGIC Comments are any text that appear after the **`#`** symbol
# MAGIC 
# MAGIC They are often used to document various aspects of your code
# MAGIC 
# MAGIC They can also be used to temporary disable code (aka commenting out)

# COMMAND ----------

# This is a comment - it's here only for explination
# Run this cell, and notice the lack of output.
# Then uncomment the following line and run this cell again.
# print("Hello world!")

# COMMAND ----------

# MAGIC %md Comments can also appear after code to provide a different style of documentation

# COMMAND ----------

print("Step 1") # This is step #1
print("Step 2") # Step number 2 comes after #1
print("Step 3") # This is the last step

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Numbers &amp; Basic Mathematical Operators
# MAGIC Run the following three cells and note their output:

# COMMAND ----------

True # This is a boolean data type (1/0, true/false, on/off)

# COMMAND ----------

37 # This is whole number (or integer)

# COMMAND ----------

3.14159265359 # This is a floating-point number

# COMMAND ----------

# MAGIC %md The Python interpreter will (by default) render the result of the last operation on the console.
# MAGIC 
# MAGIC We can see that in the rendereding of **`Out[1]: True`**, **`Out[2]: 37`**, and **`Out[3]: 3.14159265359`** above.
# MAGIC 
# MAGIC We can leverage that feature to perform some basic mathimatical operations on various numbers.
# MAGIC 
# MAGIC Give it a quick try:
# MAGIC * Addition (**`+`**)
# MAGIC * Subtraction (**`-`**)
# MAGIC * Multiplication  (**`*`**)
# MAGIC * Division (**`/`**)
# MAGIC * Modulo (**`%`**)

# COMMAND ----------

27 + 3

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Strings
# MAGIC 
# MAGIC Strings in Python have `''` (single quotes),  `""` double quotes or tripple quotes around the content.

# COMMAND ----------

'Ice cream'

# COMMAND ----------

"More ice cream"

# COMMAND ----------

"""A really long string
with multiple lines"""

# COMMAND ----------

# MAGIC %md Like, numbers, strings can be "added" to gether.
# MAGIC 
# MAGIC This is more commonly referred to as concatenation.

# COMMAND ----------

'I love' + "to eat" + """ice cream"""

# COMMAND ----------

# MAGIC %md 
# MAGIC **Question:** What mistake did we make in concatenating those three strings?

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Data Types
# MAGIC We just saw an example of four data types:
# MAGIC * Boolean values: **`bool`**
# MAGIC * Whole or integral numbers: : **`int`**
# MAGIC * Floating-point numbers : **`float`**
# MAGIC * Strings values: : **`str`**
# MAGIC 
# MAGIC By combing these basic data types (and a few to be covered later),  
# MAGIC Python allows you to create a nearly infinite set of new types.

# COMMAND ----------

# MAGIC %md
# MAGIC If you are not sure what "type" something is, you can employ the <a href="https://docs.python.org/3/library/functions.html#type" target="_blank">type()</a> function.
# MAGIC 
# MAGIC We will discuss functions in detail later, but we can easily employ simple functions like this one without fully understanding them.

# COMMAND ----------

# The first of two possible boolean values
type(True) 

# COMMAND ----------

# The second of two possible boolean values
type(False) 

# COMMAND ----------

# A whole number, or integer
type(132) 

# COMMAND ----------

# A floating point number
type(34.62) 

# COMMAND ----------

# A single-quote string
type('A single quote string') 

# COMMAND ----------

# A double-quote string
type("A double quote string") 

# COMMAND ----------

# A tripple quote string
type("""A tripple quote string""") 

# COMMAND ----------

# MAGIC %md
# MAGIC Can you predict which type the next command will produce?
# MAGIC * **`bool`**
# MAGIC * **`int`**
# MAGIC * **`float`**
# MAGIC * **`str`**

# COMMAND ----------

type("723")

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Variables
# MAGIC 
# MAGIC In Python, a variable holds a value.
# MAGIC 
# MAGIC If you plan to re-use the same value multiple times in your code, it is best to put it in a variable so you can change its value only once.
# MAGIC 
# MAGIC Changes to the one variable will be reflected throughout all of your code.
# MAGIC 
# MAGIC A few things to note on Python variable names:
# MAGIC * A variable name must start with a letter or the underscore character
# MAGIC * Conversely, a variable name cannot start with a number
# MAGIC * A variable name can only contain alpha-numeric characters and underscores (a-Z, A-Z, 0-9, and _ )
# MAGIC * Variable names are case-sensitive (`age`, `Age`, and `AGE` are three different variables)
# MAGIC 
# MAGIC Beyond these hard requirements, additional standards are often imposed by development teams so as to produce consistent and easy to read code.
# MAGIC 
# MAGIC The most common standard for Python is <a href="https://www.python.org/dev/peps/pep-0008/" target="_blank">PEP 8</a>
# MAGIC 
# MAGIC PEP 8's most iconic feature is the use of an underscore in function and variable names.

# COMMAND ----------

# Examples of valid variable names:
best_food = "ice cream"    # An example of the snake case naming convention from PEP 8
bestFood = "pizza"         # An example of the cammel case
BEST_FOOD = "watermellon"
_BEST_FOOD = "brussel sprouts"

# Examples of invalid variable names:
# 1_best_food = "broccoli"
# $_best_food = "waffles"

# COMMAND ----------

# MAGIC %md We will use the **`best_food`** variable quite extensively in the rest of this notebook.

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) The Print Function
# MAGIC 
# MAGIC We can force Python to render output to the console by using the <a href="https://docs.python.org/3/library/functions.html#print" target="_blank">print</a> function.
# MAGIC 
# MAGIC We already saw this in an earlier statement: **`print("Hello world!")`**
# MAGIC 
# MAGIC The **`print()`** function is one of many <a href="https://docs.python.org/3/library/functions.html" target="_blank">Built-in Functions</a> and we can employ it here to print the four variables we just declared.

# COMMAND ----------

print(best_food)
print(bestFood)
print(BEST_FOOD)
print(_BEST_FOOD)

# COMMAND ----------

# MAGIC %md
# MAGIC Introduced in Python 3.6, **f-strings** provide another neat feature that comes in really handy when used in conjunction with the **`print()`** function.
# MAGIC 
# MAGIC **f-strings** allow you to build a string composed of one or more values in an rather concise manner.
# MAGIC 
# MAGIC Let's take a quick look at the "hard" way to compose such a string and how **f-strings** makes this easier

# COMMAND ----------

# Just for refference, what was the "best" food?
print(best_food) 

# COMMAND ----------

# Without f-strings, we have to concatenate the values
text = "The best food ever is" + best_food + ", especially when it's hot outside!"
print(text)

# COMMAND ----------

# With f-strings, we can "inject" the variable directly into the string
# Additionally certain types of bugs are easier to catch at a quick glance
text = f"The best food ever is {best_food}, especially when it's hot outside!"
print(text)

# COMMAND ----------

# And just to be a little more consise...
print(f"The best food ever is {best_food}, especially when it's hot outside!")

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Assert Statements and Type Checking
# MAGIC 
# MAGIC If you want to test if two things are equal, you can put them on either side of the **`==`** operator.

# COMMAND ----------

232 == 232

# COMMAND ----------

# MAGIC %md 
# MAGIC Conversely, if you want to test if things are not equal, you can use the **`!=`** operator.

# COMMAND ----------

723 != 723

# COMMAND ----------

# MAGIC %md Both the **`==`** opeartor and the **`!=`** operator return a boolean value as seen above.
# MAGIC 
# MAGIC Other common comparison <a href="https://docs.python.org/3/reference/lexical_analysis.html#operators" target="_blank">operators</a> include:
# MAGIC * **`>`** greater than
# MAGIC * **`<`** les than
# MAGIC * **`>=`** greater than or equal to
# MAGIC * **`<=`** less than or equal to
# MAGIC * ...and many more

# COMMAND ----------

32 > 12

# COMMAND ----------

# MAGIC %md
# MAGIC But what if we wanted to test if a value was of a certain type?
# MAGIC 
# MAGIC For this we can use the **`type()`** function and combine it with the equality operator (**`==`**) as seen here:

# COMMAND ----------

type(best_food) == str

# COMMAND ----------

type(32) == int

# COMMAND ----------

type(True) == bool

# COMMAND ----------

type(1.32) == float

# COMMAND ----------

# MAGIC %md
# MAGIC What if you wanted to verify, or assert, a specific precondition?
# MAGIC 
# MAGIC One example might be variable's datatype, in which case execution should stop if it is of the wrong type.
# MAGIC 
# MAGIC That's exactly what <a href="http://docs.python.org/reference/lexical_analysis.html#keywords" target="_blank">assert</a> statement allow us to do.
# MAGIC 
# MAGIC If the test, or assertion, does not pass, execution stops and Python prints an error message to the console as demonstrated here:

# COMMAND ----------

# To force the assertion failure, change line #4 below
# from a string value to an integer or boolean value.

best_food = "Pizza"
assert type(best_food) == str, "If this fails, it will print this message"

print("All done")

# COMMAND ----------

# MAGIC %md 
# MAGIC If we wanted to make the error message a little more useful, we can employ an **f-string** instead:

# COMMAND ----------

best_food = "BBQ Chicken"
assert type(best_food) == str, f"Expected best_food to be of type str but found {type(best_food)} instead"

print("All done")

# COMMAND ----------

# MAGIC %md
# MAGIC `assert` is a keyword in Python, so make sure you don't declare any variables named **`assert`**!

# COMMAND ----------

# MAGIC %md
# MAGIC ### ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Review
# MAGIC 
# MAGIC **Question**: What mathimatical operators were you introduced to in this lesson?<br/>
# MAGIC Hint: See the python docs on Lexical analysis, section 2.5, <a href="https://docs.python.org/3/reference/lexical_analysis.html#operators" target="_blank">Operators</a>
# MAGIC 
# MAGIC **Question**: What reserved keywords were you introduced to in this lesson?<br/>
# MAGIC Hint: See the python docs on Lexical analysis, section 2.3.1, <a href="http://docs.python.org/reference/lexical_analysis.html#keywords" target="_blank">Keywords</a>
# MAGIC 
# MAGIC **Question**: How are reserved kewords like **`assert`** different from **`print`** and **`type`**?
# MAGIC 
# MAGIC **Question**: Which data types were you introduced to in this lesson?
# MAGIC 
# MAGIC **Question**: What functions were you introduced to in this lesson?<br/>
# MAGIC Hint: See the python docs on <a href="https://docs.python.org/3/library/functions.html" target="_blank">Built-in Functions</a>

# COMMAND ----------

# MAGIC %md
# MAGIC ### ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Congrats! You have finished your first lesson on Python!

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>