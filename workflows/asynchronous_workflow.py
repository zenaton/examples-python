from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable

from tasks.task_a import TaskA
from tasks.task_b import TaskB


class AsynchronousWorkflow(Workflow, Zenatonable):

    def handle(self):
        TaskA().dispatch()
        TaskB().execute()
