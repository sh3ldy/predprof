def bin_search(cars, low, high, min_budget, max_budget):
    found_cars = []
    while low <= high:
        mid = (low + high) // 2
        price = cars[mid]['price']

        if min_budget <= price <= max_budget:
            found_cars.append(cars[mid])
            left = mid - 1
            right = mid + 1
            while left >= low and cars[left]['price'] == price:
                found_cars.append(cars[left])
                left -= 1
            while right <= high and cars[right]['price'] == price:
                found_cars.append(cars[right])
                right += 1
            return found_cars
        elif price < min_budget:
            low = mid + 1
        else:
            high = mid - 1

    return found_cars


def data(filename):
    cars_data = []
    with open(filename, 'r') as file:
        for line in file:
            car_info = line.split('; ')
            odometer = int(car_info[2].split(': ')[1])
            price = int(car_info[3].split(': ')[1])
            manufacturer_model = car_info[0].split(' ')
            cars_data.append({'manufacturer': manufacturer_model[0], 'model': manufacturer_model[1],
                              'paint_color': car_info[1].split(': ')[1], 'odometer': odometer, 'price': price})
    return cars_data

def main():
    filename = 'cars.txt'
    cars_data = data(filename)

    while True:
        user_input = input("Введите нижнюю и верхнюю границы бюджета (через пробел), или введите 'стоп' для выхода: ")

        if user_input.lower() == 'стоп':
            print("До свидания!")
            break

        min_budget, max_budget = map(int, user_input.split())
        matching_cars = bin_search(cars_data, 0, len(cars_data) - 1, min_budget, max_budget)

        if matching_cars:
            print(f"Исходя из вашего бюджета: {min_budget} - {max_budget} найдены следующие варианты:")
            for idx, car in enumerate(matching_cars, 1):
                print(
                    f"{idx}. {car['manufacturer']} {car['model']} цена {car['price']}, пробег данной машины составляет {car['odometer']}")
        else:
            print("К сожалению, под ваш бюджет ничего не удалось найти.")


if __name__ == "__main__":
    main()
