import time

from Zenaton.core.abstracts.task import Task
from Zenaton.core.traits.zenatonable import Zenatonable


class TaskD(Task, Zenatonable):

    def handle(self):
        print('Task D')
        time.sleep(9)
        return 'Task D'
