from faker import Faker
from models.car import Car

if __name__ == "__main__":
    faker = Faker()
    car = Car(make=faker.company(), model=faker.word(), year=faker.year(), color=faker.color_name(), manufacture_date=faker.date_this_century())
    print(f"Car Details: {car}")