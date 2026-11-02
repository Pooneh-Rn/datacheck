import pandas as pd
import pytest

from datacheck.exceptions import (
    DatasetLoadError,
    DatasetNotFoundError,
    EmptyDatasetError,
    UnsupportedFormatError,
)
from datacheck.loader import DatasetLoader


@pytest.fixture
def loader():
    return DatasetLoader()


def test_load_valid_csv(loader, tmp_path):
    """A valid CSV should load into a DataFrame."""

    file_path = tmp_path / "customers.csv"

    file_path.write_text(
        "name,age,salary\nAlice,25,45000\nBob,30,60000\n",
        encoding="utf-8",
    )

    result = loader.load(file_path)

    assert isinstance(result, pd.DataFrame)
    assert result.shape == (2, 3)
    assert list(result.columns) == [
        "name",
        "age",
        "salary",
    ]


def test_file_not_found(loader, tmp_path):
    """A nonexistent file should raise an exception."""

    file_path = tmp_path / "missing.csv"

    with pytest.raises(DatasetNotFoundError):
        loader.load(file_path)


def test_unsupported_format(loader, tmp_path):
    """Unsupported file extensions should be rejected."""

    file_path = tmp_path / "data.json"
    file_path.write_text('{"name": "Alice"}', encoding="utf-8")

    with pytest.raises(UnsupportedFormatError):
        loader.load(file_path)


def test_empty_file(loader, tmp_path):
    """An empty file should raise an exception."""

    file_path = tmp_path / "empty.csv"
    file_path.write_text("", encoding="utf-8")

    with pytest.raises(EmptyDatasetError):
        loader.load(file_path)


def test_invalid_encoding(loader, tmp_path):
    """Invalid UTF-8 should raise a loading exception."""

    file_path = tmp_path / "invalid.csv"
    file_path.write_bytes(b"name\n\xff")

    with pytest.raises(DatasetLoadError):
        loader.load(file_path)


def test_directory_is_not_a_file(loader, tmp_path):
    """Directories should not be accepted as input files."""

    with pytest.raises(DatasetLoadError):
        loader.load(tmp_path)
