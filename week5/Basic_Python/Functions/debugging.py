tasks = ["email", "report", "meeting", "call"]

new_task = []
for task in tasks:
    if "e" not in task:
        new_task.append(task)

print(new_task)
