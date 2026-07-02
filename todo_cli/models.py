from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Task:
    """
    Representa una tarea dentro de la aplicación.
    """

    id: int
    description: str
    completed: bool = False

    def to_dict(self) -> dict:
        """
        Convierte la tarea en un diccionario serializable.
        """
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """
        Crea una instancia de Task a partir de un diccionario.
        """
        return cls(
            id=int(data["id"]),
            description=str(data["description"]),
            completed=bool(data["completed"]),
        )
