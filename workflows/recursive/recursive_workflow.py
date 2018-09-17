from zenaton.tasks.wait import Wait
from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable

from workflows.recursive.display_task import DisplayTask
from workflows.recursive.send_event_task import SendEventTask
from workflows.recursive.relaunch_task import RelaunchTask
from workflows.recursive.ending_event import EndingEvent


class RecursiveWorkflow(Workflow, Zenatonable):

    def __init__(self, workflow_id, max):
        self.workflow_id = workflow_id
        self.max = max

    def handle(self):
        counter = 0
        while counter < 3:
            DisplayTask(counter).execute()
            counter += 1
        SendEventTask(self.workflow_id).dispatch()
        Wait(EndingEvent).execute()
        RelaunchTask(self.workflow_id, self.max).execute()

    def id(self):
        return self.workflow_id
