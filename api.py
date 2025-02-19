from models import User, House, Room, Device

class SmartHomeAPI:
    def __init__(self):
        self.users = {}
        self.houses = {}

    def create_user(self, user_id, name, email):
        if user_id in self.users:
            raise ValueError("User already exists")
        user = User(user_id, name, email)
        self.users[user_id] = user
        return user

    def create_house(self, user_id, house_id, name, metadata=None):
        if house_id in self.houses:
            raise ValueError("House already exists")
        house = House(house_id, name, metadata)
        self.houses[house_id] = house
        return house

    def add_room_to_house(self, house_id, room_id, room_name, metadata=None):
        house = self.houses.get(house_id)
        if not house:
            raise ValueError("House not found")
        room = Room(room_id, room_name, metadata)
        house.add_room(room)
        return room

    def add_device_to_room(self, house_id, room_id, device_id, name, device_type):
        house = self.houses.get(house_id)
        if not house:
            raise ValueError("House not found")
        room = house.rooms.get(room_id)
        if not room:
            raise ValueError("Room not found")
        device = Device(device_id, name, device_type)
        room.add_device(device)
        return device

    def read_device_data(self, house_id, room_id, device_id):
        house = self.houses.get(house_id)
        if not house:
            raise ValueError("House not found")
        room = house.rooms.get(room_id)
        if not room:
            raise ValueError("Room not found")
        device = room.devices.get(device_id)
        if not device:
            raise ValueError("Device not found")
        return device.read_data()

    def read_room_data(self, house_id, room_id):
        house = self.houses.get(house_id)
        if not house:
            raise ValueError("House not found")
        room = house.rooms.get(room_id)
        if not room:
            raise ValueError("Room not found")
        room_data = {"room_id": room.room_id, "name": room.name, "devices": []}
        for device in room.devices.values():
            room_data["devices"].append(device.read_data())
        return room_data

    def read_house_data(self, house_id):
        house = self.houses.get(house_id)
        if not house:
            raise ValueError("House not found")
        house_data = {"house_id": house.house_id, "name": house.name, "rooms": []}
        for room in house.rooms.values():
            house_data["rooms"].append(self.read_room_data(house_id, room.room_id))
        return house_data
