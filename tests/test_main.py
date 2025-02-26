import pytest

from src.uniq_tool.main import main


@pytest.mark.parametrize(
    "content, expected",
    [
        ("line1\nline2\nline2\nline3\nline4", "line1\nline3\nline4"),
        ("a\na\nb\nb\nc", "c"),
        ("x\nx\ny", "y"),
    ],
)
def test_only_uniq(content, expected):
    result = main(content, uniq=True)
    assert result == expected


@pytest.mark.parametrize(
    "content, expected",
    [
        ("line1\nline2\nline2\nline3\nline4", "1 line1\n2 line2\n1 line3\n1 line4"),
        ("a\na\nb\nb\nc", "2 a\n2 b\n1 c"),
        ("x\nx\ny", "2 x\n1 y"),
    ],
)
def test_only_count(content, expected):
    result = main(content, count=True)
    assert result == expected


@pytest.mark.parametrize(
    "content, expected",
    [
        ("line1\nline2\nline2\nline3\nline4", "line2"),
        ("a\na\nb\nb\nc", "a\nb"),
        ("x\nx\ny", "x"),
    ],
)
def test_only_repeated(content, expected):
    result = main(content, repeated=True)
    assert result == expected


@pytest.mark.parametrize(
    "content, expected",
    [
        ("line1\nline2\nline2\nline3\nline4", "2 line2"),
        ("a\na\nb\nb\nc", "2 a\n2 b"),
        ("x\nx\ny", "2 x"),
    ],
)
def test_repeated_and_count(content, expected):
    result = main(content, repeated=True, count=True)
    assert result == expected
