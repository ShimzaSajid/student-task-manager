class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if title is None or not title.strip():
            raise ValueError("Task title cannot be empty.")
        title = title.strip()
        task = {"id": self.next_id, "title": title, "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def complete_task(self, task_id):
        raise NotImplementedError("Coming in feature/complete-task")

    def get_tasks(self):
        return self.tasks

    def delete_task(self, task_id):
        raise NotImplementedError("Coming in feature/delete-task")