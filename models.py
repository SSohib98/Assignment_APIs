class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class House:
    def __init__(self, house_id, name, metadata=None):
        self.house_id = house_id
        self.name = name
        self.metadata = metadata or {}
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_id] = room

class Room:
    def __init__(self, room_id, name, metadata=None):
        self.room_id = room_id
        self.name = name
        self.metadata = metadata or {}
        self.devices = {}

    def add_device(self, device):
        self.devices[device.device_id] = device

class Device:
    def __init__(self, device_id, name, device_type, status="off"):
        self.device_id = device_id
        self.name = name
        self.device_type = device_type
        self.status = status

    def read_data(self):
        return {"device_id": self.device_id, "status": self.status}
