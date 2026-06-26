from celery import Celery
import time

# 1. Celery ko initialize karein aur Redis broker set karein
# Broker: Jo tasks ko queue mein le jata hai
# Backend: Jo task ka result store karta hai
app = Celery(
    'my_first_celery_app', 
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

# 2. Ek simple background task define karein
@app.task
def hello_world():
    print("Task start ho raha hai...")
    time.sleep(2)  # 2 second ka delay (heavy background work simulate karne ke liye)
    return "Hello, World! Celery aur Redis perfectly kaam kar rahe hain."