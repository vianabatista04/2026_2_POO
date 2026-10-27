import math

class Circulo:    #entidade
    def __init__(self, raio: float=0.0):
      self.__raio=raio

    def get_raio(self) -> float:
      return self.__raio

    def set_raio(self, valor: float):
      if valor<0:
        raise ValueError("O raio não pode ser negativo!")
      self.__raio=valor

    def calcular_area(self) -> float:
        return math.pi * (self.__raio**2)

    def circunferencia(self) -> float:
        return 2* math.pi *self.__raio
        
class UI: #interface com usuário
    @staticmethod
    def main():
        x=Circulo(5.0)
        print("--- Dados do Círculo ---")
        print(f"Raio: {x.get_raio()}")
        print(f"Circunferência: {x.circunferencia():.2f}")
        print(f"Área: {x.calcular_area():.2f}")
UI.main()