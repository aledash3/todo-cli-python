from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from todo_cli.models import Task


class TaskUI:
    """
    Gestiona todos los componentes visuales de la aplicación.
    """

    def __init__(self) -> None:
        self.console = Console()

    def show_tasks(self, tasks: list[Task]) -> None:
        """
        Muestra todas las tareas en una tabla.
        """
        if not tasks:
            self.show_warning("No existen tareas registradas.")
            return

        table = Table(
            title="Lista de Tareas",
            show_lines=True,
            header_style="bold cyan",
        )

        table.add_column("ID", justify="center", style="cyan", no_wrap=True)
        table.add_column("Descripción", style="white")
        table.add_column("Estado", justify="center")

        for task in tasks:
            status = (
                "[green]✓ Completada[/green]"
                if task.completed
                else "[yellow]● Pendiente[/yellow]"
            )

            table.add_row(
                str(task.id),
                task.description,
                status,
            )

        self.console.print(table)

    def show_task(self, task: Task) -> None:
        """
        Muestra una única tarea.
        """
        table = Table(
            title="Información de la Tarea",
            header_style="bold cyan",
        )

        table.add_column("Campo")
        table.add_column("Valor")

        table.add_row("ID", str(task.id))
        table.add_row("Descripción", task.description)

        table.add_row(
            "Estado",
            "Completada" if task.completed else "Pendiente",
        )

        self.console.print(table)

    def show_success(self, message: str) -> None:
        """
        Muestra un mensaje de éxito.
        """
        self.console.print(
            Panel.fit(
                message,
                title="Éxito",
                border_style="green",
            )
        )

    def show_error(self, message: str) -> None:
        """
        Muestra un mensaje de error.
        """
        self.console.print(
            Panel.fit(
                message,
                title="Error",
                border_style="red",
            )
        )

    def show_warning(self, message: str) -> None:
        """
        Muestra un mensaje de advertencia.
        """
        self.console.print(
            Panel.fit(
                message,
                title="Aviso",
                border_style="yellow",
            )
        )

    def show_info(self, message: str) -> None:
        """
        Muestra un mensaje informativo.
        """
        self.console.print(
            Panel.fit(
                message,
                title="Información",
                border_style="blue",
            )
        )

    def show_statistics(
        self,
        total: int,
        pending: int,
        completed: int,
    ) -> None:
        """
        Muestra un resumen estadístico.
        """
        table = Table(
            title="Resumen",
            header_style="bold magenta",
        )

        table.add_column("Métrica")
        table.add_column("Valor", justify="center")

        table.add_row("Total de tareas", str(total))
        table.add_row(
            "Pendientes",
            f"[yellow]{pending}[/yellow]",
        )
        table.add_row(
            "Completadas",
            f"[green]{completed}[/green]",
        )

        self.console.print(table)

    def confirm(self, message: str) -> bool:
        """
        Solicita una confirmación al usuario.
        """
        response = (
            input(f"{message} [y/N]: ")
            .strip()
            .lower()
        )

        return response in {"y", "yes", "s", "si", "sí"}

    def print_header(self) -> None:
        """
        Imprime el encabezado principal.
        """
        self.console.print(
            Panel.fit(
                "[bold cyan]To-Do CLI[/bold cyan]\n"
                "Administrador de tareas",
                border_style="cyan",
            )
        )
