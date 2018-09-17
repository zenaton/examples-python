from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable

from tasks.task_a import TaskA
from tasks.task_b import TaskB


class AsynchronousWorkflow(Workflow, Zenatonable):

    def handle(self):
        TaskA().dispatch()
        TaskB().execute()
