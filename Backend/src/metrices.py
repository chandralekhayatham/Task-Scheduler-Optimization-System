def calculate_metrics(plan):

    total_duration = 0

    for task in plan:
        total_duration += (
            task["end"] - task["start"]
        )

    return {
        "total_tasks": len(plan),
        "total_duration": total_duration
    }