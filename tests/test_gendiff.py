import json
from gendiff.scripts.gendiff import generate_diff


def write_json(path, data):
    path.write_text(json.dumps(data))
    return str(path)


def test_deleted_key(tmp_path, capsys):
    f1 = write_json(tmp_path / "f1.json", {"key": "value"})
    f2 = write_json(tmp_path / "f2.json", {})
    generate_diff(f1, f2)
    assert "- key: value" in capsys.readouterr().out


def test_added_key(tmp_path, capsys):
    f1 = write_json(tmp_path / "f1.json", {})
    f2 = write_json(tmp_path / "f2.json", {"key": "value"})
    generate_diff(f1, f2)
    assert "+ key: value" in capsys.readouterr().out


def test_unchanged_key(tmp_path, capsys):
    f1 = write_json(tmp_path / "f1.json", {"key": "value"})
    f2 = write_json(tmp_path / "f2.json", {"key": "value"})
    generate_diff(f1, f2)
    assert "  key: value" in capsys.readouterr().out


def test_modified_key(tmp_path, capsys):
    f1 = write_json(tmp_path / "f1.json", {"key": "old"})
    f2 = write_json(tmp_path / "f2.json", {"key": "new"})
    generate_diff(f1, f2)
    out = capsys.readouterr().out
    assert "- key: old" in out
    assert "+ key: new" in out


def test_identical_files(tmp_path, capsys):
    data = {"host": "hexlet.io", "timeout": 50}
    f1 = write_json(tmp_path / "f1.json", data)
    f2 = write_json(tmp_path / "f2.json", data)
    generate_diff(f1, f2)
    out = capsys.readouterr().out
    assert "- " not in out
    assert "+ " not in out


def test_full_diff(tmp_path, capsys):
    f1 = write_json(tmp_path / "f1.json", {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
    })
    f2 = write_json(tmp_path / "f2.json", {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io",
        "proxy": "123.234.53.22",
    })
    generate_diff(f1, f2)
    out = capsys.readouterr().out
    assert "- follow" in out
    assert "  host" in out
    assert "  proxy" in out
    assert "- timeout" in out
    assert "+ timeout" in out
    assert "+ verbose" in out
