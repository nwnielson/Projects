class Pet :
    
    max_hunger = 100
    max_happiness = 100
    max_bond = 100
    min_hunger = 0
    min_happiness = 0
    min_bond = 0
    
    
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
        self.hunger = 50
        self.happiness = 50
        self.bond = 50
        
        
    
    def play(self) :
        self.happiness += 20
        self.hunger -= 20
        self.bond += 20
        
    def eat(self) :
        self.hunger += 20
        
    def sleep(self) :
        self.happiness += 20
        self.hunger -= 20
        
        
    def show_status(self) :
        print(f"{self.name}'s Status:\
            \nHunger: {self.hunger}\
            \nHappiness: {self.happiness}\
            \nBond: {self.bond}\n")