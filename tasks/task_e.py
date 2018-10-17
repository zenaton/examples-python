from zenaton.abstracts.task import Task
from zenaton.traits.zenatonable import Zenatonable


class TaskE(Task, Zenatonable):

    def handle(self):
        print('Task E starts')
        print('Task E ends')
        return 0
