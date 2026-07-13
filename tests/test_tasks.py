import os
import sys

# Add the project root to Python's import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_task, get_tasks, complete_task


def test_create_task():
    task = create_task("Write tests")
    assert task.title == "Write tests"


def test_complete():
    task = create_task("Finish tutorial")
    assert complete_task(task.id) is True


def test_list():
    assert len(get_tasks()) >= 0