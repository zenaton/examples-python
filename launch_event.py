import time
import uuid

import client
from events.my_event import MyEvent
from workflows.event_workflow import EventWorkflow

event_id = str(uuid.uuid4())
EventWorkflow(event_id).dispatch()
time.sleep(4)
EventWorkflow.where_id(event_id).send_event(event=MyEvent())
