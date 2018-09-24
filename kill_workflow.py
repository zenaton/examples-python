import time
import uuid

import client
from workflows.id_workflow import IdWorkflow

workflow_id = str(uuid.uuid4())

"""Step 1: Dispatch"""
IdWorkflow(workflow_id).dispatch()

"""Step 2: Sleep"""
time.sleep(2)

"""Step 3: Kill"""
IdWorkflow.where_id(workflow_id).kill()
