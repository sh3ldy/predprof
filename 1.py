def read_car_data(filename):
    cars_data = []
    with open(filename, 'r', encoding='utf-8') as file:
        next(file)
        for line in file:
            car_info = line.strip().split('$')
            price = int(car_info[0])
            year = int(car_info[1])
            manufacturer = car_info[2]
            model = car_info[3]
            odometer = int(car_info[4])
            paint_color = car_info[5]

            cars_data.append({'price': price, 'year': year, 'manufacturer': manufacturer, 'model': model, 'odometer': odometer, 'paint_color': paint_color})
    return cars_data

cars_data = read_car_data('cars.txt')
filtered_cars = [car for car in cars_data if car['odometer'] < 10000 and car['paint_color'] == 'серебро'][:5]

write_filtered_cars('odometer_car.txt', filtered_cars)

for idx, car in enumerate(filtered_cars, 1):
    print(f"{car['manufacturer']} {car['model']} есть машина серебряного цвета. Ее стоимость {car['price']} и пробег: {car['odometer']}")
