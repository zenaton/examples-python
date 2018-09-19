from tasks.task_a import TaskA
from tasks.task_b import TaskB
from tasks.task_c import TaskC

from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable


class SequentialWorkflow(Workflow, Zenatonable):

    def handle(self):

        a = TaskA().execute()

        if a > 0:
            TaskB().execute()
        else:
            TaskC().execute()
