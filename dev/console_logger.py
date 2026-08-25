from datetime import datetime

def log(msg):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] {msg}")
