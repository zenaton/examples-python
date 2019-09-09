<p align="center">
  <a href="https://zenaton.com" target="_blank">
    <img src="https://user-images.githubusercontent.com/36400935/58254828-e5176880-7d6b-11e9-9094-3f46d91faeee.png" target="_blank" />
  </a><br>
  Easy Asynchronous Jobs Manager for Developers <br>
  <a href="https://zenaton.com/documentation/python/getting-started/" target="_blank">
    <strong> Explore the docs » </strong>
  </a><br>
  <a href="https://zenaton.com" target="_blank"> Website </a>
    ·
  <a href="https://github.com/zenaton/zenaton-python" target="_blank"> Python Library </a>
    ·
  <a href="https://app.zenaton.com/tutorial/python" target="_blank"> Tutorial in Python </a> <br>
</p>


# Zenaton examples for Python

[Zenaton](https://zenaton.com) helps developers to easily run, monitor and orchestrate background jobs on your workers without managing a queuing system.
In addition to this, a monitoring dashboard shows you in real-time tasks executions and helps you to handle errors.

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
and populate it with your application id and api token found [here](https://app.zenaton.com/api).

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

## Example 1: Single task execution

[This example](https://github.com/zenaton/examples-python/tree/master/tasks/task_a.py) showcases

- A single execution of a task.

```python
python3 launch_task.py
```

## Example 2 : Sequential tasks execution
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/sequential_workflow.py) showcases
- a sequential execution of three tasks. The second and third tasks are executed only when the previous one is processed.
- In a sequential task execution, you can get the output of a task. The result of a task can be used by the next one.

<p align="center">
    <br>
    <img
        src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_sequential.png"
        width="324px"
        alt="Sequential Workflow Diagram"
    /> <img src="https://user-images.githubusercontent.com/36400935/58274921-30de0800-7d94-11e9-8e01-47d63f341147.gif" width="400px"/>
</p>

```python
python3 launch_sequential.py
```

## Example 3: Parallel tasks execution
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/parallel_workflow.py) showcases
- a parallel execution of 2 tasks
- a third task that is executed only after *both* first two tasks were processed

<p align="center">
    <img
        src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_parallel.png"
         width="324px"
        alt="Parallel Workflow Diagram"
    />
    <img src="https://user-images.githubusercontent.com/36400935/58277197-751fd700-7d99-11e9-8fff-d7c483c8abaf.gif" width="400px"/>
    
</p>

```python
python3 launch_parallel.py
```

## Example 4: Asynchronous tasks execution
[this example](https://github.com/zenaton/examples-python/tree/master/workflows/asynchronous_workflow.py) showcases
- Asynchronous executions of Task A and Task B (fire and forget)
- Then sequential executions of Task C and Task D

<p align="center">
    <img
        src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_async.png"
        width="324px"
        alt="Asynchronous Workflow Diagram"
    />
    <img src="https://user-images.githubusercontent.com/36400935/58277203-78b35e00-7d99-11e9-9ae8-cfa92757623f.gif" width="400px"/>
    
</p>

```python
python3 launch_asynchronous.py
```

When a task is dispatched asynchronously, the workflow continues its execution without waiting for the task completion. Consequently, a task asynchronous dispatching always returns a null value.

## Example 5: Event
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/event_workflow.py) showcases
- how to change a workflow's behaviour based on an external event

<p align="center">
    <img
        src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_react_event.png"
        width="324px"
        alt="Event Workflow Diagram"
    />
    <img src="https://user-images.githubusercontent.com/36400935/58276729-769ccf80-7d98-11e9-8ebc-d70ec82dd73b.gif" width="400px"/>
</p>

```python
python3 launch_event.py
```

## Example 6: Wait
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/wait_workflow.py) showcases
- how the provided `Wait` task can be used to pause the workflow for a specified duration

<p align="center">
    <img
        src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_wait.png"
        width="324px"
        alt="Wait Workflow Diagram"
    />
    <img src="https://user-images.githubusercontent.com/36400935/58276731-78669300-7d98-11e9-97b7-fbe0a39ecba0.gif" width="400px"/>
</p>
```python
python3 launch_wait.py
```

## Example 7: Wait Event
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/wait_event_workflow.py) showcases
- how the provided `Wait` task can also be used to pause the workflow up to receiving a specific external event

<p align="center">
    <img
        src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_wait_event.png"
        width="324px"
        alt="WaitEvent Workflow Diagram"
    />
    <img src="https://user-images.githubusercontent.com/36400935/58277648-7ac9ec80-7d9a-11e9-9b7b-58ca65809d00.gif" width="400px"/>
</p>
```python
python3 launch_wait_event.py
```

## Example 8: Recursive Workflow
[This example](https://github.com/zenaton/examples-python/tree/master/recursive/recursive_workflow.py) showcases
- how launching events or workflows directly from orchestrated tasks allows you to schedule recurring workflows

```python
python3 launch_recursive.py
```

## Example 9: Workflow Versions
[This example](https://github.com/zenaton/examples-python/tree/master/workflows/version_workflow.py) showcases
- how to update your workflow implementation, even while previous versions are still running

```python
python3 launch_version.py
```

## Example 10: Managing Errors

This example showcases

- how a failed task appear on Zenaton website
- how to retry a failed task using the retry button

<p align="center">
    <img
        src="https://raw.githubusercontent.com/zenaton/resources/master/examples/images/png/flow_error.png"
        width="324px"
        alt="Error Workflow Diagram"
    />
     <img src="https://user-images.githubusercontent.com/36400935/58315058-1007c800-7e11-11e9-8bbb-7b1fb8e5bdbb.gif" width="400px"/>
</p>

```python
python3 launch_error.py
```

## Example 11: Automatic retry of failed tasks
[This example](https://github.com/zenaton/examples-python/tree/master/tasks/task_with_retry.py) showcases
- how a failed task can be retried automatically
- how to customize the automatic retry policy
 ```python
python3 launch_automatic_retry.php
```

## Example 12: Schedule a task
[This example](https://github.com/zenaton/examples-python/tree/master/schedule_task_a.py) showcases
- how to schedule a task to make it run periodically
 ```python
python3 schedule_task_a.php
```

## Real-life Examples
__Triggering An Email After 3 Days of Cold Weather__ ([Medium Article](https://medium.com/zenaton/triggering-an-email-after-3-days-of-cold-weather-f7bed6f2df16), [Source Code](https://github.com/zenaton/articles-python/tree/master/triggering-an-email-after-3-days-of-cold-weather))
