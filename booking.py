from tenant import *
from room import *
import datetime

class Booking:
    def __init__(self, tenant:Person, room:Room, start_date:datetime.date, end_date:datetime.date):
        self.tenant = tenant
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        days = (self.end_date - self.start_date).days
        if isinstance(self.tenant, VIP):
            return self.room.room_type.price * days * (1 - VIP.discount)
        return self.room.room_type.price * days
    
    def is_complete(self):
        return self.end_date < datetime.date.today()