import Zenaton
from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable
from Zenaton.core.tasks.wait import Wait

from tasks.task_a import TaskA
from tasks.task_b import TaskB


class WaitWorkflow(Workflow, Zenatonable):

    def handle(self):
        TaskA().execute()
        Wait().seconds(5).execute()  # Wait().timestamp(1535984730).execute()
        TaskB().execute()
