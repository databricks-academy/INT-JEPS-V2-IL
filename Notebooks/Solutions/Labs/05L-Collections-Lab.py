# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Collections Lab
# MAGIC 
# MAGIC Write a function named `item_count` that accepts a list of values and returns a dictionary with a count of the number of times each unique value appeared in the list. For example, `item_count(['a', 'b', 'a'])` should return the dictionary `{'a': 2, 'b': 1}`

# COMMAND ----------

# ANSWER
def item_count(input_list):
  output_dict = {}  # Initialize an empty dictionary
  
  for item in input_list:
    if item not in output_dict:
      # Create an element for the item with an initial count of 1
      output_dict[item] = 1
    else:
      # Add 1 to the current count for the item
      output_dict[item] += 1
      
  return output_dict

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://s3-us-west-2.amazonaws.com/curriculum-release/images/105/logo_spark_tiny.png) Validate Your Answer
# MAGIC 
# MAGIC Once you have implemented and executed your solution, run the following cell to confirm that it produces correct results. It should not raise any errors if you implemented the function correctly.

# COMMAND ----------

empty_list = []
empty_count_result = {}
assert item_count(empty_list) == empty_count_result

breakfast_list = ["pancake", "egg", "egg", "pancake", "coffee", "pancake"]
breakfast_count_result = {
  "pancake": 3,
  "egg": 2,
  "coffee": 1,
}
assert item_count(breakfast_list) == breakfast_count_result

print("Congratulations! All tests passed.")


# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>