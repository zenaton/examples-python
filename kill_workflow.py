import time

import client
from workflows.sequential_workflow import SequentialWorkflow

"""Step 1: Dispatch"""
SequentialWorkflow().dispatch()

"""Step 2: Sleep"""
time.sleep(2)

"""Step 3: Kill"""
SequentialWorkflow().where_id('MySequentialId').kill()
