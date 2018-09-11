import random

import client

from workflows.recursive.recursive_workflow import RecursiveWorkflow

workflow_id = int(random.random() * 10000)

RecursiveWorkflow(workflow_id, workflow_id + 10).dispatch()
