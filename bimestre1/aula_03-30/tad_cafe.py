import time

class Cafeteira:
    def __init__(self, cap_max):
        self.cap_max = cap_max
        self.nivel_agua = 0
        self.nivel_cafe = 0
        self.acesa = False

    def ligar(self):
        self.acesa = True
        print(":: Cafeteira ligada.")

    def desligar(self):
        self.acesa = False
        print(":: Cafeteira desligada.")

    def abastecer_agua(self, ml):
        if self.nivel_agua + ml <= self.cap_max:
            self.nivel_agua += ml
            print(f":: Água adicionada ({ml}ml).")
        else:
            self.nivel_agua = self.cap_max
            print(f":: Capacidade máxima atingida.")

    def abastecer_cafe(self, mg):
        self.nivel_cafe += mg
        print(f":: Café adicionado ({mg}mg).")

    def fazer_cafe(self):
        if not self.acesa:
            print("[AVISO]: Cafeteira desligada")
            return
        if self.nivel_agua >= 100 and self.nivel_cafe >= 10:
            self.nivel_agua -= 100
            self.nivel_cafe -= 10
            print(":: Preparando café...")
            time.sleep(5)
            print(":: Café servido!")
        else:
            print("[AVISO]: Insumos insuficientes (água ou café)")

    def ver_status(self):
        if self.acesa:
            estado = "ligado"
        else:
            estado = "desligado"
        print(f"Estado: {estado} | Nível de água: {self.nivel_agua} | Nível de café: {self.nivel_cafe}")