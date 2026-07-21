import os
from datetime import datetime


class KanbanBoard:

    def __init__(self):

        self.tasks = [
            ["Search Ads", "⏳ Waiting"],
            ["Analyze Ads", "⏳ Waiting"],
            ["Generate Scripts", "⏳ Waiting"],
            ["Generate Videos", "⏳ Waiting"],
            ["Telegram Notification", "⏳ Waiting"],
        ]

    def update(self, task_name, status):

        for task in self.tasks:

            if task[0] == task_name:
                task[1] = status

        self.save()

    def save(self):

        os.makedirs("outputs/reports", exist_ok=True)

        path = "outputs/reports/kanban.md"

        with open(path, "w", encoding="utf-8") as f:

            f.write("# CrowdWisdom Hermes Kanban\n\n")

            f.write(
                f"Last Updated : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n"
            )

            f.write("| Task | Status |\n")
            f.write("|------|--------|\n")

            for task in self.tasks:

                f.write(f"| {task[0]} | {task[1]} |\n")