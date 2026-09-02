import json
from pathlib import Path
def save_to_json(jobs, filename="jobs.json"):
    path = Path(filename)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            old_jobs = json.load(f)
    else:
        old_jobs = []
    old_jobs.extend(jobs)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            old_jobs,
            f,
            ensure_ascii=False,
            indent=4
        )
