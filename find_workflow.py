import time

import client
from workflows.sequential_workflow import SequentialWorkflow

"""Step 1: Dispatch"""
SequentialWorkflow().dispatch()

"""Step 2: Sleep"""
time.sleep(1)

"""Step 3: Find Workflow"""
workflow = SequentialWorkflow().where_id('MySequentialId').find()
print(workflow)
