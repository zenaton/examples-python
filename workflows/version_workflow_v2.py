from tasks.task_a import TaskA
from tasks.task_b import TaskB
from tasks.task_c import TaskC
from tasks.task_d import TaskD

from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable
from Zenaton.core.parallel import Parallel


class VersionWorkflowV2(Workflow, Zenatonable):

    def handle(self):
        Parallel(
            TaskA(),
            TaskB(),
            TaskC(),
            TaskD()
        ).execute()
