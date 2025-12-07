import pytest
import pandas as pd
import os
from src.loader import load_data

# Create a dummy test file
@pytest.fixture
def dummy_data_file(tmp_path):
    d = tmp_path / "test_data.txt"
    content = "Col1|Col2|Col3\nVal1|Val2|10\nValA|ValB|20"
    d.write_text(content)
    return str(d)

def test_load_data_success(dummy_data_file):
    df = load_data(dummy_data_file)
    assert df is not None
    assert df.shape == (2, 3)
    assert 'Col1' in df.columns

def test_load_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_data("non_existent_file.txt")
