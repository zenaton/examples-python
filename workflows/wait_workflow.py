from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable
from zenaton.tasks.wait import Wait

from tasks.task_a import TaskA
from tasks.task_b import TaskB


class WaitWorkflow(Workflow, Zenatonable):

    def handle(self):
        TaskA().execute()
        Wait().seconds(5).execute()
        TaskB().execute()
