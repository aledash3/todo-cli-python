from pathlib import Path

from todo_cli.storage import JsonStorage, TaskStorage, get_default_storage_path


def test_storage_implements_protocol(tmp_path):
    storage = JsonStorage(tmp_path / "tasks.json")
    assert isinstance(storage, TaskStorage)


def test_initialize_and_save_load(tmp_path):
    file_path = tmp_path / "subdir" / "tasks.json"
    storage = JsonStorage(file_path)
    assert file_path.exists()
    assert storage.load_tasks() == []

    task = storage.add_task("First task")
    assert task.id == 1
    assert task.description == "First task"
    assert len(storage.load_tasks()) == 1


def test_storage_handles_corrupted_json(tmp_path):
    file_path = tmp_path / "corrupted.json"
    file_path.write_text("invalid json content {{{", encoding="utf-8")

    storage = JsonStorage(file_path)
    assert storage.load_tasks() == []


def test_storage_find_and_replace(tmp_path):
    storage = JsonStorage(tmp_path / "tasks.json")
    task = storage.add_task("Task to modify")

    found = storage.find_task(task.id)
    assert found is not None
    assert found.description == "Task to modify"

    found.description = "Updated description"
    found.completed = True
    assert storage.replace_task(found) is True

    reloaded = storage.find_task(task.id)
    assert reloaded.description == "Updated description"
    assert reloaded.completed is True


def test_storage_delete_task(tmp_path):
    storage = JsonStorage(tmp_path / "tasks.json")
    task = storage.add_task("Task to delete")
    assert storage.task_exists(task.id) is True

    assert storage.delete_task(task.id) is True
    assert storage.task_exists(task.id) is False
    assert storage.delete_task(999) is False


def test_get_default_storage_path_env(monkeypatch, tmp_path):
    custom_path = str(tmp_path / "env_tasks.json")
    monkeypatch.setenv("TODO_CLI_PATH", custom_path)
    resolved = get_default_storage_path()
    assert resolved == Path(custom_path)
