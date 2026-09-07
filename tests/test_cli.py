from typer.testing import CliRunner

from todo_cli.main import app

runner = CliRunner()


def test_cli_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "To-Do CLI" in result.stdout


def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "add" in result.stdout
    assert "search" in result.stdout


def test_cli_crud_flow(monkeypatch, tmp_path):
    test_db = tmp_path / "cli_tasks.json"
    monkeypatch.setenv("TODO_CLI_PATH", str(test_db))

    # Re-initialize controller with custom storage
    from todo_cli import main
    main.controller = main.TaskController.create_default(test_db)

    # 1. Add
    res = runner.invoke(app, ["add", "Write documentation"])
    assert res.exit_code == 0
    assert "ID: 1" in res.stdout

    # 2. Add empty
    res_err = runner.invoke(app, ["add", "   "])
    assert res_err.exit_code == 1

    # 3. List
    res_list = runner.invoke(app, ["list"])
    assert res_list.exit_code == 0
    assert "Write documentation" in res_list.stdout

    # 4. Search
    res_search = runner.invoke(app, ["search", "doc"])
    assert res_search.exit_code == 0
    assert "Write documentation" in res_search.stdout

    # 5. Complete
    res_comp = runner.invoke(app, ["complete", "1"])
    assert res_comp.exit_code == 0
    assert "completada" in res_comp.stdout

    # 6. Stats
    res_stats = runner.invoke(app, ["stats"])
    assert res_stats.exit_code == 0

    # 7. Remove with --yes
    res_rem = runner.invoke(app, ["remove", "1", "--yes"])
    assert res_rem.exit_code == 0
    assert "eliminada" in res_rem.stdout
