import time

from Zenaton.core.abstracts.task import Task
from Zenaton.core.traits.zenatonable import Zenatonable


class DisplayTask(Zenatonable, Task):

    def __init__(self, counter):
        self.counter = counter

    def handle(self):
        print('DisplayTask: {}'.format(self.counter))
        time.sleep(1)
