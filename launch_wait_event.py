import time
import uuid

import client
from workflows.wait_event_workflow import WaitEventWorkflow
from events.my_event import MyEvent

event_id = str(uuid.uuid4())

WaitEventWorkflow(event_id).dispatch()

time.sleep(2)

WaitEventWorkflow.where_id(event_id).send_event(event=MyEvent())
