def calcular_tempo_viagem():

  tempo = distancia / velocidade
  return tempo

distancia = float(input("Digite a distância da viagem (em km): "))
velocidade = float(input("Digite a velocidade do veículo (em km/h): "))

tempo_viagem = calcular_tempo_viagem(distancia, velocidade)


print(f"O tempo de viagem será de {tempo_viagem:.2f} horas.")

