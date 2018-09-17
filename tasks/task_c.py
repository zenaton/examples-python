import time

from zenaton.abstracts.task import Task
from zenaton.traits.zenatonable import Zenatonable


class TaskC(Task, Zenatonable):

    def handle(self):
        print('Task C starts')
        time.sleep(7)
        print('Task C ends')
        return 2
