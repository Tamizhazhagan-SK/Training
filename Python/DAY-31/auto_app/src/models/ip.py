from faker import Faker

def create_ip():
    fake = Faker()
    ip = []
    for i in range(1000):
        ip_addr = fake.ipv4()
        ip.append(ip_addr)
    return set(ip)    

def set_operations(set1, set2):
    """Perform common comparison operations on two sets.

    Returns the results with descriptive names so callers do not need to
    remember the position of each operation in a tuple.
    """
    return {
        "union": set1 | set2,
        "intersection": set1 & set2,
        "set1_only": set1 - set2,
        "set2_only": set2 - set1,
        "symmetric_difference": set1 ^ set2,
        "set1_is_subset": set1 <= set2,
        "set2_is_subset": set2 <= set1,
        "set1_is_superset": set1 >= set2,
        "set2_is_superset": set2 >= set1,
        "are_disjoint": set1.isdisjoint(set2),
    }