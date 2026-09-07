from todo_cli.models import Task


def test_task_creation():
    task = Task(id=1, description="Buy groceries")
    assert task.id == 1
    assert task.description == "Buy groceries"
    assert task.completed is False


def test_task_to_dict():
    task = Task(id=2, description="Write tests", completed=True)
    assert task.to_dict() == {
        "id": 2,
        "description": "Write tests",
        "completed": True,
    }


def test_task_from_dict():
    data = {"id": "3", "description": "Read documentation", "completed": 0}
    task = Task.from_dict(data)
    assert task.id == 3
    assert task.description == "Read documentation"
    assert task.completed is False
