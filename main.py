from api import SmartHomeAPI

def main():
    api = SmartHomeAPI()
    user = api.create_user("user1", "John Doe", "john@example.com")
    house = api.create_house("user1", "house1", "My Smart House")
    print(f"House '{house.name}' created for user '{user.name}'")

if __name__ == '__main__':
    main()
