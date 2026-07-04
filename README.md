# Hello World using Celery

## 📌 Overview

This project demonstrates a basic Celery background task using Redis as the message broker and result backend.

The task waits for 2 seconds and then returns a simple message.

---

## 🛠 Technologies Used

- Python
- Celery
- Redis

---

## 📂 Project Files

```
tasks.py
```

---

## ⚙️ How It Works

1. A Celery application is created.
2. Redis is configured as the broker and result backend.
3. The `hello_world` task is registered using `@app.task`.
4. When the task is called, the Celery worker executes it in the background.
5. The task waits for 2 seconds and returns a success message.

---

## ▶️ Steps to Run

### 1. Install the required packages

```bash
pip install celery redis
```

### 2. Start Redis

```bash
redis-server
```

### 3. Start the Celery Worker

```bash
celery -A tasks worker --loglevel=info
```

### 4. Run the Task

```python
from tasks import hello_world

result = hello_world.delay()
print(result.get())
```

---

## ✅ Expected Output

```
Hello, World! Celery is working perfectly.
```

---

## 📖 Conclusion
This project is a simple example of how Celery executes tasks asynchronously using Redis. It helps in understanding the basic workflow of background task processing.

This project is a simple example of how Celery executes tasks asynchronously using Redis. It helps in understanding the basic workflow of background task processing.
