import time

from zenaton.abstracts.task import Task
from zenaton.traits.zenatonable import Zenatonable


class TaskD(Task, Zenatonable):

    def handle(self):
        print('Task D starts')
        time.sleep(9)
        print('Task D ends')
        return 3
