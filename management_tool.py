from booking import *
from room import *
from tenant import *
from exceptions import *
import datetime

class ManagementTool:
    def __init__(self):
        self.rooms = []
        self.room_types = []
        self.bookings = []

    def add_room_type(self, type_name:str, price:int):
        for room_type in self.room_types:
            if room_type == type_name:
                raise RoomTypeAlreadyExistsError(type_name)
        self.room_types.append(Type(type_name, price))
    
    def remove_room_type(self, type_name:str):
        if type_name not in [room_type.type_name for room_type in self.room_types]:
            raise RoomTypeNotFoundError(type_name)
        for booking in self.bookings:
            if booking.room.room_type == type_name:
                raise RoomTypeInUseError(type_name)
        self.room_types = [room_type for room_type in self.room_types if room_type != type_name]
        self.rooms = [room for room in self.rooms if room.room_type != type_name]

    def add_room(self, room_name:str, type_name:str):
        if type_name not in [room_type.type_name for room_type in self.room_types]:
            raise RoomTypeNotFoundError(type_name)
        for room in self.rooms:
            if room == room_name:
                raise RoomAlreadyExistsError(room_name)
        self.rooms.append(Room(room_name, [room_type for room_type in self.room_types if room_type == type_name][0]))
    
    def remove_room(self, room_name:str):
        if room_name not in [room.room_name for room in self.rooms]:
            raise RoomNotFoundError(room_name)
        for booking in self.bookings:
            if booking.room == room_name:
                raise RoomInUseError(room_name)
        self.rooms = [room for room in self.rooms if room != room_name]
            
    def add_guest(self, full_name:str, age:int, id_card_num:str, is_vip:bool, start_date:datetime.date, end_date:datetime.date):
        if len([room for room in self.rooms if not room.in_use]) == 0:
            raise NoAvailableRoomError()
        tenant = VIP(full_name, age, id_card_num) if is_vip else Person(full_name, age, id_card_num)
        room = [room for room in self.rooms if not room.in_use][0]
        room.in_use = True
        booking = Booking(tenant, room, start_date, end_date)
        self.bookings.append(booking)
        
    def remove_guest(self, id_card_num:str):
        if id_card_num not in [booking.tenant.id_card_num for booking in self.bookings]:
            raise GuestNotFoundError(id_card_num)
        for booking in self.bookings:
            if booking.tenant == id_card_num:
                booking.room.in_use = False
        self.bookings = [booking for booking in self.bookings if booking.tenant != id_card_num]

    def compute_cost_for_guest(self, id_card_num:str) -> int:
        if id_card_num not in [booking.tenant.id_card_num for booking in self.bookings]:
            raise GuestNotFoundError(id_card_num)
        return sum([booking.total_price for booking in self.bookings if booking.tenant == id_card_num])

    def show_available_rooms(self) -> list:
        return [room.room_name for room in self.rooms if not room.in_use]

    def show_occupied_rooms(self) -> list:
        return [room.room_name for room in self.rooms if room.in_use]

    def computer_total_revenue_between(self, start_date:datetime.date, end_date:datetime.date) -> int:
        return sum([booking.total_price for booking in self.bookings if booking.start_date >= start_date and booking.end_date <= end_date])
    