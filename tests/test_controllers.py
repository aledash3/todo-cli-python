import pytest

from todo_cli.controllers import (
    InvalidTaskDescriptionError,
    TaskAlreadyCompletedError,
    TaskController,
    TaskNotFoundError,
)
from todo_cli.storage import JsonStorage


@pytest.fixture
def controller(tmp_path):
    storage = JsonStorage(tmp_path / "tasks.json")
    return TaskController(storage)


def test_add_task_success_and_validation(controller):
    task = controller.add_task("Study SOLID principles")
    assert task.id == 1
    assert task.description == "Study SOLID principles"
    assert controller.task_count() == 1

    with pytest.raises(InvalidTaskDescriptionError):
        controller.add_task("   ")


def test_get_and_complete_task(controller):
    task = controller.add_task("Prepare demo")
    retrieved = controller.get_task(task.id)
    assert retrieved.id == task.id

    completed = controller.complete_task(task.id)
    assert completed.completed is True

    with pytest.raises(TaskAlreadyCompletedError):
        controller.complete_task(task.id)

    with pytest.raises(TaskNotFoundError):
        controller.get_task(999)


def test_delete_task(controller):
    task = controller.add_task("Temporary task")
    controller.delete_task(task.id)
    assert controller.task_count() == 0

    with pytest.raises(TaskNotFoundError):
        controller.delete_task(task.id)


def test_update_description(controller):
    task = controller.add_task("Old description")
    updated = controller.update_description(task.id, "New description")
    assert updated.description == "New description"

    with pytest.raises(InvalidTaskDescriptionError):
        controller.update_description(task.id, "   ")


def test_search_and_filter_tasks(controller):
    t1 = controller.add_task("Buy milk")
    controller.add_task("Buy bread")
    controller.add_task("Read book")
    controller.complete_task(t1.id)

    assert len(controller.pending_tasks()) == 2
    assert len(controller.completed_tasks()) == 1
    assert controller.pending_count() == 2
    assert controller.completed_count() == 1

    matches = controller.search_tasks("buy")
    assert len(matches) == 2

    no_matches = controller.search_tasks("workout")
    assert len(no_matches) == 0

    all_tasks = controller.search_tasks("")
    assert len(all_tasks) == 3


def test_clear_completed(controller):
    t1 = controller.add_task("Task 1")
    controller.add_task("Task 2")
    controller.complete_task(t1.id)

    removed = controller.clear_completed_tasks()
    assert removed == 1
    assert controller.task_count() == 1
    assert controller.has_tasks() is True

    # Clearing again when none are completed
    assert controller.clear_completed_tasks() == 0
