import time

from zenaton.abstracts.task import Task
from zenaton.traits.zenatonable import Zenatonable

from .task_a import TaskA


class ParentTask(Task, Zenatonable):

    def handle(self):
        print('Parent Task')
        time.sleep(1)
        TaskA().execute()
        return 'Parent Task'
