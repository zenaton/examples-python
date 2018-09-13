import client

from workflows.recursive.recursive_workflow import RecursiveWorkflow

# if you need to kill an existing workflow, use:
# RecursiveWorkflow.where_id(0).kill()

RecursiveWorkflow(0, 2).dispatch()
