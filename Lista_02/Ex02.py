class Viagem:    #entidade
    def __init__(self, dist_km: float = 0.0, horas: int =0, minutos:int=0):
      self.__dist_km= dist_km
      self.__horas= horas
      self.__minutos= minutos

    def get_dist_km(self) -> float:
      return self.__dist_km

    def set_dist_km(self, dist_km : float):
      if dist_km<0:
        raise ValueError("A distância não pode ser negativa!")
      self.__dist_km=dist_km

    def get_horas(self) -> int:
      return self.__horas

    def set_horas(self, horas : int):
      if horas<0:
        raise ValueError("O valor da hora não pode ser negativo!")
      self.__horas= horas

    def get_minutos(self) -> int:
      return self.__minutos

    def set_minutos(self, minutos : int):
      if minutos<0 or minutos >=60:
        raise ValueError("O valor deve estar entre 0 e 59.")
      self.__minutos= minutos

    def velocidade_media(self):
      tempo_hora=self.get_horas()+ (self.get_minutos()/60.0)
      if tempo_hora == 0:
        return 0.0
      vmedia=(self.__dist_km)/tempo_hora
      return vmedia
        
class UI: #interface com usuário
    @staticmethod
    def main():
        x=Viagem(1000.0, 8,50)
        print("--- Dados da Viagem ---")
        print(f"Distância: {x.get_dist_km()} km")
        print(f"Tempo: {int(x.get_horas()):02d}:{int(x.get_minutos()):02d}")
        print(f"Velocidade Média: {x.velocidade_media():.2f} km/h")
UI.main()