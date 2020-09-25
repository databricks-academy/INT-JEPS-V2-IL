// Databricks notebook source
// MAGIC %md-sandbox
// MAGIC 
// MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
// MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
// MAGIC </div>

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC #Getting Started with Python
// MAGIC 
// MAGIC ## In this lesson you'll learn:
// MAGIC 
// MAGIC * Key Python Internet resources
// MAGIC * How to run Python code in various environments

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) What is Python?
// MAGIC 
// MAGIC > Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.<br/>
// MAGIC > Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it<br/>
// MAGIC > very attractive for Rapid Application Development, as well as for use as a scripting or glue language<br/>
// MAGIC > to connect existing components together.
// MAGIC 
// MAGIC <a href="https://www.python.org/doc/essays/blurb/" target="_blank">https&#58;//www.python.org/doc/essays/blurb</a>
// MAGIC 
// MAGIC Key Points:
// MAGIC - Python is an interpreted programming language (compilation of the program is not required)
// MAGIC - The main focus is on **readability** and **productivity**
// MAGIC - It is dynamically typed language (type checking is performed at run time)
// MAGIC - Despite their dynamic nature, values cannot be implicitly coerced to unrelated types (for example, **`print("Foo " + 5)`** throws a **`TypeError`**)
// MAGIC - Created by Guido van Rossum and first released in 1990

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Important Links
// MAGIC 
// MAGIC - The home page of Python is at <a href="https://www.python.org" target="_blank">https&#58;//www.python.org</a>
// MAGIC - Documentation about standard features and library is available at <a href="https://docs.python.org/3" target="_blank">https&#58;//docs.python.org/3</a>
// MAGIC - A useful list of libraries available for Python is available at <a href="https://github.com/vinta/awesome-python" target="_blank">https&#58;//github.com/vinta/awesome-python</a>
// MAGIC 
// MAGIC Additional Resources:
// MAGIC * [Python for Data Analysis by Wes McKinney](https://www.amazon.com/gp/product/1491957662/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=quantpytho-20&creative=9325&linkCode=as2&creativeASIN=1491957662&linkId=ea8de4253cce96046e8ab0383ac71b33)
// MAGIC * [Python reference sheet](http://www.cogsci.rpi.edu/~destem/igd/python_cheat_sheet.pdf)
// MAGIC * [Python official tutorial](https://docs.python.org/3/tutorial/)

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Running Python Programs
// MAGIC 
// MAGIC This is a Python program that simply prints "Hello, world!" to the terminal when executed:
// MAGIC 
// MAGIC <pre style="font-weight:bold">
// MAGIC print("Hello, world!")
// MAGIC </pre>
// MAGIC 
// MAGIC :SIDENOTE: By convention, Python source files use a **`.py`** extension.
// MAGIC 
// MAGIC Use the **`python`** command to run your Python program:
// MAGIC 
// MAGIC <pre>$ python HelloWorld.py</pre>

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) The Python REPL
// MAGIC 
// MAGIC Python also includes a REPL (“read-eval-print-loop”) that functions as an interpreter for Python code. Using the REPL you can interactively execute and test out Python code.
// MAGIC 
// MAGIC You start the REPL from the terminal by executing the **`python`** command with no arguments. For example:
// MAGIC 
// MAGIC <pre style="font-weight:bold">
// MAGIC $ python
// MAGIC Python 3.7.1 (default, Dec 14 2018, 13:28:58) 
// MAGIC [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
// MAGIC Type "help", "copyright", "credits" or "license" for more information.
// MAGIC >>> print("Welcome to Databricks Academy")
// MAGIC Welcome to Databricks Academy
// MAGIC >>> exit()
// MAGIC $ 
// MAGIC </pre>

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Python and IDEs
// MAGIC 
// MAGIC For developing Python in an integrated development environment (IDE), there are two main choices:
// MAGIC 
// MAGIC * PyCharm: <a href="https://www.jetbrains.com/pycharm" target="_blank">https&#58;//www.jetbrains.com/pycharm</a>
// MAGIC * Spyder: <a href="https://www.spyder-ide.org" target="_blank">https&#58;//www.spyder-ide.org</a>
// MAGIC * Atom: <a href="https://ide.atom.io/" target="_blank">https&#58;//ide.atom.io/</a>

// COMMAND ----------

// MAGIC %md ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Databricks Connect
// MAGIC 
// MAGIC **Databricks Connect** allows you to connect your favorite IDE (IntelliJ, Eclipse, PyCharm, RStudio, Visual Studio), notebook server (Zeppelin, Jupyter), and other custom applications to Databricks clusters and run Apache Spark code.
// MAGIC 
// MAGIC With Databricks Connect, you can:
// MAGIC * Run large-scale Spark jobs from any Python, Java, Scala, or R application. 
// MAGIC * Step through and debug code in your IDE even when working with a remote cluster.
// MAGIC * Iterate quickly when developing libraries. 
// MAGIC * Shut down idle clusters without losing work. 
// MAGIC 
// MAGIC For more information, see <a href="https://docs.databricks.com/dev-tools/databricks-connect.html" target="_blank">https&#58;//docs.databricks.com/dev-tools/databricks-connect.html</a>

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Notebook Interfaces for Python Development
// MAGIC 
// MAGIC Databricks provides a notebook interface for developing executable code, visualizations, and narrative text. When you run an executable code cell in a notebook, the code is executed in a Python REPL on the Databricks cloud platform and the results are displayed in the notebook.
// MAGIC 
// MAGIC Other notebook interfaces with support for Python include:
// MAGIC 
// MAGIC * Apache Zeppelin: <a href="https://zeppelin.apache.org" target="_blank">https&#58;//zeppelin.apache.org</a>
// MAGIC * Jupyter Notebook: <a href="https://jupyter.org" target="_blank">https&#58;//jupyter.org</a>
// MAGIC 
// MAGIC Try executing the following code cell.

// COMMAND ----------

// MAGIC %python
// MAGIC 
// MAGIC print("Hello, world!")

// COMMAND ----------

// MAGIC %md-sandbox
// MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
// MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
// MAGIC <br/>
// MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>