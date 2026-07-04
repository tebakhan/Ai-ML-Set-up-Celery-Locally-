🛠️ Environment Setup & Installation
1. Initialize the Directory & Virtual Environment
Clone the repository, navigate into the project directory, and initialize a local Python virtual environment to manage dependencies safely:

Bash
git clone [https://github.com/tebakhan/Ai-ML-Set-up-Celery-Locally-](https://github.com/tebakhan/Ai-ML-Set-up-Celery-Locally-)
cd Ai-ML-Set-up-Celery-Locally-

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
2. Install Project Dependencies
Install the required framework packages via pip:

Bash
pip install celery redis
3. Spin Up the Redis Broker
Launch an isolated instance of Redis locally. The cleanest and most stable approach is running it via Docker:

Bash
docker run -d -p 6379:6379 redis
📄 Code Implementation Overview (tasks.py)
To satisfy project constraints and avoid over-engineering, the initialization, routing configuration, and task definitions are kept inside a single file:

Python
from celery import Celery
import time

# Initialize the Celery application
# 'tasks' matches the current module name
app = Celery(
    'tasks', 
    broker='redis://localhost:6379/0',   # Location where tasks are sent
    backend='redis://localhost:6379/0'   # Location where execution results are tracked
)

# Register a basic background task using the app decorator
@app.task
def hello_world():
    print("Background task execution started...")
    time.sleep(2)  # Simulating 2 seconds of heavy computational background work
    return "Hello, World! Celery and Redis are working perfectly."
🚀 Execution & Verification Steps
To demonstrate the asynchronous capabilities of the setup, open two separate terminal windows side-by-side:

Step 1: Start the Celery Worker (Terminal 1)
Run the worker process so it can sit in the background and listen for incoming messages:

Bash
celery -A tasks worker --loglevel=info
💡 Windows Troubleshooting Note: If your environment encounters native OS processing blockades or execution locks, append the explicit thread execution pool flag instead:
celery -A tasks worker --loglevel=info -P threads

Step 2: Trigger the Asynchronous Task (Terminal 2)
Open an interactive Python shell session to push a task to the queue live:

Bash
python
Run the following script line-by-line inside the interactive interpreter:

Python
from tasks import hello_world

# Call the task asynchronously using .delay()
result = hello_world.delay()

# Check the current status of the task queue instantly (Returns True or False)
print("Is the task execution complete?:", result.ready())

# Wait and fetch the final returned message output from the backend
print("Result Output:", result.get())
