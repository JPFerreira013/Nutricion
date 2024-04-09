# ler de arquivo excell (Alimentos.xlsx) os dados de macros dos alimentos (proteinas, gorduras, carboidratos, calorias) para 100g
# salvar em arquivo jason, dicionario, os dados de cada alimento
# perguntar ao usuario quais alimentos e seu respectivo peso se utilizou na refeicao
# consultar se esse alimento esta na base de dados
# calcular os macros para o peso informado de cada alimento (regra de 3)
# ir somando para os macros totais da refeicao
# perguntar proximo alimento e repetir o processo anterior
# quando nao ouver mais alimentos, informar os macros totais da refeicao
import pandas as pd
import json

# Ler os dados do arquivo Excel
df = pd.read_excel("Alimentos.xlsx")

# Converter para um dicionário
alimentos_dict = df.to_dict(orient="records")

# Salvar o dicionário em um arquivo JSON
with open("alimentos.json", "w") as json_file:
    json.dump(alimentos_dict, json_file, indent=4)

# Carregar dados do arquivo JSON
with open("alimentos.json", "r") as json_file:
    alimentos_data = json.load(json_file)


def procurar_alimento(nome_alimento):
    for alimento in alimentos_data:
        if alimento['Alimento'].strip().lower() == nome_alimento.strip().lower():
            return alimento
    return None


# Lista para armazenar os alimentos da refeição
refeicao = []

# Perguntar ao usuário os alimentos e pesos
while True:
    nome_alimento = input(
        "Digite o nome do alimento (ou 'fim' para terminar): ").capitalize()
    if nome_alimento == 'Fim':
        break
    peso_alimento = float(input("Digite o peso do alimento em gramas: "))

    # Verificar se o alimento está na base de dados
    alimento_info = procurar_alimento(nome_alimento)
    if alimento_info:
        alimento_info['Peso'] = peso_alimento
        refeicao.append(alimento_info)
    else:
        print("Alimento não encontrado na base de dados.")

# Exibir os alimentos selecionados
print("\nAlimentos selecionados para a refeição:")
for alimento in refeicao:
    print(f"{alimento['Alimento']}: {alimento['Peso']}g")

# Calcular macros para o peso informado de cada alimento
for alimento in refeicao:
    peso_total = alimento['Peso']
    alimento['Proteina'] = round(alimento['Proteina'] * peso_total / 100, 1)
    alimento['Gordura'] = round(alimento['Gordura'] * peso_total / 100, 1)
    alimento['Carboidrato'] = round(
        alimento['Carboidrato'] * peso_total / 100, 1)
    alimento['Kcal'] = round(alimento['Kcal'] * peso_total / 100, 1)

# Exibir os macros calculados para cada alimento
print("\nMacros calculados para cada alimento:")
for alimento in refeicao:
    print(f"{alimento['Alimento']} - Proteína: {alimento['Proteina']}g, Gordura: {alimento['Gordura']
                                                                                  }g, Carboidrato: {alimento['Carboidrato']}g, Calorias: {alimento['Kcal']} kcal")

# Inicializar variáveis para os macros totais da refeição
total_proteina = 0
total_gordura = 0
total_carboidrato = 0
total_calorias = 0

# Somar os macros totais da refeição
for alimento in refeicao:
    total_proteina += alimento['Proteina']
    total_gordura += alimento['Gordura']
    total_carboidrato += alimento['Carboidrato']
    total_calorias += alimento['Kcal']

# Arredondar os macros totais da refeição para uma casa decimal
total_proteina = round(total_proteina, 1)
total_gordura = round(total_gordura, 1)
total_carboidrato = round(total_carboidrato, 1)
total_calorias = round(total_calorias, 1)

# Exibir os macros totais da refeição
print("\nMacros totais da refeição:")
print(f"Proteína total: {total_proteina}g")
print(f"Gordura total: {total_gordura}g")
print(f"Carboidrato total: {total_carboidrato}g")
print(f"Calorias totais: {total_calorias} kcal")
