import sys

from ...client import Client
from .recursive_workflow import RecursiveWorkflow

RecursiveWorkflow.where_id(sys.argv[0]).kill()
