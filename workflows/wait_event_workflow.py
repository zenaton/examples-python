import Zenaton
from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable
from Zenaton.core.tasks.wait import Wait

from tasks.task_a import TaskA
from tasks.task_b import TaskB
from events.my_event import MyEvent


class WaitEventWorkflow(Workflow, Zenatonable):

    def handle(self):

        event = Wait(MyEvent).seconds(4.0).execute()

        if event:
            TaskA().execute()
        else:
            TaskB().execute()

    def id(self):
        return 'MyId40'
