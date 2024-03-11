class Person:
    def __init__(self, full_name:str, age:int, id_card_num:str):
        self.name = full_name
        self.age = age
        self.id_card_num = id_card_num
    
    def __eq__(self, id_card_num:str):
        return self.id_card_num == id_card_num

class VIP(Person):
    discount = 0.1
    def __init__(self, full_name:str, age:int, id_card_num:str):
        super().__init__(full_name, age, id_card_num)