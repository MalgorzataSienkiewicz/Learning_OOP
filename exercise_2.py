class MobilePhone:
    def __init__(self,number):
        self.number = number 
        
    def turn_on(self):
        return f"mobile phone {self.number} is turned on"
        
    def turn_off(self):
        return "mobile phone is turned off"
    
    def call(number):
        return f"calling {number}"
        

phone1 = MobilePhone(444333222)
phone2 = MobilePhone(222333444)
print(phone1.turn_on())
print(phone2.turn_on())
print(MobilePhone.call(555666777))
print(phone1.turn_off())
