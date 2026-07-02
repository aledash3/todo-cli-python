from __future__ import annotations

import typer
from rich.console import Console

from todo_cli.controllers import (
    InvalidTaskDescriptionError,
    TaskAlreadyCompletedError,
    TaskController,
    TaskNotFoundError,
)
from todo_cli.ui import TaskUI

app = typer.Typer(
    name="todo",
    help="Aplicación CLI para la gestión de tareas.",
    add_completion=False,
)

console = Console()
controller = TaskController.create_default()
ui = TaskUI()


@app.command("add")
def add_task(description: str) -> None:
    """
    Agrega una nueva tarea.
    """
    try:
        task = controller.add_task(description)

        ui.show_success(
            f"Tarea agregada correctamente.\n\n"
            f"ID: {task.id}\n"
            f"Descripción: {task.description}"
        )

    except InvalidTaskDescriptionError as error:
        ui.show_error(str(error))
        raise typer.Exit(code=1)


@app.command("list")
def list_tasks() -> None:
    """
    Lista todas las tareas.
    """
    tasks = controller.list_tasks()

    ui.show_tasks(tasks)
    ui.show_statistics(
        total=controller.task_count(),
        pending=controller.pending_count(),
        completed=controller.completed_count(),
    )


@app.command("complete")
def complete_task(task_id: int) -> None:
    """
    Marca una tarea como completada.
    """
    try:
        task = controller.complete_task(task_id)

        ui.show_success(
            f"La tarea #{task.id} fue marcada como completada."
        )

    except (
        TaskNotFoundError,
        TaskAlreadyCompletedError,
    ) as error:
        ui.show_error(str(error))
        raise typer.Exit(code=1)


@app.command("remove")
def remove_task(task_id: int) -> None:
    """
    Elimina una tarea.
    """
    try:
        task = controller.get_task(task_id)

        if not ui.confirm(
            f"¿Desea eliminar la tarea #{task.id}?"
        ):
            ui.show_warning("Operación cancelada.")
            return

        controller.delete_task(task_id)

        ui.show_success(
            f"La tarea #{task_id} fue eliminada."
        )

    except TaskNotFoundError as error:
        ui.show_error(str(error))
        raise typer.Exit(code=1)


@app.command("show")
def show_task(task_id: int) -> None:
    """
    Muestra una tarea específica.
    """
    try:
        task = controller.get_task(task_id)
        ui.show_task(task)

    except TaskNotFoundError as error:
        ui.show_error(str(error))
        raise typer.Exit(code=1)


@app.command("pending")
def pending_tasks() -> None:
    """
    Lista únicamente las tareas pendientes.
    """
    tasks = controller.pending_tasks()

    ui.show_tasks(tasks)

    ui.show_statistics(
        total=len(tasks),
        pending=len(tasks),
        completed=0,
    )


@app.command("completed")
def completed_tasks() -> None:
    """
    Lista únicamente las tareas completadas.
    """
    tasks = controller.completed_tasks()

    ui.show_tasks(tasks)

    ui.show_statistics(
        total=len(tasks),
        pending=0,
        completed=len(tasks),
    )


@app.command("update")
def update_task(
    task_id: int,
    description: str,
) -> None:
    """
    Actualiza la descripción de una tarea.
    """
    try:
        task = controller.update_description(
            task_id,
            description,
        )

        ui.show_success(
            f"La tarea #{task.id} fue actualizada."
        )

    except (
        TaskNotFoundError,
        InvalidTaskDescriptionError,
    ) as error:
        ui.show_error(str(error))
        raise typer.Exit(code=1)


@app.command("clear-completed")
def clear_completed() -> None:
    """
    Elimina todas las tareas completadas.
    """
    removed = controller.clear_completed_tasks()

    if removed == 0:
        ui.show_warning(
            "No existen tareas completadas."
        )
        return

    ui.show_success(
        f"Se eliminaron {removed} tarea(s) completada(s)."
    )


@app.command("stats")
def statistics() -> None:
    """
    Muestra estadísticas generales.
    """
    ui.show_statistics(
        total=controller.task_count(),
        pending=controller.pending_count(),
        completed=controller.completed_count(),
    )


@app.command("version")
def version() -> None:
    """
    Muestra la versión de la aplicación.
    """
    console.print(
        "[bold green]To-Do CLI[/bold green] v1.0.0"
    )


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """
    Punto de entrada principal.
    """
    if ctx.invoked_subcommand is None:
        ui.print_header()
        console.print()
        console.print(
            "[bold cyan]Comandos disponibles:[/bold cyan]"
        )
        console.print("  add")
        console.print("  list")
        console.print("  show")
        console.print("  complete")
        console.print("  remove")
        console.print("  update")
        console.print("  pending")
        console.print("  completed")
        console.print("  clear-completed")
        console.print("  stats")
        console.print("  version")
        console.print()
        console.print(
            "Ejecute [bold]todo --help[/bold] para más información."
        )


if __name__ == "__main__":
    app()
