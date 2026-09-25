import pytest

from petroleum_units.cli import main


def test_convert_command_prints_result(capsys):
    exit_code = main(["convert", "length", "1", "ft", "m"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "0.3048" in captured.out


def test_list_categories(capsys):
    exit_code = main(["list"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "length" in captured.out
    assert "pressure" in captured.out


def test_list_units_for_category(capsys):
    exit_code = main(["list", "volume"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "bbl" in captured.out


def test_convert_unknown_category_reports_error(capsys):
    exit_code = main(["convert", "bogus", "1", "a", "b"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Erreur" in captured.err


def test_api_command(capsys):
    exit_code = main(["api", "10", "api", "sg"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "1.0" in captured.out


def test_api_command_rejects_unknown_unit():
    with pytest.raises(SystemExit):
        main(["api", "10", "bogus", "sg"])
