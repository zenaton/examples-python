import time

from Zenaton.core.abstracts.task import Task
from Zenaton.core.traits.zenatonable import Zenatonable


class TaskA(Task, Zenatonable):

    def handle(self):
        print('Task A')
        time.sleep(3)
        return 'Task A'
