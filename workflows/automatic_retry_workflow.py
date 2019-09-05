from tasks.task_with_retry import TaskWithRetry

from zenaton.abstracts.workflow import Workflow
from zenaton.traits.zenatonable import Zenatonable


class AutomaticRetryWorkflow(Workflow, Zenatonable):

    def handle(self):
        TaskWithRetry().execute()
