from Zenaton.core.workflows.version import Version
from .version_workflow_v0 import VersionWorkflowV0
from .version_workflow_v1 import VersionWorkflowV1
from .version_workflow_v2 import VersionWorkflowV2


class VersionWorkflow(Version):

    def versions(self):
        return [
            VersionWorkflowV0,
            VersionWorkflowV1,
            VersionWorkflowV2
        ]
