class Type:
    def __init__(self, type_name:str, price:int):
        self.type_name = type_name
        self.price = price

    def __eq__(self, type_name:str):
        return self.type_name == type_name
    
class Room:
    def __init__(self, room_name:str, room_type:Type):
        self.room_name = room_name
        self.room_type = room_type
        self.in_use = False
    
    def __eq__(self, room_name:str):
        return self.room_name == room_name