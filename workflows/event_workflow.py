from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable

from events.my_event import MyEvent
from tasks.task_a import TaskA
from tasks.task_b import TaskB
from tasks.task_c import TaskC


class EventWorkflow(Workflow, Zenatonable):

    def __init__(self, id_):
        self.id_ = id_

    def handle(self):
        TaskA().execute()
        TaskB().execute()

    def on_event(self, event):
        if issubclass(MyEvent, type(event)):
            TaskC().execute()

    def id(self):
        return self.id_
