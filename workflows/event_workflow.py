from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable

from events.my_event import MyEvent
from tasks.task_a import TaskA
from tasks.task_b import TaskB
from tasks.task_c import TaskC


class EventWorkflow(Workflow, Zenatonable):

    def handle(self):
        TaskA().execute()
        TaskB().execute()

    def on_event(self, event):
        if issubclass(MyEvent, type(event)):
            TaskC().execute()

    def id(self):
        return 'MyId5'
