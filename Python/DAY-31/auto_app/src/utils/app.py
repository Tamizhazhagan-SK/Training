from models.users import create_users, fetch_user_details
from models.projects import create_projects
from models.mapper import create_mapper
from models.lats_longs import city_loc
from models.ip import create_ip, set_operations
from models.config import car_model_set, frozen_set, car_prize
from faker import Faker

if __name__ == "__main__":
    # users = create_users()
    # projects = create_projects()
    # mapped = create_mapper(users, projects)
    # loc = city_loc()

    # print(loc)

    # ip = create_ip()
    # print(ip)


    # fake = Faker()
    # #need bmw car models
    
    # set1={"BMW X5", "BMW 3 Series", "BMW 5 Series", "BMW 7 Series", "BMW Z4"} 
    # set2={"BMW X5", "BMW 3 Series", "BMW 5 Series", "BMW 7 Series", "BMW Z4", "BMW M3", "BMW M4", "BMW M5"}
    # operations = set_operations(set1, set2)
    # print(f"Union: {operations['union']}")
    # print(f"Intersection: {operations['intersection']}")
    # print(f"BMW models only in set 1: {operations['set1_only']}")
    # print(f"BMW models only in set 2: {operations['set2_only']}")
    # print(f"Models in either set, but not both: {operations['symmetric_difference']}")
    # print(f"Set 1 is a subset of set 2: {operations['set1_is_subset']}")
    # print(f"Set 2 is a subset of set 1: {operations['set2_is_subset']}")
    # print(f"Sets are disjoint: {operations['are_disjoint']}")

    #calling frozen set
    # frozen_features = frozen_set()
    # print(f"Frozen features: {frozen_features}")

    # car_models = car_model_set()
    # print(f"Car models: {car_models}")

    # prize_dict = car_prize()
    # print(f"Car prize dictionary: {prize_dict}")

    users = fetch_user_details()
    print(f"Fetched user details: {users}")
