import time

from zenaton.abstracts.task import Task
from zenaton.traits.zenatonable import Zenatonable


class TaskWithRetry(Task, Zenatonable):

    def handle(self):
        print('TaskWithRetry starts')
        time.sleep(3)
        raise Exception('TaskWithRetry Error')
        print('TaskWithRetry ends')

    def on_error_retry_delay(self, exception):
        # The retry index starts at 1 and increases by one for every retry.
        # This can be used to to increase the time between each attempt.
        n = self.get_context().retry_index
        if n > 3:
            return False

        return n * 5
