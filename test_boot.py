from Zenaton.core.abstracts.workflow import Workflow
from workflows.recursive.recursive_workflow import RecursiveWorkflow

print(issubclass(RecursiveWorkflow, Workflow))

nested_dict = {'z': 50, 'a': 10}

dict = {'nested_dict': nested_dict, 'a': 1}

print(dict)

import json

print(json.dumps(dict))

print(json.dumps(dict, sort_keys=True))
