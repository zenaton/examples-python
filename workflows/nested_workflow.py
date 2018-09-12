from tasks.parent_task import ParentTask

from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable


class NestedWorkflow(Workflow, Zenatonable):

    def handle(self):
        ParentTask().execute()
