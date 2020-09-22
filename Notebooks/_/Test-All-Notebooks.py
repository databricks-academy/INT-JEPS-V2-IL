# Databricks notebook source
# MAGIC %md # Basic Config

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC # Job Name / Course Name
# MAGIC sku = "INT-JEPFS-V2-IL"
# MAGIC 
# MAGIC # The runtime you wish to test against
# MAGIC spark_version = "7.0.x-scala2.12"
# MAGIC 
# MAGIC # Which instance pool to test against (pools makes jobs a 1,000,000x faster)
# MAGIC instance_pool = "1117-113806-juice922-pool-JxljQpdx" # Amazon
# MAGIC #instance_pool = "1117-121723-show503-pool-ubXZ7gOS" # MS Azure
# MAGIC 
# MAGIC tags = sc._jvm.scala.collection.JavaConversions.mapAsJavaMap(dbutils.entry_point.getDbutils().notebook().getContext().tags())
# MAGIC home = f"""/Projects/{tags["user"]}/INT-JEPFS-V2-IL/Notebooks"""
# MAGIC 
# MAGIC notebooks = [
# MAGIC   f"{home}/JEP 01 - Databricks Environment",
# MAGIC   f"{home}/JEP 02 - Variables and Data Types",
# MAGIC   f"{home}/JEP 03 - Conditionals and Loops",
# MAGIC   f"{home}/JEP 04 - Methods, Functions, Packages",
# MAGIC   f"{home}/JEP 05 - Collections and Classes",
# MAGIC   
# MAGIC   f"{home}/Optional/JEP 06 - Pandas",
# MAGIC   f"{home}/Optional/JEP 07 - COVID Demo",
# MAGIC   
# MAGIC   # f"{home}/Labs/JEP 02L - Variables and Data Types Lab",
# MAGIC   # f"{home}/Labs/JEP 03L - Fizz Buzz Lab",
# MAGIC   # f"{home}/Labs/JEP 04L - Functions Lab",
# MAGIC   # f"{home}/Labs/JEP 05L - Collections Lab",
# MAGIC   # f"{home}/Labs/JEP 06L - Pandas Lab",
# MAGIC   # f"{home}/Labs/JEP 07L - Data Analysis Lab",
# MAGIC   
# MAGIC   f"{home}/Solutions/JEP 02S - Variables and Data Types Lab",
# MAGIC   f"{home}/Solutions/JEP 03S - Fizz Buzz Lab",
# MAGIC   f"{home}/Solutions/JEP 04S - Functions Lab",
# MAGIC   f"{home}/Solutions/JEP 05S - Collections Lab",
# MAGIC   f"{home}/Solutions/JEP 06S - Pandas Lab",
# MAGIC   f"{home}/Solutions/JEP 07S - Data Analysis Lab",
# MAGIC ]

# COMMAND ----------

# MAGIC %md # REST API & Utility Functions

# COMMAND ----------

# MAGIC %run "./Test-Utilities"

# COMMAND ----------

# MAGIC %md # Remove old jobs

# COMMAND ----------

deleteJobs(sku)

# COMMAND ----------

# MAGIC %md
# MAGIC # All notebooks at once

# COMMAND ----------

resultsMap = testAllNotebooks(sku, notebooks, spark_version, instance_pool)

# COMMAND ----------

for key in resultsMap:
  waitForNotebook(key, resultsMap)

# COMMAND ----------

# MAGIC %md # Clean Up

# COMMAND ----------

deleteJobs(sku)

# COMMAND ----------

