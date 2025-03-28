import pytest
from main import sort_by_area, sort_by_population


@pytest.fixture
def sample_countries():
    return [
        ("CountryA", 500.0, 1000000),
        ("CountryB", 1000.0, 500000),
        ("CountryC", 200.0, 2000000),
    ]


@pytest.mark.parametrize("sort_function, key_index", [
    (sort_by_area, 1),
    (sort_by_population, 2),
])
def test_sort_functions(sort_function, key_index, sample_countries):
    sorted_countries = sort_function(sample_countries)
    sorted_values = [country[key_index] for country in sorted_countries]

    assert sorted_values == sorted(sorted_values, reverse=True)


def test_sort_functions_empty():
    assert sort_by_area([]) == []
    assert sort_by_population([]) == []


def test_sort_functions_same_values():
    data = [("CountryX", 500.0, 1000000), ("CountryY", 500.0, 1000000)]
    assert sort_by_area(data) == data
    assert sort_by_population(data) == data
