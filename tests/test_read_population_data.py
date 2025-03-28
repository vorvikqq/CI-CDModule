import pytest
from main import read_population_data 

@pytest.fixture
def valid_data_file(tmp_path):
    file = tmp_path / "valid_data.txt"
    file.write_text("USA, 9833517, 331002651\nCanada, 9984670, 37742154\n")
    return file

@pytest.fixture
def invalid_format_file(tmp_path):
    file = tmp_path / "invalid_format.txt"
    file.write_text("USA, 9833517\nCanada, 9984670,\n")
    return file

@pytest.fixture
def invalid_numbers_file(tmp_path):
    file = tmp_path / "invalid_numbers.txt"
    file.write_text("USA, 98x33517, 331002651\nCanada, 9984670, not_a_number\n")
    return file
