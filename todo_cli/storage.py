from __future__ import annotations

import json
from pathlib import Path

from todo_cli.models import Task


class JsonStorage:
    """
    Gestiona la persistencia de tareas mediante un archivo JSON.
    """

    def __init__(self, file_path: str | Path) -> None:
        self._file_path = Path(file_path)
        self._initialize_storage()

    def _initialize_storage(self) -> None:
        """
        Crea automáticamente el directorio y el archivo JSON
        si no existen.
        """
        self._file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self._file_path.exists():
            self._save_raw([])

    def _load_raw(self) -> list[dict]:
        """
        Lee el contenido bruto del archivo JSON.
        """
        try:
            with self._file_path.open(
                mode="r",
                encoding="utf-8",
            ) as file:
                return json.load(file)

        except json.JSONDecodeError:
            return []

    def _save_raw(self, data: list[dict]) -> None:
        """
        Guarda una lista de diccionarios en el archivo JSON.
        """
        with self._file_path.open(
            mode="w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def load_tasks(self) -> list[Task]:
        """
        Recupera todas las tareas almacenadas.
        """
        raw_tasks = self._load_raw()

        return [
            Task.from_dict(task)
            for task in raw_tasks
        ]

    def save_tasks(self, tasks: list[Task]) -> None:
        """
        Guarda la colección completa de tareas.
        """
        serialized_tasks = [
            task.to_dict()
            for task in tasks
        ]

        self._save_raw(serialized_tasks)

    def get_next_id(self) -> int:
        """
        Obtiene el siguiente ID disponible.
        """
        tasks = self.load_tasks()

        if not tasks:
            return 1

        return max(task.id for task in tasks) + 1

    def find_task(self, task_id: int) -> Task | None:
        """
        Busca una tarea por su identificador.
        """
        tasks = self.load_tasks()

        for task in tasks:
            if task.id == task_id:
                return task

        return None

    def task_exists(self, task_id: int) -> bool:
        """
        Verifica si una tarea existe.
        """
        return self.find_task(task_id) is not None

    def replace_task(self, updated_task: Task) -> bool:
        """
        Reemplaza una tarea existente.
        """
        tasks = self.load_tasks()

        for index, task in enumerate(tasks):
            if task.id == updated_task.id:
                tasks[index] = updated_task
                self.save_tasks(tasks)
                return True

        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Elimina una tarea por su ID.
        """
        tasks = self.load_tasks()

        remaining_tasks = [
            task
            for task in tasks
            if task.id != task_id
        ]

        if len(remaining_tasks) == len(tasks):
            return False

        self.save_tasks(remaining_tasks)

        return True

    def add_task(self, description: str) -> Task:
        """
        Crea y almacena una nueva tarea.
        """
        tasks = self.load_tasks()

        task = Task(
            id=self.get_next_id(),
            description=description.strip(),
            completed=False,
        )

        tasks.append(task)

        self.save_tasks(tasks)

        return task
