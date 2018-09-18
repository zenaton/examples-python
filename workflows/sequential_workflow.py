from tasks.task_a import TaskA
from tasks.task_b import TaskB
from tasks.task_c import TaskC
from tasks.task_d import TaskD

from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable


class SequentialWorkflow(Workflow, Zenatonable):

    def handle(self):

        a = TaskA().execute()

        if a == 0:
            TaskB().execute()
        else:
            TaskC().execute()

        TaskD().execute()
