import csv
from pathlib import Path
def save_to_csv(jobs, filename="jobs.csv"):
    if not jobs:
        return
    file_exists = Path(filename).exists()
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=jobs[0].keys())
        if not file_exists:
            writer.writeheader()
        writer.writerows(jobs)
