def calcular_tempo_viagem():

  tempo = distancia / velocidade
  return tempo

distancia = float(input("Digite a distância da viagem (em km): "))
velocidade = float(input("Digite a velocidade do veículo (em km/h): "))

tempo_viagem = calcular_tempo_viagem(distancia, velocidade)


print(f"O tempo de viagem será de {tempo_viagem:.2f} horas.")


def pedir_nome_motorista():
  """
  Função para solicitar ao usuário o nome do motorista e retorna o valor digitado.

  Retorno:
      str: Nome do motorista digitado pelo usuário.
  """

  # Solicita o nome do motorista ao usuário
  nome_motorista = input("Digite o nome do motorista: ")

  return nome_motorista


nome_digitado = pedir_nome_motorista()
print(f"O nome do motorista digitado foi: {nome_digitado}")