import unittest
from api import SmartHomeAPI, User, House, Room, Device

class TestSmartHomeAPI(unittest.TestCase):

    def setUp(self):
        """Set up before each test."""
        self.api = SmartHomeAPI()

    def test_create_user(self):
        """Test creating a new user."""
        user = self.api.create_user("user1", "John Doe", "john@example.com")
        self.assertEqual(user.user_id, "user1")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john@example.com")

    def test_create_house(self):
        """Test creating a new house."""
        user = self.api.create_user("user1", "John Doe", "john@example.com")
        house = self.api.create_house("user1", "house1", "My Smart House")
        self.assertEqual(house.house_id, "house1")
        self.assertEqual(house.name, "My Smart House")
        self.assertEqual(house.metadata, {})

    def test_add_room_to_house(self):
        """Test adding a room to a house."""
        user = self.api.create_user("user1", "John Doe", "john@example.com")
        house = self.api.create_house("user1", "house1", "My Smart House")
        room = self.api.add_room_to_house("house1", "room1", "Living Room")
        self.assertEqual(room.room_id, "room1")
        self.assertEqual(room.name, "Living Room")
        self.assertEqual(room.metadata, {})

    def test_add_device_to_room(self):
        """Test adding a device to a room."""
        user = self.api.create_user("user1", "John Doe", "john@example.com")
        house = self.api.create_house("user1", "house1", "My Smart House")
        room = self.api.add_room_to_house("house1", "room1", "Living Room")
        device = self.api.add_device_to_room("house1", "room1", "device1", "Smart Light", "light")
        self.assertEqual(device.device_id, "device1")
        self.assertEqual(device.name, "Smart Light")
        self.assertEqual(device.device_type, "light")
        self.assertEqual(device.status, "off")

    def test_read_device_data(self):
        """Test reading data from a device."""
        user = self.api.create_user("user1", "John Doe", "john@example.com")
        house = self.api.create_house("user1", "house1", "My Smart House")
        room = self.api.add_room_to_house("house1", "room1", "Living Room")
        device = self.api.add_device_to_room("house1", "room1", "device1", "Smart Light", "light")
        data = self.api.read_device_data("house1", "room1", "device1")
        self.assertEqual(data["device_id"], "device1")
        self.assertEqual(data["status"], "off")

    def test_read_room_data(self):
        """Test reading data from a room."""
        user = self.api.create_user("user1", "John Doe", "john@example.com")
        house = self.api.create_house("user1", "house1", "My Smart House")
        room = self.api.add_room_to_house("house1", "room1", "Living Room")
        device = self.api.add_device_to_room("house1", "room1", "device1", "Smart Light", "light")
        room_data = self.api.read_room_data("house1", "room1")
        self.assertEqual(room_data["room_id"], "room1")
        self.assertEqual(len(room_data["devices"]), 1)

    def test_read_house_data(self):
        """Test reading data from a house."""
        user = self.api.create_user("user1", "John Doe", "john@example.com")
        house = self.api.create_house("user1", "house1", "My Smart House")
        room = self.api.add_room_to_house("house1", "room1", "Living Room")
        device = self.api.add_device_to_room("house1", "room1", "device1", "Smart Light", "light")
        house_data = self.api.read_house_data("house1")
        self.assertEqual(house_data["house_id"], "house1")
        self.assertEqual(len(house_data["rooms"]), 1)

if __name__ == '__main__':
    unittest.main()
