# Just Enoug Python for Spark
This repository contains the resources students need to follow along with the instructor teaching this course in addition to the various labs and their solutions.

There are two means by which to get started (with and w/o Databricks Projects). Besides the instructions provided here, You instructor will review these procedures at the start of the course.

## Getting Started with Databricks Projects
1. Note: As of Sept, 18, 2020, Databricks Projects is only availbe as a private preview and may not be availble to all customers
2. Click on the **Projects** icon in the navigational pane to the left
3. By default, you should be in the folder **/Projects/*your-email-address* ** for example: **/Projects/student@azuredatabrickstraining.onmicrosoft.com**
4. Click the **Create Projects** button above the two swim lanes
5. In the **Create Projects** dialog box
   1. Select **Clone from Git repo**
   2. Enter the URL for the Git repo, in this case, https://github.com/databricks-curriculum/INT-JEPS-V2-IL.git
   3. The Git provider **GitHub** should be selected for you automatically
   4. The **Project name** should default to **INT-JEPS-V2-IL** - feel free to rename this if you like
   5. Click the **Create** button
6. Once the import is done, select the project folder, the default being **INT-JEPS-V2-IL**
7. From here you should be able to follow along with your instructor

## Getting Started without Databricks Projects
1. Click on the **Home** icon in the navigational pane to the left
2. By default, you should be in the folder **/Users/*your-email-address* ** for example: **/Users/student@azuredatabrickstraining.onmicrosoft.com**
3. In the swimlane for your email address, click on the down chevron and select **Create|Folder**
4. In the **New Folder Name** dialog enter a name for this project, for example, **INT-JEPS-V2-IL**, or any other name you desire to use
5. Import each notebook:
   1. In the swimlane **INT-JEPS-V2-IL**, click the down chevron and select **Import**
   2. In the **Import Notebooks** dialog
      1. Select **URL**
      2. Enter the URL for the desired notebook, the first one being https://raw.githubusercontent.com/databricks-curriculum/INT-JEPS-V2-IL/master/01-Databricks-Environment.py
      3. Click **Import**
   3. Repeat these steps for each notebook. Note: The URL for each notebook will start with https://raw.githubusercontent.com/databricks-curriculum/INT-JEPS-V2-IL/master/
      - 01-Databricks-Environment
      - 02-Variables-and-Data-Types
      - 03-Conditionals-and-Loops
      - 04-Methods-Functions-Packages
      - 05-Collections-and-Classes
      - 06-Pandas
      - 07-COVID-Demo
   4. For the labs we suggest creating the **Labs** folder and importing the corresponding notebooks into that folder.  
   The notebooks for this set will start with the URL  
   https://raw.githubusercontent.com/databricks-curriculum/INT-JEPS-V2-IL/master/Labs
   5. For the solutions, we suggest creating the **Solutions** folder and importing the corresponding notebooks into that folder.  
   The notebooks for this set will start with the URL  
   https://raw.githubusercontent.com/databricks-curriculum/INT-JEPS-V2-IL/master/Solutions
