from storage import TaskStorage

storage = TaskStorage()

def create_task(title):
    return storage.add_task(title)

def get_tasks():
    return storage.list_tasks()

def complete_task(task_id):
    return storage.complete_task(task_id)


if __name__ == "__main__":
    create_task("Learn Shipd")
    create_task("Submit tutorial")

    for task in get_tasks():
        print(task)