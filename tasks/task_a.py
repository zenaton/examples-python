import time

from zenaton.abstracts.task import Task
from zenaton.traits.zenatonable import Zenatonable


class TaskA(Task, Zenatonable):

    def handle(self):
        print('Task A starts')
        time.sleep(3)
        print('Task A ends')
        return 0
