from celery import Celery
import time

# Initialize Celery app instance and configure local Redis broker & backend
app = Celery(
    'my_first_celery_app', 
    broker='redis://localhost:6379/0',   # Used to send and route tasks
    backend='redis://localhost:6379/0'   # Used to track and retrieve task states
)

# Registering a basic background task
@app.task
def hello_world():
    print("Task processing started...")
    time.sleep(2)  # Simulating a heavy data processing or background work load
    return "Hello, World! Celery and Redis are working perfectly."
