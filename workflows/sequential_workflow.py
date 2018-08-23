from tasks.task_a import TaskA
from tasks.task_b import TaskB

from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable


class SequentialWorkflow(Workflow, Zenatonable):

    def handle(self):
        TaskA().execute()
        TaskB().execute()