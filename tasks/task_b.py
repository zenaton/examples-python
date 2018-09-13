import time

from Zenaton.core.abstracts.task import Task
from Zenaton.core.traits.zenatonable import Zenatonable


class TaskB(Task, Zenatonable):

    def handle(self):
        print('Task B starts')
        time.sleep(5)
        print('Task B ends')
        return 1
