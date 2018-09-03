import time

from Zenaton.core.abstracts.task import Task
from Zenaton.core.traits.zenatonable import Zenatonable


class TaskC(Task, Zenatonable):

    def handle(self):
        print('Task C')
        time.sleep(9)
        return 'Task C'
