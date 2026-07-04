1. Project Directory
Create a new directory for your project and navigate into it:

Bash
mkdir celery-hello-world
cd celery-hello-world
2. Install Dependencies
You need celery and the redis client library. It is recommended to use a virtual environment:

Bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

pip install celery redis
🏃‍♂️ Running Redis (The Broker)
Celery requires a message broker to pass messages between your application and the workers. We will use Redis.

If you don't have Redis installed locally, the easiest way to run it is via Docker:

Bash
docker run -d -p 6379:6379 redis
Alternatively, if you have Redis installed natively on your system, just start the service (e.g., redis-server).

📝 The Code
Since we want to keep it simple and avoid complex structures, we will put everything into a single file named tasks.py.

tasks.py
Python
from celery import Celery
import time

# Initialize Celery
# 'tasks' is the name of the current module
# broker: where tasks are sent
# backend: where results are stored
app = Celery(
    'tasks', 
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@app.task
def hello_world():
    time.sleep(2)  # Simulating a short delay/background work
    return "Hello, World! Celery is working perfectly."
🚀 How to Run and Test
To see Celery in action, you need two things running at the same time: the Celery Worker and a Python Script (or terminal) to trigger the task.

Step 1: Start the Celery Worker
Open a terminal window and run the following command to start the worker:

Bash
celery -A tasks worker --loglevel=info
Note for Windows Users: If you run into OS-specific issues on Windows, append -P threads or -P gevent to the command: celery -A tasks worker --loglevel=info -P threads

Step 2: Trigger the Task
Open a second terminal window, activate your virtual environment, and open an interactive Python shell:

Bash
python
Now, run the following code to queue your task:

Python
from tasks import hello_world

# Call the task asynchronously using .delay()
result = hello_world.delay()

# Check if the task is finished
print("Task completed?", result.ready())

# Wait and get the result
print("Result:", result.get())
If you look back at your first terminal (where the worker is running), you will see logs showing that the worker received and successfully executed the hello_world task!


