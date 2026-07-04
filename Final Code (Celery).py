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
