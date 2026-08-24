def create_mapper(users, projects):
    """Create a mapper that associates users with projects."""
    for (x,y) in zip(users, projects):
        print(f"User: {x}, Project: {y}")