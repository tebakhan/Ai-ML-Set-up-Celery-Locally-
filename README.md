Hello World Celery Task
📌 Project Overview

This project demonstrates a simple Celery background task using Redis as both the message broker and the result backend.

The task waits for 2 seconds and then returns a success message. It is a basic example to understand how Celery executes asynchronous tasks.

🎯 Objective
Learn how Celery works.
Execute a background task asynchronously.
Connect Celery with Redis.
Retrieve the task result.
🛠 Technologies Used
Python
Celery
Redis
📂 Project Structure
project/
│── tasks.py
⚙️ Setup Process
1. Install Required Packages
pip install celery redis
2. Start Redis Server

Make sure Redis is running before starting Celery.

redis-server
3. Start Celery Worker

Open a new terminal and run:

celery -A tasks worker --loglevel=info
4. Run the Task

Open Python shell:

from tasks import hello_world

result = hello_world.delay()

print(result.get())
🔄 How It Works
The Celery application is created.
Redis is used as the message broker and result backend.
The hello_world task is sent to the queue.
The Celery worker picks up the task.
The task waits for 2 seconds using time.sleep(2).
Finally, it returns the message:
Hello, World! Celery is working perfectly.
📌 Expected Output
Hello, World! Celery is working perfectly.
📖 Learning Outcome

After completing this project, you will understand:

What Celery is.
How background tasks are executed.
How Redis works with Celery.
How to run a Celery worker.
How to trigger asynchronous tasks and receive their results.
