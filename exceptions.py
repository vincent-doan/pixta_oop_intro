# custom exception class

class RoomTypeAlreadyExistsError(Exception):
    def __init__(self, type_name:str):
        self.message = "Room type {} already exists".format(type_name)
        super().__init__(self.message)

class RoomTypeNotFoundError(Exception):
    def __init__(self, type_name:str):
        self.message = "Room type {} not found".format(type_name)
        super().__init__(self.message)

class RoomTypeInUseError(Exception):
    def __init__(self, type_name:str):
        self.message = "Room type {} is in use".format(type_name)
        super().__init__(self.message)

class RoomAlreadyExistsError(Exception):
    def __init__(self, room_name:str):
        self.message = "Room {} already exists".format(room_name)
        super().__init__(self.message)

class RoomNotFoundError(Exception):
    def __init__(self, room_name:str):
        self.message = "Room {} not found".format(room_name)
        super().__init__(self.message)

class RoomInUseError(Exception):
    def __init__(self, room_name:str):
        self.message = "Room {} is in use".format(room_name)
        super().__init__(self.message)

class NoAvailableRoomError(Exception):
    def __init__(self):
        self.message = "No available room"
        super().__init__(self.message)

class GuestNotFoundError(Exception):
    def __init__(self, id_card_num:str):
        self.message = "Guest with ID card number {} not found".format(id_card_num)
        super().__init__(self.message)