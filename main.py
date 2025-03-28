def read_population_data(file_path):
    countries = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(', ')
            if len(parts) != 3:
                raise ValueError(f"Невірний формат рядка: {line}")

            country, area, population = parts[0], parts[1], parts[2]

            if not area.replace('.', '', 1).isdigit() or not population.isdigit():
                raise ValueError(f"Помилка у форматі чисел: {line}")

            try:
                area = float(area)
                population = int(population)
                countries.append((country, area, population))
            except ValueError as e:
                raise ValueError(f"Помилка у форматі даних: {line}") from e

    return countries


def sort_by_area(countries):
    return sorted(countries, key=lambda x: x[1], reverse=True)


def main():
    file_path = 'population.txt'
    countries = read_population_data(file_path)

    print(countries)


if __name__ == "__main__":
    main()
