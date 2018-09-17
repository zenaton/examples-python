from tasks.parent_task import ParentTask

from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable


class NestedWorkflow(Workflow, Zenatonable):

    def handle(self):
        ParentTask().execute()
