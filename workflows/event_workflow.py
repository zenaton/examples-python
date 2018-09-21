from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable

from events.my_event import MyEvent
from tasks.task_a import TaskA
from tasks.task_b import TaskB
from tasks.task_c import TaskC


class EventWorkflow(Workflow, Zenatonable):

    def __init__(self, id_, state=True):
        self.id_ = id_
        self.state = state

    def handle(self):
        TaskA().execute()
        if self.state:
            TaskB().execute()
        else:
            TaskC().execute()

    def on_event(self, event):
        if issubclass(MyEvent, type(event)):
            self.state = False

    def id(self):
        return self.id_
