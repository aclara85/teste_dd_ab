class Animal:
    def __init__(self, tipo: str, som: str):
        self.tipo: str = tipo
        self.som: str = som
        self.idade: int = 0

    def __str__(self) -> str:
        return f"{self.tipo}:{self.idade}:{self.som}"
    
    def envelhecer(self,anos: int) -> None: 
        if self.idade == 4:
            print(f"aviso: {self.tipo} já morreu")
            return
        self.idade += anos
        if self.idade >= 4:
            self.idade = 4
            print(f"aviso: {self.tipo} morreu")

    def emitir_som(self) -> str:
        if self.idade == 0:
            return "_ _ _"
        elif self.idade in (1, 2, 3):
            return self.som
        elif self.idade ==4:
            return "Rip"
        
    def main():
        bicho = Animal = Animal ("", "")
        while True:
            comando: str = input()
            print("$" + comando)
            partes: list[str] = comando.split(" ")

            if partes[0] == "end":
                break
            elif partes[0] == "init":
                tipo: str = partes [1]
                som: str = partes [2]
                bicho = Animal (tipo, som)
            elif partes[0] == "show":
                print(bicho)
            elif partes[0] == "grow":
                anos: int = int(partes[1])
                bicho.envelhecer(anos)
            elif partes[0] == "noise":
                print(bicho.emitir_som())
    main()
            
