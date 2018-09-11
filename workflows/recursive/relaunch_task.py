from Zenaton.core.abstracts.task import Task
from Zenaton.core.traits.zenatonable import Zenatonable


class RelaunchTask(Zenatonable, Task):

    def __init__(self, task_id, max):
        self.task_id = task_id
        self.max = max

    def handle(self):
        from .recursive_workflow import RecursiveWorkflow
        if self.task_id < self.max:
            self.task_id += 1
            print("Iterations: {}".format(self.task_id))
            RecursiveWorkflow(self.task_id, self.max).dispatch()
