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


@pytest.mark.parametrize("file_fixture, expected", [
    ("valid_data_file", [("USA", 9833517.0, 331002651), ("Canada", 9984670.0, 37742154)])
])
def test_read_population_data_valid(file_fixture, expected, request):
    file_path = request.getfixturevalue(file_fixture)
    assert read_population_data(file_path) == expected

@pytest.mark.parametrize("file_fixture", [
    "invalid_format_file",
    "invalid_numbers_file"
])
def test_read_population_data_invalid(file_fixture, request):
    file_path = request.getfixturevalue(file_fixture)
    with pytest.raises(ValueError):
        read_population_data(file_path)
