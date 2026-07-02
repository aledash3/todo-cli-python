# ✅ To-Do CLI - Professional Command Line Task Manager

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
![Typer](https://img.shields.io/badge/Typer-CLI-green?style=for-the-badge)
![Rich](https://img.shields.io/badge/Rich-Terminal-purple?style=for-the-badge)
![JSON](https://img.shields.io/badge/Storage-JSON-orange?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-Layered-red?style=for-the-badge)

------------------------------------------------------------------------

# 📌 Descripción General

Este repositorio contiene el desarrollo de una aplicación **To-Do List**
para la interfaz de línea de comandos (CLI), desarrollada en **Python
3.13** utilizando una arquitectura en capas, principios **SOLID**,
buenas prácticas **PEP 8** y persistencia local mediante archivos JSON.

La aplicación permite administrar tareas desde la terminal mediante
comandos intuitivos, proporcionando una solución ligera, modular y
fácilmente extensible.

------------------------------------------------------------------------

# 🎯 Objetivos

## Objetivo General

Desarrollar una aplicación CLI para la gestión de tareas utilizando una
arquitectura profesional y buenas prácticas de desarrollo en Python.

## Objetivos Específicos

-   Implementar una arquitectura en capas.
-   Separar la lógica de negocio, persistencia e interfaz.
-   Gestionar tareas mediante comandos CLI.
-   Persistir información utilizando JSON.
-   Aplicar principios SOLID.
-   Mantener compatibilidad con Python 3.13.

------------------------------------------------------------------------

# 🏗️ Arquitectura

``` text
todo_cli_project/
├── .vscode/
│   └── settings.json
├── data/
│   └── tasks.json
├── todo_cli/
│   ├── __init__.py
│   ├── controllers.py
│   ├── main.py
│   ├── models.py
│   ├── storage.py
│   └── ui.py
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Capas

-   Presentación (CLI): Typer + Rich
-   Lógica de negocio: Controller
-   Persistencia: JSON
-   Modelo: Dataclass Task

------------------------------------------------------------------------

# ⚙️ Tecnologías

  Tecnología    Uso
  ------------- ----------------------
  Python 3.13   Lenguaje principal
  Typer         CLI
  Rich          Interfaz de terminal
  JSON          Persistencia
  Ruff          Formateo y linting

------------------------------------------------------------------------

# ✨ Funcionalidades

-   Agregar tareas.
-   Listar tareas.
-   Marcar tareas como completadas.
-   Actualizar descripción.
-   Eliminar tareas.
-   Consultar estadísticas.
-   Mostrar tareas pendientes.
-   Mostrar tareas completadas.
-   Persistencia automática de la información.

------------------------------------------------------------------------

# ⚙️ Requisitos

## Software

-   Python 3.13 o superior
-   Visual Studio Code (opcional)

## Dependencias

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# 🚀 Instalación

## 1. Clonar el repositorio

``` bash
git clone https://github.com/aledash3/todo-cli-python.git
```

## 2. Acceder al proyecto

``` bash
cd todo-cli-python
```

## 3. Crear un entorno virtual

### Linux

``` bash
python3.13 -m venv .venv
source .venv/bin/activate
```

### Windows

``` powershell
python -m venv .venv
.venv\Scripts\activate
```

## 4. Instalar las dependencias

``` bash
pip install -r requirements.txt
```

## 5. Instalar el comando global del proyecto

``` bash
pip install -e .
```

------------------------------------------------------------------------

# ▶️ Ejecución

## Utilizando el comando `todo`

``` bash
todo --help
```

### Ejemplos

``` bash
todo add "Comprar leche"
todo list
todo show 1
todo complete 1
todo update 1 "Comprar leche descremada"
todo pending
todo completed
todo stats
todo remove 1
todo clear-completed
todo version
```

## Sin instalar el comando `todo`

``` bash
python -m todo_cli.main --help
```

### Ejemplos

``` bash
python -m todo_cli.main add "Comprar leche"
python -m todo_cli.main list
python -m todo_cli.main show 1
python -m todo_cli.main complete 1
python -m todo_cli.main update 1 "Comprar leche descremada"
python -m todo_cli.main pending
python -m todo_cli.main completed
python -m todo_cli.main stats
python -m todo_cli.main remove 1
python -m todo_cli.main clear-completed
python -m todo_cli.main version
```

------------------------------------------------------------------------

# 📂 Persistencia

Las tareas se almacenan automáticamente en:

``` text
data/tasks.json
```

Formato:

``` json
[
    {
        "id": 1,
        "description": "Comprar leche",
        "completed": false
    }
]
```

------------------------------------------------------------------------

# 🧩 Principios Aplicados

-   Arquitectura en capas.
-   Principios SOLID.
-   Estándar PEP 8.
-   Programación Orientada a Objetos.
-   Type Hints.
-   Manejo de excepciones.
-   Persistencia desacoplada mediante JSON.

------------------------------------------------------------------------

# 👨‍💻 Autor

**David Alejandro Cruz Palacios**

Carrera de Ciencias de la Computación

Facultad de Ingeniería

Universidad Politécnica Salesiana

Quito, Ecuador

GitHub: https://github.com/aledash3

------------------------------------------------------------------------

# 📜 Licencia

Este proyecto fue desarrollado con fines académicos y educativos.

Todos los derechos pertenecen a su autor.

Su utilización es libre para fines de aprendizaje, estudio y consulta,
conservando el reconocimiento de la autoría original.
