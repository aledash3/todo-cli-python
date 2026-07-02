from __future__ import annotations

from pathlib import Path

from todo_cli.models import Task
from todo_cli.storage import JsonStorage


class TaskNotFoundError(Exception):
    """
    Se lanza cuando una tarea no existe.
    """


class InvalidTaskDescriptionError(Exception):
    """
    Se lanza cuando la descripción de una tarea es inválida.
    """


class TaskAlreadyCompletedError(Exception):
    """
    Se lanza cuando una tarea ya se encuentra completada.
    """


class TaskController:
    """
    Controlador encargado de la lógica de negocio de la aplicación.
    """

    def __init__(self, storage: JsonStorage) -> None:
        self._storage = storage

    @classmethod
    def create_default(cls) -> "TaskController":
        """
        Crea una instancia del controlador utilizando el
        almacenamiento por defecto.
        """
        storage = JsonStorage(Path("data/tasks.json"))
        return cls(storage)

    def add_task(self, description: str) -> Task:
        """
        Agrega una nueva tarea.
        """
        description = description.strip()

        if not description:
            raise InvalidTaskDescriptionError(
                "La descripción de la tarea no puede estar vacía."
            )

        return self._storage.add_task(description)

    def list_tasks(self) -> list[Task]:
        """
        Devuelve todas las tareas almacenadas.
        """
        return sorted(
            self._storage.load_tasks(),
            key=lambda task: task.id,
        )

    def get_task(self, task_id: int) -> Task:
        """
        Obtiene una tarea por su ID.
        """
        task = self._storage.find_task(task_id)

        if task is None:
            raise TaskNotFoundError(
                f"No existe una tarea con ID {task_id}."
            )

        return task

    def complete_task(self, task_id: int) -> Task:
        """
        Marca una tarea como completada.
        """
        task = self.get_task(task_id)

        if task.completed:
            raise TaskAlreadyCompletedError(
                f"La tarea {task_id} ya está completada."
            )

        task.completed = True

        self._storage.replace_task(task)

        return task

    def delete_task(self, task_id: int) -> None:
        """
        Elimina una tarea.
        """
        deleted = self._storage.delete_task(task_id)

        if not deleted:
            raise TaskNotFoundError(
                f"No existe una tarea con ID {task_id}."
            )

    def pending_tasks(self) -> list[Task]:
        """
        Devuelve únicamente las tareas pendientes.
        """
        return [
            task
            for task in self.list_tasks()
            if not task.completed
        ]

    def completed_tasks(self) -> list[Task]:
        """
        Devuelve únicamente las tareas completadas.
        """
        return [
            task
            for task in self.list_tasks()
            if task.completed
        ]

    def task_count(self) -> int:
        """
        Devuelve el número total de tareas.
        """
        return len(self.list_tasks())

    def pending_count(self) -> int:
        """
        Devuelve el número de tareas pendientes.
        """
        return len(self.pending_tasks())

    def completed_count(self) -> int:
        """
        Devuelve el número de tareas completadas.
        """
        return len(self.completed_tasks())

    def has_tasks(self) -> bool:
        """
        Indica si existen tareas registradas.
        """
        return self.task_count() > 0

    def clear_completed_tasks(self) -> int:
        """
        Elimina todas las tareas completadas.

        Returns
        -------
        int
            Número de tareas eliminadas.
        """
        tasks = self.list_tasks()

        remaining_tasks = [
            task
            for task in tasks
            if not task.completed
        ]

        removed = len(tasks) - len(remaining_tasks)

        if removed > 0:
            self._storage.save_tasks(remaining_tasks)

        return removed

    def update_description(
        self,
        task_id: int,
        new_description: str,
    ) -> Task:
        """
        Actualiza la descripción de una tarea.
        """
        new_description = new_description.strip()

        if not new_description:
            raise InvalidTaskDescriptionError(
                "La descripción no puede estar vacía."
            )

        task = self.get_task(task_id)

        task.description = new_description

        self._storage.replace_task(task)

        return task
