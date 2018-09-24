import time
import uuid

import client
from workflows.id_workflow import IdWorkflow

workflow_id = str(uuid.uuid4())

"""Step 1: Dispatch"""
IdWorkflow(workflow_id).dispatch()

"""Step 2: Pause"""
IdWorkflow.where_id(workflow_id).pause()

"""Step 3: Sleep"""
time.sleep(30)

""""Step 4: Resume"""
IdWorkflow.where_id(workflow_id).resume()
