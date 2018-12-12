# Zenaton examples for Python
This repository contains examples of workflows built with Zenaton. These examples illustrates how Zenaton orchestrates tasks that are executed on different workers.

## Installation
Download this repo
```
git clone https://github.com/zenaton/examples-python.git && cd examples-python
```
then add an .env file
```
cp .env.example .env
```
and populate it with your application id and api token found [here](https://zenaton.com/app/api).

Or use the `.env.example` file in this repo.

These a the minimal requirements to run the Zenaton client:

```
ZENATON_APP_ID=*****************
ZENATON_API_TOKEN=***************************
ZENATON_APP_ENV=dev
```
### Running Locally
Install dependencies
```
pip3 install -r requirements.txt
```
Then, you need to install a Zenaton worker
```
curl https://install.zenaton.com | sh
```
and start it, and make it listen to your configuration:
```
zenaton start; zenaton listen --env=.env --boot=boot.py
```
Your all set!

### Running on Docker
Simply run
```
docker-compose build; docker-compose up
```
 You're all set!

*Your workflows will be processed by your worker, so you won't see anything except the stdout and stderr, respectively `zenaton.out` and `zenaton.err`. Look at these files :)*

## Example 1 : Sequential tasks execution
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/sequential_workflow.py) showcases
- a sequential execution of three tasks. The second and third tasks are executed only when the previous one is processed.
- In a sequential task execution, you can get the output of a task. The result of a task can be used by the next one.

<p align="center">
    <img src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_sequential.png" alt="Sequential Workflow Diagram" />
</p>

```python
python3 launch_sequential.py
```

## Example 2: Parallel tasks execution
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/parallel_workflow.py) showcases
- a parallel execution of 2 tasks
- a third task that is executed only after *both* first two tasks were processed

<p align="center">
    <img src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_parallel.png" alt="Parallel Workflow Diagram" />
</p>

```python
python3 launch_parallel.py
```

## Example 3: Asynchronous tasks execution
[this example](https://github.com/zenaton/examples-python/tree/master/workflows/asynchronous_workflow.py) showcases
- Asynchronous executions of Task A and Task B (fire and forget)
- Then sequential executions of Task C and Task D

<p align="center">
    <img src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_async.png" alt="Asynchronous Workflow Diagram" />
</p>

```python
python3 launch_asynchronous.py
```

When a task is dispatched asynchronously, the workflow continues its execution without waiting for the task completion. Consequently, a task asynchronous dispatching always returns a null value.

## Example 4: Event
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/event_workflow.py) showcases
- how to change a workflow's behaviour based on an external event

<p align="center">
    <img src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_react_event.png" alt="Event Workflow Diagram" />
</p>

```python
python3 launch_event.py
```

## Example 5: Wait
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/wait_workflow.py) showcases
- how the provided `Wait` task can be used to pause the workflow for a specified duration

<p align="center">
    <img src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_wait.png" alt="Wait Workflow Diagram" />
</p>

```python
python3 launch_wait.py
```

## Example 6: Wait Event
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/wait_event_workflow.py) showcases
- how the provided `Wait` task can also be used to pause the workflow up to receiving a specific external event

<p align="center">
    <img src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_wait_event.png" alt="WaitEvent Workflow Diagram" />
</p>

```python
python3 launch_wait_event.py
```

## Example 7: Recursive Workflow
[This example](https://github.com/zenaton/examples-python/tree/master/recursive/recursive_workflow.py) showcases
- how launching events or workflows directly from orchestrated tasks allows you to schedule recurring workflows

```python
python3 launch_recursive.py
```

## Example 8: Workflow Versions
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/version_workflow.py) showcases
- how to update your workflow implementation, even while previous versions are still running

```python
python3 launch_version.py
```

## Real-life Examples
__Triggering An Email After 3 Days of Cold Weather__ ([Medium Article](https://medium.com/zenaton/triggering-an-email-after-3-days-of-cold-weather-f7bed6f2df16), [Source Code](https://github.com/zenaton/articles-python/tree/master/triggering-an-email-after-3-days-of-cold-weather))
