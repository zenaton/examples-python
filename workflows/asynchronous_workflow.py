from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable

from tasks.task_a import TaskA
from tasks.task_b import TaskB
from tasks.task_c import TaskC
from tasks.task_d import TaskD


class AsynchronousWorkflow(Workflow, Zenatonable):

    def handle(self):
        TaskA().dispatch()
        TaskB().dispatch()
        TaskC().execute()
        TaskD().execute()
