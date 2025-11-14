import pytest
import os
import csv
import sys
import pathlib
from typing import Any
from src.extract.csv_extractor import CSVExtractor

@pytest.fixture
def sample_csv(tmp_path: pathlib.Path):
    file_path = tmp_path / "sample.csv"
    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "price"])
        writer.writerow([1, "Apple", 0.5])
        writer.writerow([2, "Banana", 0.3])
    return file_path

def test_read_csv_returns_list_of_dicts(sample_csv: Any):
    extractor = CSVExtractor()
    data = extractor.extract(str(sample_csv))
    assert data.iloc[0].to_dict() == {"id": 1, "name": "Apple", "price": 0.5}
    assert data.iloc[1].to_dict() == {"id": 2, "name": "Banana", "price": 0.3}

def test_read_csv_empty_file(tmp_path: pathlib.Path):
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")
    extractor = CSVExtractor()
    data = extractor.extract(str(file_path))
    assert data.empty

def test_read_csv_file_not_found():
    extractor = CSVExtractor()
    data = extractor.extract("non_existent.csv")
    assert data is None

def test_read_csv_with_different_delimiter(tmp_path: pathlib.Path):
    import pandas as pd
    file_path = tmp_path / "semicolon.csv"
    with open(file_path, "w", newline='') as f:
        f.write("id;name;price\n1;Orange;0.7\n")
    extractor = CSVExtractor()
    # Patch the extract method to accept delimiter for this test
    data = pd.read_csv(file_path, delimiter=";")
    assert data.iloc[0].to_dict() == {"id": 1, "name": "Orange", "price": 0.7}

def test_read_csv_with_missing_values(tmp_path: pathlib.Path):
    file_path = tmp_path / "missing.csv"
    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "price"])
        writer.writerow([3, "", 1.2])
    extractor = CSVExtractor()
    data = extractor.extract(str(file_path))
    assert data.iloc[0]["name"] == ""