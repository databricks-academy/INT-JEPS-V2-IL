# Databricks notebook source
# MAGIC %python
# MAGIC import time, json, requests
# MAGIC 
# MAGIC endpoint = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().getOrElse(None)
# MAGIC token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().getOrElse(None)
# MAGIC 
# MAGIC def deleteJobs(job_name):
# MAGIC   response = requests.get(
# MAGIC     f"{endpoint}/api/2.0/jobs/list",
# MAGIC     headers = { "Authorization": "Bearer " + token }
# MAGIC   )
# MAGIC   assert response.status_code == 200, f"({response.status_code}): {response.text}"
# MAGIC 
# MAGIC   count = 0
# MAGIC   jobs = response.json()["jobs"]
# MAGIC   print(f"Found {len(jobs)} in all")
# MAGIC   
# MAGIC   for job in jobs:
# MAGIC     job_id = job["job_id"]
# MAGIC     if job_name == job["settings"]["name"]:
# MAGIC       print(f"Deleting job #{job_id}")
# MAGIC       response = requests.post(
# MAGIC         f"{endpoint}/api/2.0/jobs/delete",
# MAGIC         headers = { "Authorization": "Bearer " + token },
# MAGIC         data = json.dumps({ "job_id": job_id })
# MAGIC       )
# MAGIC       assert response.status_code == 200, f"({response.status_code}): {response.text}"
# MAGIC       count += 1
# MAGIC   print(f"Deleted {count} jobs")
# MAGIC 
# MAGIC def createJob(job_name, notebook_path, spark_version, instance_pool):
# MAGIC   params = {
# MAGIC 	"notebook_task": {
# MAGIC 		"notebook_path": f"{notebook_path}",
# MAGIC         "base_parameters": {
# MAGIC           "sparkVersion": f"{spark_version}",
# MAGIC           "databricksUsername": f"run-all-{job_name.lower()}@databricks.com"
# MAGIC         }
# MAGIC 	},    	
# MAGIC 	"name": f"{job_name}",    	
# MAGIC 	"timeout_seconds": 7200,    	
# MAGIC 	"max_concurrent_runs": 1,    	
# MAGIC 	"email_notifications": {},    	
# MAGIC 	"libraries": [],    	
# MAGIC 	"new_cluster": {    		
# MAGIC 		"num_workers": 2,    		
# MAGIC 		"instance_pool_id": f"{instance_pool}",
# MAGIC 		"spark_version": f"{spark_version}"
# MAGIC 		}    
# MAGIC   }
# MAGIC   response = requests.post(
# MAGIC     f"{endpoint}/api/2.0/jobs/create",
# MAGIC     headers = { "Authorization": "Bearer " + token },
# MAGIC     data = json.dumps(params)
# MAGIC   )
# MAGIC   assert response.status_code == 200, f"({response.status_code}): {response.text}"
# MAGIC   return response.json()["job_id"]
# MAGIC 
# MAGIC def runJobNow(job_id):
# MAGIC   response = requests.post(
# MAGIC     f"{endpoint}/api/2.0/jobs/run-now",
# MAGIC     headers = { "Authorization": "Bearer " + token },
# MAGIC     data = json.dumps({ "job_id": job_id })
# MAGIC   )
# MAGIC   assert response.status_code == 200, f"({response.status_code}): {response.text}"
# MAGIC   return response.json()["run_id"]
# MAGIC 
# MAGIC 
# MAGIC def getRun(run_id):
# MAGIC   response = requests.get(
# MAGIC     f"{endpoint}/api/2.0/jobs/runs/get?run_id={run_id}",
# MAGIC     headers = { "Authorization": "Bearer " + token }
# MAGIC   )
# MAGIC   assert response.status_code == 200, f"({response.status_code}): {response.text}"
# MAGIC   return response.json()
# MAGIC 
# MAGIC def waitForRun(run_id):
# MAGIC   wait = 15
# MAGIC   response = getRun(run_id)
# MAGIC   state = response["state"]["life_cycle_state"]
# MAGIC   
# MAGIC   if state != "TERMINATED" and state != "INTERNAL_ERROR":
# MAGIC     print(f" - job is {state}, checking again in {wait} seconds")
# MAGIC     time.sleep(wait)
# MAGIC     return waitForRun(run_id)
# MAGIC   
# MAGIC   return response
# MAGIC 
# MAGIC def waitForNotebook(notebook, resultsMap, fail_fast=True):
# MAGIC   run_id = resultsMap[notebook]
# MAGIC   print(f"Waiting for {notebook} to finish")
# MAGIC   
# MAGIC   response = waitForRun(run_id)
# MAGIC   
# MAGIC   if response['state']['life_cycle_state'] == 'INTERNAL_ERROR':
# MAGIC     print() # Usually a notebook-not-found
# MAGIC     print(json.dumps(response, indent=1))
# MAGIC     raise RuntimeError(response['state']['state_message'])
# MAGIC 
# MAGIC   
# MAGIC   print(f" - job is {response['state']['life_cycle_state']} - {response['state']['result_state']}")
# MAGIC   
# MAGIC   if response['state']['result_state'] == 'FAILED':
# MAGIC     print("-"*80)
# MAGIC     print(json.dumps(response, indent=1))
# MAGIC     print("-"*80)
# MAGIC     if fail_fast: raise RuntimeError(f"{response['task']['notebook_task']['notebook_path']} failed.")
# MAGIC   
# MAGIC def testAllNotebooks(job_name, notebooks, spark_version, instance_pool):
# MAGIC   results = dict()
# MAGIC   
# MAGIC   for notebook_path in notebooks:
# MAGIC     print(f"Starting job for {notebook_path}")
# MAGIC     job_id = createJob(job_name, notebook_path, spark_version, instance_pool)
# MAGIC     run_id = runJobNow(job_id)
# MAGIC     results[notebook_path] = run_id
# MAGIC   
# MAGIC   return results