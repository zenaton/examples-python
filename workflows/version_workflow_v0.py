from tasks.task_a import TaskA
from tasks.task_b import TaskB

from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable
from zenaton.parallel import Parallel


class VersionWorkflowV0(Workflow, Zenatonable):

    def handle(self):
        Parallel(
            TaskA(),
            TaskB()
        ).execute()
