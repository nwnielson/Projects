class FortniteBot :
    
    def __init__(self, bot_name): #constructor -- Runs once when bot is created
        
        self.name = bot_name
        self.health = 100 #attribute
        
    def take_damge(self, amount) : #method
        self.health -= amount