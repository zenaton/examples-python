import sys
import trace

from workflows.sequential_workflow import SequentialWorkflow
import client

tracer = trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix],trace=0,count=1)
tracer.runfunc(SequentialWorkflow().dispatch)

# SequentialWorkflow().dispatch()