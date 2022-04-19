from Cars import create_cars, get_car_info

bmw = create_cars.Car('BMW', 'M5', 'black')
bmw.start_engine()
bmw.stop_engine()
get_car_info.get_car_info(bmw)