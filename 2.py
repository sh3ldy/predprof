def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        p = arr[0]['price']
        mi = [x for x in arr[1:] if x['price'] < p]
        g = [x for x in arr[1:] if x['price'] >= p]
        return quick_sort(mi) + [arr[0]] + quick_sort(g)

with open('odometer_car.txt', 'r') as file:
    cars_data = []
    for line in file:
        car_info = line.split('; ')
        odometer = int(car_info[2].split(': ')[1])
        price = int(car_info[3].split(': ')[1])
        manufacturer_model = car_info[0].split(' ')
        cars_data.append({'manufacturer': manufacturer_model[0], 'model': manufacturer_model[1], 'paint_color': car_info[1].split(': ')[1], 'odometer': odometer, 'price': price})

sorted_cars = quick_sort(cars_data)

print("Вам могут подойти:")
for car in sorted_cars[:3]:
    print(f"{car['manufacturer']} {car['model']}; Цвет: {car['paint_color']}; Пробег: {car['odometer']}; Цена: {car['price']}")
