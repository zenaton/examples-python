import time

import client
from workflows.sequential_workflow import SequentialWorkflow

"""Step 1: Dispatch"""
SequentialWorkflow().dispatch()

"""Step 2: Pause"""
SequentialWorkflow().where_id('MySequentialId').pause()

"""Step 3: Sleep"""
time.sleep(30)

""""Step 4: Resume"""
SequentialWorkflow().where_id('MySequentialId').resume()
