from Zenaton.core.abstracts.task import Task
from Zenaton.core.traits.zenatonable import Zenatonable

from .ending_event import EndingEvent


class SendEventTask(Zenatonable, Task):

    def __init__(self, send_id):
        self.send_id = send_id

    def handle(self):
        from .recursive_workflow import RecursiveWorkflow
        RecursiveWorkflow.where_id(self.send_id).send_event(EndingEvent())
