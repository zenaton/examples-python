from tasks.task_a import TaskA
from tasks.task_b import TaskB
from tasks.task_c import TaskC

from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable
from zenaton.parallel import Parallel


class VersionWorkflowV1(Workflow, Zenatonable):

    def handle(self):
        Parallel(
            TaskA(),
            TaskB(),
            TaskC()
        ).execute()
