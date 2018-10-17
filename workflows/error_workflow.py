from tasks.task_a import TaskA
from tasks.task_c import TaskC
from tasks.task_e import TaskE

from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable
from zenaton.parallel import Parallel


class ErrorWorkflow(Workflow, Zenatonable):

    def handle(self):
        Parallel(
            TaskA(),
            TaskE()
        ).execute()

        TaskC().execute()
