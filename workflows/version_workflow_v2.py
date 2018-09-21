from tasks.task_a import TaskA
from tasks.task_b import TaskB
from tasks.task_c import TaskC
from tasks.task_d import TaskD

from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable
from zenaton.parallel import Parallel


class VersionWorkflowV2(Workflow, Zenatonable):

    def handle(self):
        Parallel(
            TaskA(),
            TaskB(),
            TaskC(),
            TaskD()
        ).execute()
