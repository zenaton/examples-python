from tasks.task_a import TaskA
from tasks.task_b import TaskB
from tasks.task_c import TaskC
from tasks.task_d import TaskD

from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable
from zenaton.parallel import Parallel


class ParallelWorkflow(Workflow, Zenatonable):

    def handle(self):

        # Execute taskA and taskB in parallel
        a, b = Parallel(
            TaskA(),
            TaskB()
        ).execute()

        # Wait for the end of execution of both tasks
        if a > b:
            TaskC().execute()
        else:
            TaskD().execute()
