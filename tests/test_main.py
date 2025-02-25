import pytest

from src.uniq_tool.main import main

@pytest.mark.parametrize(
    "content, expected",
    [
        ("line1\nline2\nline2\nline3\nline4", "line1\nline2\nline3\nline4"),
        ("a\na\nb\nb\nc", "a\nb\nc"),
        ("x\nx\nx", "x"),
    ]
)
def test_remove_duplicates(content, expected):
    result = main(content, uniq=True)
    assert result == expected
