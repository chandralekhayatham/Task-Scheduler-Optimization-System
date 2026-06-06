import csv
from collections import defaultdict, deque
from metrics import calculate_metrics

def load_tasks(path="data/tasks.csv"):
    tasks = []

    with open(path) as f:
        for row in csv.DictReader(f):
            deps = [d for d in (row["depends_on"] or "").split("|") if d]

            tasks.append({
                "task_id": row["task_id"],
                "dur": int(row["duration_h"]),
                "ddl": int(row["deadline_h"]),
                "prio": int(row["priority"]),
                "skill": row["skill"],
                "deps": deps
            })

    return tasks


def load_resources(path="data/resources.csv"):
    resources = []

    with open(path) as f:
        for row in csv.DictReader(f):

            resources.append({
                "res_id": row["res_id"],
                "skills": set(row["skills"].split("|")),
                "start": int(row["shift_start_h"]),
                "end": int(row["shift_end_h"])
            })

    return resources


def greedy_schedule(tasks, resources):

    indeg = defaultdict(int)
    children = defaultdict(list)

    for task in tasks:
        for dep in task["deps"]:
            indeg[task["task_id"]] += 1
            children[dep].append(task["task_id"])

    queue = deque([
        task["task_id"]
        for task in tasks
        if indeg[task["task_id"]] == 0
    ])

    lookup = {t["task_id"]: t for t in tasks}

    topo = []

    while queue:

        ids = sorted(
            list(queue),
            key=lambda x: (
                -lookup[x]["prio"],
                lookup[x]["ddl"]
            )
        )

        current = ids[0]
        queue.remove(current)

        topo.append(current)

        for nxt in children[current]:
            indeg[nxt] -= 1

            if indeg[nxt] == 0:
                queue.append(nxt)

    plan = []
    current_time = 0

    for tid in topo:

        task = lookup[tid]

        plan.append({
            "task_id": tid,
            "start": current_time,
            "end": current_time + task["dur"]
        })

        current_time += task["dur"]

    return plan


if __name__ == "__main__":

    tasks = load_tasks()
    resources = load_resources()

    plan = greedy_schedule(tasks, resources)

    print("\nOptimized Schedule:\n")

    for p in plan:
        print(
            f"{p['task_id']} : "
            f"{p['start']} -> {p['end']}"
        )
        metrics = calculate_metrics(plan)
print("\nMetrics:")
print(metrics)