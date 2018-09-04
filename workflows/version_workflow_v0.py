from tasks.task_a import TaskA
from tasks.task_b import TaskB

from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable
from Zenaton.core.parallel import Parallel


class VersionWorkflowV0(Workflow, Zenatonable):

    def handle(self):
        Parallel(
            TaskA(),
            TaskB()
        ).execute()
