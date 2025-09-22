class Towel: 
    def __init__(self, color:str, size: str): #construtor
        self.color: str= color
        self.size: str = size
        self.wetness: int = 0

    def dry(self, amount: int)-> None: 
            self.wetness += amount
            if self.wetness >= self.getMaxWetness():
                print("Toalha encharcada")
                self.wetness = self.getMaxWetness()

    def wringOut(self)-> None:
            self.wetness = 0
    

    def getMaxWetness(self) -> int:
            if self.size == "p":
                return 10
            if self .size == "m":
                return 20       
            if self.size == "g":
                return 30
            return 0 
        
    def __str__(self) -> str:
            return f"Cor: {self.color}, Tam:{self.size}, Umidade:{self.wetness}"
        

doguito= Towel("velha", "m")   
print(doguito)
doguito.dry(3)
print(doguito)
doguito.dry(15)
doguito.dry(10)
print(doguito)
        
  

