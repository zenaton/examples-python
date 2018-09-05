import time

import client
from events.my_event import MyEvent
from workflows.event_workflow import EventWorkflow

EventWorkflow().dispatch()

time.sleep(0.5)

EventWorkflow.where_id('MyId').send_event(event=MyEvent())
