# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Pandas Lab
# MAGIC 
# MAGIC In this lab, you will use [pandas](https://pandas.pydata.org/docs/) for basic data manipulation.

# COMMAND ----------

# MAGIC %md
# MAGIC Create a DataFrame called `df` with 3 columns and 3 rows with integers like in the following image. It should also have the appropriate column names.
# MAGIC 
# MAGIC ![DataFrame](https://files.training.databricks.com/images/create_dataframe.png)

# COMMAND ----------

# ANSWER
import pandas as pd

data = [[1,2,3], [4,5,6], [7,8,9]]
df = pd.DataFrame(data=data, columns = ["one", "two", "three"])
df

# COMMAND ----------

# MAGIC %md
# MAGIC Display a DataFrame that only has the column `three`.

# COMMAND ----------

# ANSWER
df[["three"]]

# COMMAND ----------

# MAGIC %md
# MAGIC Return a Series (not DataFrame) object which just contains the values from the column `three`.

# COMMAND ----------

# ANSWER
print(type(df["three"]))
df["three"]

# COMMAND ----------

# MAGIC %md
# MAGIC Programmatically extract the number `5` from `df`. Which column and row do you need to access?

# COMMAND ----------

# ANSWER

df["two"][1]

# COMMAND ----------

# MAGIC %md
# MAGIC Add a new column called `row sum` to `df` which contains the sum of entries across each row in `df`.

# COMMAND ----------

# ANSWER

df["row sum"] = df["one"] + df["two"] + df["three"]
df


# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>