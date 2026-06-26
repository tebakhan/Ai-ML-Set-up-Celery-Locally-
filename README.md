Hello World using Celery
What is Celery?

Celery is a Python library used to run tasks in the background (asynchronously). Instead of making the main program wait for a task to finish, Celery sends the task to a worker. The worker executes it separately while the main program can continue doing other work.

Example:
Suppose a website needs to send an email after a user signs up. Sending the email may take a few seconds. Instead of making the user wait, the website sends the email task to Celery. Celery runs it in the background, and the user immediately gets the response.

What is Redis?

Redis acts as a message broker in this project.

Its job is to store the task temporarily and deliver it to the Celery worker.

In this project, Redis is also used as the result backend, which stores the result after the task is completed.

Code Explanation
Step 1: Import Required Libraries
from celery import Celery
import time
Celery is imported to create the Celery application.
time is used to simulate a delay.
Step 2: Create the Celery App
app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

Here we create a Celery application named tasks.

Broker → Redis receives the task and keeps it in the queue.
Backend → Redis stores the result after the task finishes.

Both broker and backend are connected to Redis running on localhost at port 6379.

Step 3: Create the Task
@app.task
def hello_world():

@app.task tells Celery that this function should run as a background task.

Without this decorator, Celery cannot execute the function asynchronously.

Step 4: Simulate Processing
time.sleep(2)

The task waits for 2 seconds.

This delay is only for demonstration purposes. In a real application, this could be:

Sending emails
Processing images
Generating reports
Uploading files
Step 5: Return the Result
return "Hello, World! Celery is working perfectly."

After completing the task, Celery returns this message.

Complete Flow
User Starts Task
        │
        ▼
hello_world.delay()
        │
        ▼
Redis (Stores Task)
        │
        ▼
Celery Worker
        │
        ▼
Runs hello_world()
        │
        ▼
Waits 2 Seconds
        │
        ▼
Returns Result
        │
        ▼
Redis Stores Result
        │
        ▼
User Gets Output
How to Run the Project
Step 1

Install dependencies

pip install celery redis
Step 2

Start Redis Server

redis-server

Redis starts listening on port 6379.

Step 3

Start Celery Worker

celery -A tasks worker --loglevel=info

The worker starts waiting for tasks.

Step 4

Run the Task

from tasks import hello_world

result = hello_world.delay()

print(result.get())
Output
Hello, World! Celery is working perfectly.
