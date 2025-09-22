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
            return f"Cor: {self.color}, Tamanho:{self.size}, Umidade:{self.wetness}"
        

def main():
   toalha = Towel("azul", "m") #objeto manipulado
   while True:
        line:str = input()
        args:list[str] = line.split(" ")

        if args[0] == "end":
            break   
        elif args[0] == "criar":
             color = args[1]
             size = args[2]    
             toalha = Towel(color, size)
        elif args[0] == "mostrar":
            print(toalha)
        
        elif args[0] == "seca":
            print("sim" if toalha.dry() else "não")
        elif args[0] == "dry": #amout
            amount:int = int(args[1])
            toalha.dry(amount)
        else:
            print("fail: Comando inválido")    
        
  
main()

def main():
     toalha = Towel 
     main()
