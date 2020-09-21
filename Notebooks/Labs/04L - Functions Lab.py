# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Functions Lab

# COMMAND ----------

# MAGIC %md
# MAGIC 1. Convert the following code to a function that takes a number as an argument and returns either FizzBuzz, Buzz and Fizz correctly.<br>
# MAGIC 2. Write a loop that applies your function to `num_list1` to test your function.<br>
# MAGIC 3. After you have your function working add an int type hint to the num parameter.<br>
# MAGIC Then remove the conditional test for a number from you function by removing the following lines:<br>
# MAGIC 
# MAGIC <pre><code>  if type(num) == int or type(num) == float:<br>
# MAGIC   else:
# MAGIC     print("Not a number")
# MAGIC </code></pre>    

# COMMAND ----------

# MAGIC %md
# MAGIC Convert the following code to a function that takes a number as an argument and returns FizzBuzz, Buzz, Fizz, or the number itself correctly.

# COMMAND ----------

# TODO
num = 10

def <FILL_IN>
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

fizzBuzz(num)

# COMMAND ----------

# MAGIC %md
# MAGIC Write a loop that applies your function to `num_list1` to test your function

# COMMAND ----------

# TODO
num_list1 = [1, 1.56, 3, 5, 15, 30, 50, 77, "Hello"]
# <FILL_IN>

# COMMAND ----------

# MAGIC %md
# MAGIC Now add in an int type hint to the the num parameter of the `fizzBuzz` function, and remove the check for int or float (let the type hint do the work instead).<br>
# MAGIC 
# MAGIC You can remove the conditional test for a number from you function by removing the following lines:<br>
# MAGIC 
# MAGIC <pre><code>  if type(num) == int or type(num) == float:<br>
# MAGIC   else:
# MAGIC     print("Not a number")
# MAGIC </code></pre>    

# COMMAND ----------

# TODO

# COMMAND ----------

# MAGIC %md
# MAGIC Uncomment lines 2 and 3 below and you should receive the following error:<br>
# MAGIC `TypeError: not all arguments converted during string formatting`

# COMMAND ----------

# Uncomment below - it should error
#for num in num_list1:
#  fizzBuzz(num)

# COMMAND ----------

# MAGIC %md
# MAGIC When you run the for loop on the list below with the string removed, it will not error even though this list still contains a double, Why?

# COMMAND ----------

num_list2 = [1, 1.56, 3, 5, 15, 30, 50, 77]
for num in num_list2:
  fizzBuzz(num)


# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>