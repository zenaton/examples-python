import time

import client
from workflows.wait_event_workflow import WaitEventWorkflow
from events.my_event import MyEvent

WaitEventWorkflow().dispatch()

time.sleep(2)

WaitEventWorkflow.where_id('MyId').send_event(event=MyEvent())
