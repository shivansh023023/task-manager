from models import Task

class TaskStorage:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False