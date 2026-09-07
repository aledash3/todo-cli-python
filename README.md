# ✅ To-Do CLI — Professional Task Manager

<p align="center">
  <a href="https://github.com/aledash3/todo-cli-python/actions/workflows/ci.yml">
    <img src="https://github.com/aledash3/todo-cli-python/actions/workflows/ci.yml/badge.svg" alt="CI Status">
  </a>
  <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue?logo=python&logoColor=white" alt="Python Versions">
  <img src="https://img.shields.io/badge/CLI-Typer-green.svg" alt="Typer">
  <img src="https://img.shields.io/badge/Terminal-Rich-purple.svg" alt="Rich">
  <img src="https://img.shields.io/badge/Tests-Pytest-yellow.svg" alt="Pytest">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
  <a href="README.es.md">
    <img src="https://img.shields.io/badge/lang-Espa%C3%B1ol-yellow.svg" alt="Leer en Español">
  </a>
</p>

A lightweight, robust, and extensible command-line task management application built in Python using **Typer**, **Rich**, and a layered **SOLID** architecture. Features portable JSON persistence, case-insensitive keyword search, non-interactive scriptability (`--yes`), rich terminal tables, and 100% automated test coverage.

> 🌐 **Language / Idioma:** English | [Leer documentación en Español](README.es.md)

---

## 📌 Overview

**To-Do CLI** is engineered for developers and terminal power users who want a distraction-free, reliable task tracking system directly inside their shell. Built with enterprise software engineering standards, it decouples user interface, domain logic, and data persistence behind abstract protocols (DIP in SOLID).

---

## 🎯 Key Architectural Highlights

- **Layered Architecture:** Clear separation of concerns between CLI Presentation (`typer` + `rich`), Domain Controller, Abstract Storage Protocol, and Models (`Task` dataclass).
- **SOLID Compliance:** Implements the **Dependency Inversion Principle (DIP)** with a runtime-checkable `TaskStorage` Protocol, enabling pluggable backends (JSON, SQLite, In-Memory) without modifying business logic.
- **Smart Path Resolution:** Stores user tasks in `~/.todo_cli/tasks.json` by default (or customizable via `TODO_CLI_PATH` environment variable and local `./data/tasks.json` fallback).
- **Automation Ready:** Commands like `remove` and `clear-completed` support the `--yes / -y` flag for seamless shell scripting and CI/CD pipelines.
- **Broad Compatibility:** Supports **Python 3.10, 3.11, 3.12, and 3.13**.
- **Production Tested:** Complete test suite covering models, storage resilience (corrupted file recovery), business rules, and CLI invocation via `CliRunner`.

---

## 🏗 System Architecture

```text
todo-cli-python/
├── .github/
│   └── workflows/
│       └── ci.yml               # Multi-version CI matrix (Python 3.10 - 3.13)
├── tests/
│   ├── test_cli.py              # CLI integration tests via CliRunner
│   ├── test_controllers.py      # Business logic & error handling unit tests
│   ├── test_models.py           # Dataclass serialization unit tests
│   └── test_storage.py          # Persistence, corrupt JSON recovery & protocol tests
├── todo_cli/
│   ├── __init__.py              # Package entry point
│   ├── controllers.py           # TaskController business logic
│   ├── main.py                  # Typer CLI commands & argument handling
│   ├── models.py                # Task dataclass with slots
│   ├── storage.py               # TaskStorage protocol & JsonStorage implementation
│   └── ui.py                    # Rich console tables, panels & formatting
├── pyproject.toml               # PEP 517/518 build config & CLI console scripts
├── requirements.txt             # Direct dependencies
├── LICENSE                      # MIT License
├── README.md                    # English documentation
└── README.es.md                 # Spanish documentation
```

---

## ⚙️ Tech Stack

| Component | Technology | Purpose |
| --- | --- | --- |
| **Language** | Python 3.10+ | Core language with type hints & slots |
| **CLI Framework** | Typer (Click) | Command parsing, help generation, exit codes |
| **Terminal UI** | Rich | Colored tables, panels, status glyphs |
| **Persistence** | JSON / Pathlib | Portable file-based storage with protocol abstraction |
| **Testing** | Pytest | Automated unit & integration testing |
| **Linter & Formatter** | Ruff | Modern static analysis and style formatting |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher.
- `pip` package manager.

### 1. Clone the Repository
```bash
git clone https://github.com/aledash3/todo-cli-python.git
cd todo-cli-python
```

### 2. Install the Package
To register the `todo` command globally in your virtual environment:
```bash
pip install -e .
```

To install test dependencies as well:
```bash
pip install -e ".[test]"
```

---

## ▶️ Usage & CLI Reference

### Available Commands

| Command | Arguments / Flags | Description |
| :--- | :--- | :--- |
| `todo add` | `<description>` | Add a new task to your list |
| `todo list` | None | Display all tasks with status & summary stats |
| `todo show` | `<task_id>` | Display detailed view of a specific task |
| `todo search` | `<query>` | Search tasks by keyword in their description |
| `todo complete` | `<task_id>` | Mark a pending task as completed |
| `todo update` | `<task_id> <new_description>` | Edit an existing task's description |
| `todo remove` | `<task_id> [-y/--yes]` | Delete a task (supports non-interactive `-y`) |
| `todo pending` | None | List only pending tasks |
| `todo completed` | None | List only completed tasks |
| `todo clear-completed`| `[-y/--yes]` | Delete all completed tasks in batch |
| `todo stats` | None | View overview counts (Total, Pending, Completed) |
| `todo version` | None | Display application version |

### Examples

```bash
# Add new tasks
todo add "Review pull requests"
todo add "Configure GitHub Actions CI"

# Search tasks
todo search "Actions"

# Complete a task
todo complete 1

# List tasks
todo list

# Delete a task without interactive prompt
todo remove 2 --yes

# Clear completed tasks
todo clear-completed --yes
```

---

## 🧪 Running Automated Tests

Run the full test suite with `pytest`:

```bash
pytest -v
```

Run static analysis with `ruff`:

```bash
ruff check .
```

All pushes and pull requests trigger automated matrix testing across Python 3.10, 3.11, 3.12, and 3.13 via **GitHub Actions**.

---

## 👨‍💻 Author

**David Alejandro Cruz Palacios**  
Computer Science Engineering Student  
Universidad Politécnica Salesiana — Quito, Ecuador  
GitHub: [@aledash3](https://github.com/aledash3)

---

## 📄 License

This project is licensed under the terms of the [MIT License](LICENSE).
