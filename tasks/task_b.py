import time

from Zenaton.core.abstracts.task import Task
from Zenaton.core.traits.zenatonable import Zenatonable


class TaskB(Task, Zenatonable):

    def handle(self):
        print('Task B')
        time.sleep(5)
        return 'Task B'
