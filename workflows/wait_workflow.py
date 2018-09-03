import Zenaton
from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable

from tasks.task_a import TaskA
from tasks.task_b import TaskB


class WaitWorkflow(Workflow, Zenatonable):

    def handle(self):
        TaskA().execute()
        # Zenaton.core.tasks.wait.Wait().seconds(5).execute()
        Zenaton.core.tasks.wait.Wait().timestamp(1535984730).execute()
        TaskB().execute()
