import json
import pytest
import yaml
from gendiff.scripts.gendiff import generate_diff


def write_json(path, data):
    path.write_text(json.dumps(data))
    return str(path)


def write_yaml(path, data):
    path.write_text(yaml.dump(data))
    return str(path)


FILE_FORMATS = pytest.mark.parametrize(
    "writer,ext",
    [
        pytest.param(write_json, "json", id="json"),
        pytest.param(write_yaml, "yaml", id="yaml"),
    ],
)


@FILE_FORMATS
def test_deleted_key(tmp_path, capsys, writer, ext):
    f1 = writer(tmp_path / f"f1.{ext}", {"key": "value"})
    f2 = writer(tmp_path / f"f2.{ext}", {})
    generate_diff(f1, f2)
    assert "- key: value" in capsys.readouterr().out


@FILE_FORMATS
def test_added_key(tmp_path, capsys, writer, ext):
    f1 = writer(tmp_path / f"f1.{ext}", {})
    f2 = writer(tmp_path / f"f2.{ext}", {"key": "value"})
    generate_diff(f1, f2)
    assert "+ key: value" in capsys.readouterr().out


@FILE_FORMATS
def test_unchanged_key(tmp_path, capsys, writer, ext):
    f1 = writer(tmp_path / f"f1.{ext}", {"key": "value"})
    f2 = writer(tmp_path / f"f2.{ext}", {"key": "value"})
    generate_diff(f1, f2)
    assert "  key: value" in capsys.readouterr().out


@FILE_FORMATS
def test_modified_key(tmp_path, capsys, writer, ext):
    f1 = writer(tmp_path / f"f1.{ext}", {"key": "old"})
    f2 = writer(tmp_path / f"f2.{ext}", {"key": "new"})
    generate_diff(f1, f2)
    out = capsys.readouterr().out
    assert "- key: old" in out
    assert "+ key: new" in out


@FILE_FORMATS
def test_identical_files(tmp_path, capsys, writer, ext):
    data = {"host": "hexlet.io", "timeout": 50}
    f1 = writer(tmp_path / f"f1.{ext}", data)
    f2 = writer(tmp_path / f"f2.{ext}", data)
    generate_diff(f1, f2)
    out = capsys.readouterr().out
    assert "- " not in out
    assert "+ " not in out


@FILE_FORMATS
def test_full_diff(tmp_path, capsys, writer, ext):
    f1 = writer(tmp_path / f"f1.{ext}", {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
    })
    f2 = writer(tmp_path / f"f2.{ext}", {
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
