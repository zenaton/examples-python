from tasks.task_a import TaskA
from tasks.task_b import TaskB
from tasks.task_c import TaskC
from tasks.task_d import TaskD

from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable


class IdWorkflow(Workflow, Zenatonable):

    def __init__(self, id_):
        self.id_ = id_

    def handle(self):

        a = TaskA().execute()

        if a > 0:
            TaskB().execute()
        else:
            TaskC().execute()

        TaskD().execute()

    def id(self):
        return self.id_
