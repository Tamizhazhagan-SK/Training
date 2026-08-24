from faker import Faker

def city_loc():
    fake = Faker()
    cities = []
    for i in range(10):
        lats_longs = (fake.latitude(), fake.longitude())
        cities.append(lats_longs)

    return tuple(cities)    
