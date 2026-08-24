from faker import Faker

def create_projects():
    """Create and return ten sample projects."""
    faker = Faker()
    projects = []
    for project_id in range(1, 11):
        projects.append({
            project_id,
            f"{faker.word().title()} Project",
            faker.sentence(),
        })
    return projects