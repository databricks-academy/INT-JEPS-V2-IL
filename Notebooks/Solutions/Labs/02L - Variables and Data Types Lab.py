# Databricks notebook source
# MAGIC 
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Variables and Data Types Lab
# MAGIC 
# MAGIC Let's convert EUR to USD and prints the results. The current exchange rate as of 14 August 2020 is 1 EUR -> 1.18 USD.

# COMMAND ----------

# MAGIC %md
# MAGIC First let's create a variable called `conversion_rate` to use.
# MAGIC 
# MAGIC This way, if the rate ever changes, we would only need to modify this single line of code and have everything else still work properly!

# COMMAND ----------

# ANSWER
conversion_rate = 1.18

# COMMAND ----------

# MAGIC %md
# MAGIC Check what is the type of `conversion_rate`.

# COMMAND ----------

# ANSWER
type(conversion_rate)

# COMMAND ----------

# MAGIC %md
# MAGIC Given that we have 567 EUR, compute what the corresponding amount should be in USD, assigning the result to the variable `usd_amount`. Make sure you to use the variable `conversion_rate` in your computation.

# COMMAND ----------

# ANSWER
euro_amount = 567
usd_amount = conversion_rate * euro_amount
usd_amount

# COMMAND ----------

# MAGIC %md
# MAGIC Print out the statement `{} Euros is equal to ${} USD`, passing in the variables `euro_amount` and `usd_amount` into the expression.

# COMMAND ----------

# ANSWER
print(f"{euro_amount} Euros is equal to ${usd_amount} USD")


# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>