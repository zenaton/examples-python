import client

from workflows.recursive.recursive_workflow import RecursiveWorkflow

# if you need to kill an existing workflow, use:
# RecursiveWorkflow.where_id(0).kill()

RecursiveWorkflow(13, 17).dispatch()
