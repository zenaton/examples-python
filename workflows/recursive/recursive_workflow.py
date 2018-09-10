from Zenaton.core.tasks.wait import Wait
from Zenaton.core.abstracts.workflow import Workflow
from Zenaton.core.traits.zenatonable import Zenatonable

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
        print('Step 1: Display Task Loop')
        while counter < 10:
            DisplayTask(counter).execute()
            counter += 1
        print('Step 2: SendEventTask')
        SendEventTask(self.workflow_id).dispatch()
        print('Step 3: Wait Task')
        Wait(EndingEvent).execute()
        print('Step 4: Relaunch Task')
        RelaunchTask(self.workflow_id, self.max).execute()

    def id(self):
        return self.workflow_id
