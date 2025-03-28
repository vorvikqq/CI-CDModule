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


def sort_by_population(countries):
    return sorted(countries, key=lambda x: x[2], reverse=True)


def main():
    file_path = 'population.txt'

    try:
        countries = read_population_data(file_path)

        print("\nВідсортовано за площею:")
        for country, area, population in sort_by_area(countries):
            print(f"{country}: {area} км², {population} осіб")

        print("\nВідсортовано за населенням:")
        for country, area, population in sort_by_population(countries):
            print(f"{country}: {area} км², {population} осіб")
    except FileNotFoundError:
        print("Помилка: Файл не знайдено!")
    except ValueError as e:
        print(f"Помилка у вхідних даних: {e}")
    except Exception as e:
        print(f"Невідома помилка: {e}")


if __name__ == "__main__":
    main()
